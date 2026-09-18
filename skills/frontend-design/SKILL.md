---
name: frontend-design
description: >-
  Especialista y arquitecto senior en Frontend Design, Sistemas de Diseño UI/UX, Estilizado Moderno y Experiencias Web de Alto Impacto.
  Utiliza este skill cuando el usuario necesite diseñar, maquetar, refinar o modernizar interfaces web (HTML, Vanilla CSS, Tailwind, React, Next.js, Vite),
  crear sistemas de diseño con tokens (colores HSL, tipografía, glassmorphism, modo oscuro), implementar micro-interacciones y animaciones fluidas,
  resolver problemas de jerarquía visual, espaciado ("apiñado"/crowded layouts), optimizar responsividad mobile-first o construir componentes visualmente deslumbrantes.
---

# Especialista en Frontend Design & Arquitectura de Interfaces

Este skill capacita al agente como un **Especialista y Diseñador Frontend Senior**, combinando maestría técnica en CSS moderno, HTML5 semántico y frameworks reactivos con sensibilidad estética de vanguardia (Dark Theme, Glassmorphism, Neumorphism sutil, animaciones `cubic-bezier` fluidas y jerarquías tipográficas de élite).

---

## 💎 Principios Fundamentales de Diseño Visual

```mermaid
graph TD
    A[Frontend Design de Élite] --> B[1. Jerarquía Visual y Espaciado]
    A --> C[2. Sistema de Tokens y Paleta]
    A --> D[3. Tipografía y Legibilidad]
    A --> E[4. Micro-interacciones y Animación]
    A --> F[5. Responsividad y Ergonomía Táctil]

    B --> B1[Regla de Espacios: Ritmo 4px/8px, Padding Generoso, Evitar Cajas Anidadas Pesadas]
    C --> C1[Glassmorphism Dark: Fondos translúcidos con backdrop-filter blur, bordes 1px alpha]
    D --> D1[Fuentes Modernas: Outfit / Plus Jakarta Sans / Inter, Eyebrows en Gradiente]
    E --> E1[Transiciones Suaves: cubic-bezier(0.16, 1, 0.3, 1), Hover translate, Resplandor]
    F --> F1[Mobile-First: Drawers con swipe, áreas táctiles mínimo 44x44px, clamp fluido]
```

---

## 🎨 Guía Rápida de Implementación

### 1. Paleta de Colores & Glassmorphism Tokens
```css
:root {
    /* Superficies y Fondos Dark */
    --bg-main: #0B0F19;
    --bg-surface: rgba(18, 24, 40, 0.65);
    --bg-surface-elevated: rgba(23, 33, 56, 0.85);
    --bg-glass: rgba(255, 255, 255, 0.03);

    /* Bordes con Transparencia Alpha */
    --border-subtle: rgba(255, 255, 255, 0.07);
    --border-hover: rgba(255, 255, 255, 0.15);
    --border-accent: rgba(168, 85, 247, 0.35);

    /* Gradientes y Acentos */
    --accent-primary: #6366F1;   /* Indigo */
    --accent-secondary: #A855F7; /* Purple */
    --accent-gradient: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
    --accent-glow: rgba(168, 85, 247, 0.25);

    /* Textos con Alto Contraste */
    --text-primary: #F8FAFC;   /* 95% White */
    --text-secondary: #CBD5E1; /* Slate 300 */
    --text-muted: #94A3B8;     /* Slate 400 */
    --text-disabled: #64748B;  /* Slate 500 */
}
```

### 2. Reglas de Oro contra el Síndrome "Apiñado" (Cramped Layouts)
1. **Nunca apilar badges redundantes sobre títulos**: Los encabezados deben tener una sola fila equilibrada con el tag/índice a la izquierda, título en el centro/izquierda y contador/chevron a la derecha.
2. **Eliminar tags genéricos repetitivos**: Si el 90% de los elementos son videos o tareas estándar, no colocar un tag de texto repetitivo en cada fila; usar un icono de estado circular sutil para liberar 60–80px de espacio horizontal.
3. **Agrupar con divisores de sección**: En estructuras anidadas (ej. subcarpetas o categorías), usar separadores de sección (`.subfolder-divider`) en lugar de repetir la ruta completa dentro de cada ítem.
4. **Espaciado fluido (`clamp`)**: Usar `clamp(min, preferred, max)` en anchos de barra lateral, tamaños de fuente y paddings para que el layout se adapte automáticamente al monitor.

---

## 📚 Módulos de Referencia y Documentación Técnica

| Módulo de Especialidad | Archivo de Referencia | Temas Clave |
| :--- | :--- | :--- |
| **Tokens, Paletas y Glassmorphism** | [01_design_tokens_and_colors.md](./references/01_design_tokens_and_colors.md) | HSL dinámico, elevaciones oscuras, sombras con tinte de acento, blur. |
| **Tipografía, Jerarquía y Badges** | [02_typography_and_hierarchy.md](./references/02_typography_and_hierarchy.md) | Escalas modulares, pairings modernos (Outfit/Plus Jakarta), tags eyebrow. |
| **Sistemas de Layout y Responsividad** | [03_layout_and_responsive_systems.md](./references/03_layout_and_responsive_systems.md) | CSS Grid, Flexbox pro, drawers móviles, scrollbars invisibles/estéticas. |
| **Micro-interacciones y Animación** | [04_micro_interactions_and_animation.md](./references/04_micro_interactions_and_animation.md) | Curvas de aceleración, hover states dinámicos, esqueletos de carga. |

---

## 🛠️ Checklist para Toda Creación o Refactor de UI

- [ ] **Contraste de Texto:** Texto principal con ratio >= 4.5:1 respecto al fondo (`#F8FAFC` o `#F1F5F9`).
- [ ] **Breathing Room:** Padding mínimo de 12px a 16px en tarjetas e ítems interactivos.
- [ ] **Truncamiento Elegante:** Títulos largos con `text-overflow: ellipsis; white-space: nowrap;` o `line-clamp: 2`.
- [ ] **Feedback Visual Inmediato:** Hover (`transform: translateX/Y`, brillo) y Active (`border-accent`, fondo iluminado).
- [ ] **Accesibilidad Táctil:** Objetivos de clic/toque de al menos 44x44px en móviles y tablets.
- [ ] **Scrollbars Personalizadas:** Barra ultrafina de 6px transparente para evitar barras grises toscas del SO.
