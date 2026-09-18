# Plantilla Estándar de Reporte de Auditoría UX/UI

```markdown
# 📋 Reporte de Auditoría de Calidad UX/UI

## 1. Resumen Ejecutivo
- **Pantalla / Componente Evaluado:** [Nombre del componente o URL]
- **Puntuación Global de Usabilidad:** [8.5 / 10]
- **Total de Hallazgos:** [X Críticos, Y Mayores, Z Menores]

---

## 2. Tabla de Hallazgos y Severidad

| ID | Componente | Hallazgo / Defecto | Severidad | Impacto | Solución Recomendada |
| :--- | :--- | :--- | :--- | :--- | :--- |
| #01 | `.module-header` | Título oculto en estado colapsado | **P1 (Mayor)** | Usuario no sabe qué contiene el módulo | Unificar en 1 fila con título siempre visible |
| #02 | `.lesson-item` | Etiquetas repetitivas reducen espacio | **P2 (Menor)** | Títulos se parten en 4 líneas apretadas | Agrupar por subcarpeta y remover tag |

---

## 3. Comparativa Antes vs. Después (Visual Walkthrough)
- **Antes:** [Descripción o captura del problema visual]
- **Después:** [Descripción o captura de la solución aplicada]

---

## 4. Plan de Acción y Verificación
- [x] Corrección de estilos CSS y marcado HTML.
- [x] Prueba de estrés con nombres largos.
- [x] Verificación en viewport móvil (375px) y desktop (1440px).
```
