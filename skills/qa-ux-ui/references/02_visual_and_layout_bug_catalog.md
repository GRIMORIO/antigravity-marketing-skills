# Catálogo de Defectos Visuales y Soluciones Técnicas

## 1. El Síndrome de Amontonamiento ("Apiñado" / Cramped Layout)
- **Síntoma:** Elementos pegados sin margen, badges apilados sobre títulos, filas angostas donde el texto se quiebra en muchas líneas.
- **Causa Raíz:** Falta de padding en tarjetas, uso de anchos rígidos insuficientes (`width: 320px`), inclusión de etiquetas de texto redundantes.
- **Solución:** 
  1. Aumentar el ancho de la barra lateral con `clamp(380px, 26vw, 460px)`.
  2. Unificar el encabezado en una sola fila (`flex-direction: row; justify-content: space-between`).
  3. Reemplazar badges de texto por iconos minimalistas.

## 2. Cortes de Chevron o Iconos (Clipping / Overflow Bugs)
- **Síntoma:** El icono de flecha/chevron se corta por la mitad en la parte inferior o derecha.
- **Causa Raíz:** `overflow: hidden` en el contenedor padre combinado con `height` fija o falta de `align-items: center` en flexbox.
- **Solución:**
  ```css
  .module-header {
      display: flex;
      align-items: center; /* Alineación vertical perfecta */
      padding: 0.85rem 1rem;
      min-height: auto;
  }
  ```

## 3. Síndrome de Cajas Anidadas (Nested Box Clutter)
- **Síntoma:** Múltiples bordes sólidos y fondos contrastados uno dentro de otro (borde en árbol, borde en módulo, borde en lección, borde en badge).
- **Causa Raíz:** Sobre-estilización sin jerarquía de elevación.
- **Solución:** Dejar los ítems de lista transparentes en reposo y usar bordes únicamente en el contenedor de módulo o en el ítem activo.

## 4. Contraste Insuficiente en Modo Oscuro
- **Síntoma:** Textos en gris oscuro (`#475569`) sobre fondo azul noche (`#0F172A`) difíciles de leer.
- **Causa Raíz:** No verificar ratios de contraste WCAG AA.
- **Solución:** Subir el texto secundario a `#CBD5E1` (Slate 300) y texto muted a `#94A3B8` (Slate 400).
