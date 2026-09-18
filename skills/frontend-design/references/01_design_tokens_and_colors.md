# Tokens, Paletas de Color y Glassmorphism Moderno

## 1. Filosofía Dark Mode Premium
El modo oscuro moderno NO es negro puro (`#000000`) sobre blanco (`#FFFFFF`). Es un ecosistema de capas profundas azuladas y sombras coloreadas que simulan profundidad tridimensional:

- **Fondo Base (Nivel 0)**: `#0B0F19` o `#070A11` (Azul-negro ultra profundo).
- **Tarjetas y Contenedores (Nivel 1)**: `rgba(18, 24, 40, 0.65)` con `backdrop-filter: blur(16px);`.
- **Elementos Elevados / Modales (Nivel 2)**: `rgba(23, 33, 56, 0.85)`.
- **Bordes Alpha**: `1px solid rgba(255, 255, 255, 0.08)`. Da definición nítida sin sentirse pesado.

## 2. Sombras con Tinte (Glow & Ambient Lighting)
Evita sombras negras duras (`box-shadow: 0 4px 10px #000`). En su lugar, usa iluminación ambiental teñida por el color de acento:
```css
/* Sombra estándar de tarjeta */
box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.05);

/* Tarjeta activa o destacada con resplandor neón */
box-shadow: 0 8px 30px -4px rgba(168, 85, 247, 0.25), 0 0 0 1px rgba(168, 85, 247, 0.4);
```

## 3. Receta Glassmorphism Perfecta
Para lograr un efecto de cristal esmerilado sin saturar la GPU:
```css
.glass-card {
    background: rgba(18, 24, 40, 0.6);
    backdrop-filter: blur(16px) saturate(180%);
    -webkit-backdrop-filter: blur(16px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
}
```
