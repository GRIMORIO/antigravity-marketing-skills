# Perfil 5: DevOps & Cloud Infrastructure Engineer (SRE)

El **DevOps & Cloud SRE** se encarga de la infraestructura de servidores, containerización, automatización de despliegues (CI/CD), certificados SSL/TLS, seguridad de red y monitoreo continuo para asegurar un **99.9% de disponibilidad (Uptime)**.

---

## 🐳 1. Containerización con Docker & Docker Compose

### Dockerfile Multi-Stage para Aplicaciones Web de Producción

```dockerfile
# Stage 1: Build & Dependencies
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --prefer-offline --no-audit
COPY . .
RUN npm run build

# Stage 2: Production Server
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production --prefer-offline --no-audit
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/public ./public

# Ejecutar como usuario no-root por seguridad
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### Docker Compose de Producción (App + Nginx + DB + Redis)

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      target: runner
    restart: unless-stopped
    environment:
      - DATABASE_URL=postgresql://user:${DB_PASSWORD}@postgres:5432/production_db
      - REDIS_URL=redis://redis:6379
    depends_on:
      - postgres
      - redis
    networks:
      - internal-net

  nginx:
    image: nginx:alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./certbot/conf:/etc/letsencrypt:ro
    depends_on:
      - app
    networks:
      - internal-net
      - public-net

  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: production_db
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - internal-net

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redisdata:/data
    networks:
      - internal-net

networks:
  internal-net:
    internal: true
  public-net:

volumes:
  pgdata:
  redisdata:
```

---

## 🚀 2. Pipeline de CI/CD (GitHub Actions)

Flujo automatizado de validación, testing y despliegue continuo:

```yaml
name: CI/CD Production Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      - name: Linting & Type Checking
        run: |
          npm run lint
          npm run typecheck

      - name: Run Unit & Integration Tests
        run: npm run test:coverage

      - name: Run E2E Smoke Tests
        run: npx playwright test

  deploy:
    needs: validate-and-test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Cloud Production via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.PROD_HOST }}
          username: ${{ secrets.PROD_USER }}
          key: ${{ secrets.PROD_SSH_KEY }}
          script: |
            cd /var/www/my-app
            git pull origin main
            docker compose build --pull app
            docker compose up -d --remove-orphans
            docker system prune -af --volumes
```

---

## 🔒 3. Configuración de Nginx & Hardening SSL/TLS

```nginx
server {
    listen 80;
    server_name misitioweb.com www.misitioweb.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name misitioweb.com www.misitioweb.com;

    ssl_certificate /etc/letsencrypt/live/misitioweb.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/misitioweb.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Compresión Gzip / Brotli
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml image/svg+xml;
    gzip_min_length 1000;

    # Proxy a la App
    location / {
        proxy_pass http://app:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Caché para Assets Estáticos
    location ~* \.(webp|png|jpg|jpeg|gif|svg|ico|woff2|woff|ttf)$ {
        expires 1y;
        add_header Cache-Control "public, no-transform, immutable";
    }
}
```
