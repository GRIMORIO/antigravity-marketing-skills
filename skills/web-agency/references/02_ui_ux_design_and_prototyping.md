# Perfil 2: UI/UX Designer & Art Director

El **UI/UX Designer & Art Director** se encarga de conceptualizar, estructurar y diseñar experiencias visuales que impacten positivamente al usuario, combinando estética premium (Dark Glassmorphism, Neumorphism suave, tipografía editorial) con usabilidad matemática y accesible (WCAG 2.1 AA).

---

## 🎨 1. Sistema de Tokens de Diseño (Design Tokens)

Toda interfaz diseñada por la agencia debe construirse a partir de variables y tokens globales bien estructurados:

```css
:root {
    /* Superficies y Fondos */
    --bg-app: #090D16;
    --bg-surface: rgba(17, 24, 39, 0.7);
    --bg-surface-elevated: rgba(30, 41, 59, 0.85);
    --bg-glass-card: rgba(255, 255, 255, 0.035);

    /* Efectos Glassmorphism & Blur */
    --backdrop-blur-sm: blur(8px);
    --backdrop-blur-md: blur(16px);
    --backdrop-blur-lg: blur(24px);

    /* Bordes con Transparencia Alpha */
    --border-subtle: rgba(255, 255, 255, 0.08);
    --border-focus: rgba(99, 102, 241, 0.5);
    --border-hover: rgba(255, 255, 255, 0.18);

    /* Acentos & Paleta HSL */
    --primary: #6366F1;       /* Indigo 500 */
    --primary-hover: #4F46E5; /* Indigo 600 */
    --primary-light: #818CF8; /* Indigo 400 */
    --secondary: #A855F7;     /* Purple 500 */
    --accent: #EC4899;        /* Pink 500 */
    --success: #10B981;       /* Emerald 500 */
    --warning: #F59E0B;       /* Amber 500 */
    --danger: #EF4444;        /* Red 500 */

    /* Tipografía */
    --font-heading: 'Plus Jakarta Sans', 'Outfit', system-ui, sans-serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-code: 'JetBrains Mono', 'Fira Code', monospace;

    /* Sombras Elevadas y Resplandores (Ambient Glow) */
    --shadow-sm: 0 2px 8px -2px rgba(0, 0, 0, 0.4);
    --shadow-md: 0 8px 24px -4px rgba(0, 0, 0, 0.5);
    --shadow-lg: 0 16px 48px -8px rgba(0, 0, 0, 0.65);
    --glow-primary: 0 0 30px rgba(99, 102, 241, 0.25);
    --glow-secondary: 0 0 30px rgba(168, 85, 247, 0.25);

    /* Transiciones Curvadas */
    --ease-out-spring: cubic-bezier(0.16, 1, 0.3, 1);
    --transition-fast: 0.15s var(--ease-out-spring);
    --transition-normal: 0.25s var(--ease-out-spring);
}
```

---

## 📐 2. Principios de Maquetación y Espaciado (Anti-Apiñamiento)

1. **Ritmo de Espaciado 8pt**: Todo margen, padding y gap debe ser múltiplo de 8px (o sub-múltiplo de 4px): `4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px`.
2. **Jerarquía en una Sola Fila**: Evitar apilar 4 elementos uno encima de otro en encabezados de tarjeta. Usar layouts horizontales tipo Flexbox (`justify-content: space-between; align-items: center`).
3. **Píldoras y Badges Minimalistas**:
   - Usar badges discretos con fondo translúcido (`background: rgba(99, 102, 241, 0.12); color: #818CF8; border: 1px solid rgba(99, 102, 241, 0.25)`).
   - Reemplazar textos redundantes con iconos semánticos de 16x16px para preservar espacio de lectura.
4. **Espaciado Adaptativo (`clamp`)**:
   ```css
   .container {
       padding: clamp(1rem, 4vw, 3rem);
       max-width: 1280px;
       margin: 0 auto;
   }
   .hero-title {
       font-size: clamp(2rem, 5vw, 3.75rem);
       line-height: 1.15;
   }
   ```

---

## ♿ 3. Accesibilidad Web (WCAG 2.1 AA)

- **Ratio de Contraste:** Mínimo **4.5:1** para texto normal y **3:1** para texto grande (18pt / 24px o 14pt negrita).
- **Indicadores de Foco Visibles:** Nunca aplicar `outline: none` sin proveer un reemplazo accesible como `box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.45)`.
- **Touch Targets en Móviles:** Mínimo **44x44px** en todos los botones, enlaces e inputs interactivos.
- **Soporte `prefers-reduced-motion`**:
  ```css
  @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
          animation-duration: 0.01ms !important;
          animation-iteration-count: 1 !important;
          transition-duration: 0.01ms !important;
          scroll-behavior: auto !important;
      }
  }
  ```

---

## 🎬 4. Micro-interacciones y Estados de Interacción

- **Hover en Tarjetas:** Elevación sutil de 2px a 4px hacia arriba (`transform: translateY(-3px)`), aumento de borde brillante y sombra proyectada.
- **Botones Activos:** Efecto de presión táctil sutil (`transform: scale(0.98)`).
- **Esqueletos de Carga (Skeletons):** Animación de brillo shimmer suave sobre fondo translúcido mientras se recupera la información de la API.
