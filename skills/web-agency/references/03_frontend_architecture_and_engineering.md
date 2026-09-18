# Perfil 3: Frontend Architect & Lead Engineer

El **Frontend Architect & Lead Engineer** es el responsable de traducir los diseños del equipo de UX en código modular, performante, mantenible y libre de bugs, garantizando una experiencia de usuario fluida a 60 FPS y puntuaciones verdes en Google Core Web Vitals.

---

## 🏗️ 1. Estructura de Proyectos Frontend

### Estructura de Proyecto Recomendada (Modular / Feature-Based)

```text
src/
├── assets/          # Imágenes optimizadas (WebP/SVG), fuentes, iconos
├── components/      # Componentes UI atómicos y reutilizables
│   ├── ui/          # Button, Modal, Input, Badge, Toast, Dropdown
│   └── layout/      # Navbar, Sidebar, Footer, Container, Drawer
├── features/        # Módulos por dominio de negocio (Auth, Checkout, Player, Catalog)
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── types/
├── hooks/           # Custom React hooks o utilidades reactivas
├── services/        # Clientes HTTP (fetch / axios wrapper), interceptores
├── store/           # Estado global (Zustand, Redux Toolkit o Context)
├── styles/          # Variables globales, reset, animaciones CSS
└── utils/           # Helpers puros (dateFormatter, numberFormat, validators)
```

---

## ⚡ 2. Core Web Vitals & Optimización de Rendimiento

Para alcanzar un puntaje de **95+ en Google PageSpeed Insights**:

| Métrica | Objetivo | Qué Mide | Técnicas de Optimización de la Agencia |
| :--- | :---: | :--- | :--- |
| **LCP** *(Largest Contentful Paint)* | `< 2.5s` | Velocidad de carga del elemento visual principal | Formatos WebP/AVIF modernos, `fetchpriority="high"` en hero images, precarga de fuentes críticas. |
| **INP** *(Interaction to Next Paint)* | `< 200ms` | Capacidad de respuesta a clics/toques | Desacoplar tareas pesadas con `requestAnimationFrame` o Web Workers, debouncing en inputs de búsqueda. |
| **CLS** *(Cumulative Layout Shift)* | `< 0.1` | Estabilidad visual durante la carga | Definir siempre `aspect-ratio` o `width` y `height` explícitos en imágenes y videos; reservar espacio con placeholders/esqueletos. |

### Snippet de Carga Óptima de Fuentes e Imágenes
```html
<!-- Precarga de Fuente Primaria -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap">

<!-- Imagen Hero Optimizada con Prioridad Alta -->
<img src="/assets/hero-banner.webp"
     srcset="/assets/hero-banner-480w.webp 480w, /assets/hero-banner-1080w.webp 1080w"
     sizes="(max-width: 768px) 100vw, 1200px"
     width="1200" height="630"
     fetchpriority="high"
     alt="Plataforma de cursos"
     loading="eager"
     decoding="async">
```

---

## 📱 3. Responsive Web Design & Mobile-First

1. **Breakpoints Estándar:**
   - Móvil pequeño: `< 480px`
   - Móvil / Tablet Portrait: `481px – 768px`
   - Tablet Landscape / Laptop: `769px – 1024px`
   - Desktop: `1025px – 1440px`
   - Pantallas Ultrawide: `> 1440px`
2. **Uso de Flexbox y CSS Grid Moderno:**
   ```css
   /* Grid auto-fit que no requiere media queries */
   .card-grid {
       display: grid;
       grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
       gap: 1.5rem;
   }
   ```
3. **Gestión de Menús Móviles (Drawers):**
   - Transición fluida con `transform: translateX(-100%)` a `translateX(0)`.
   - Soporte para cierre mediante gesto *Swipe* hacia la izquierda y tecla `Escape`.

---

## 🛡️ 4. Manejo Robusto de Estados y Errores

- **Estados de Carga:** Siempre mostrar indicadores de carga elegantes (esqueletos o spinners con brillo).
- **Estados Vacíos (Empty States):** Ilustración/icono claro + título + mensaje amigable + botón de acción principal.
- **Límites de Error (Error Boundaries / Toasts):** Si una petición falla, mostrar un Toast discreto con opción de reintentar sin romper la vista del usuario.
