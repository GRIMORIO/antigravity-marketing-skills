# Módulo 7: El Método PEKAO de Optimización Sistemática

## 1. Introducción al Método PEKAO

El **Método PEKAO** es el framework de optimización recurrente desarrollado por Alan Valdez para gestionar y escalar cuentas de Google Ads de manera ordenada, evitando cambios caóticos y garantizando que cada ajuste responda a datos estadísticos sólidos.

```text
  ┌────────────────────────────────────────────────────────┐
  │                   MÉTODO P.E.K.A.O.                    │
  ├────────────────────────────────────────────────────────┤
  │  P  ───  Presupuestos & Pujas (Bidding & Budgets)     │
  │  E  ───  Estructura & Segmentación (Structure)         │
  │  K  ───  Keywords & Términos de Búsqueda (Keywords)    │
  │  A  ───  Anuncios & Creativos (Ads & Copywriting)      │
  │  O  ───  Otros, Experimentos & Landings (Others & A/B) │
  └────────────────────────────────────────────────────────┘
```

---

## 2. Desglose Paso a Paso del Método PEKAO

### 🅿️ P — Presupuestos y Pujas (Budgets & Bidding)
1. **Monitoreo de Cuota de Impresiones**:
   - Analizar `Search Lost IS (Budget)`. Si una campaña rentable pierde más del 20% de impresiones por presupuesto, incrementar el presupuesto diario gradualmente (+15% a +20% cada 4-5 días para no reiniciar el aprendizaje de Smart Bidding).
2. **Reasignación de Capital**:
   - Reducir o pausar presupuestos en campañas con CPA superior al objetivo y mover fondos hacia campañas con mejor ROAS o CPA más bajo.
3. **Ajustes de Puja por Dispositivo, Ubicación y Horario**:
   - Si en móviles el CPA es 50% más barato que en desktop (o viceversa), aplicar ajustes de puja porcentuales (+/- 20%).
   - Analizar el reporte de *Horas del día y días de la semana* para concentrar inversión en picos de conversión.

---

### 🇪 E — Estructura y Segmentación (Structure)
1. **Higiene de Grupos de Anuncios**:
   - Si un grupo de anuncios tiene más de 15 palabras clave heterogéneas, dividirlo en 2 o 3 grupos temáticos específicos con sus propios anuncios RSA alineados.
2. **Eliminación de Canibalización**:
   - Asegurar que no existan grupos de anuncios con palabras clave idénticas compitiendo entre sí dentro de la misma cuenta.
3. **Aislamiento de Ganadores (Alpha / Beta)**:
   - Extraer términos de búsqueda que generen el 80% de las conversiones y colocarlos en grupos dedicados con concordancia exacta y mayor presupuesto.

---

### 🇰 K — Keywords y Términos de Búsqueda (Keywords & Negatives)
1. **Auditoría del Informe de Términos de Búsqueda (Search Terms Report)**:
   - Revisar las consultas reales de los últimos 7, 14 y 30 días.
2. **Acción 1: Negativización Implacable**:
   - Añadir como palabra clave negativa cualquier término irrelevante, informativo no comercial o fuera de la zona de servicio que haya generado gasto sin conversiones.
3. **Acción 2: Expansión de Palabras Ganadoras**:
   - Si un término de búsqueda nuevo tiene múltiples conversiones y CPA bajo, agregarlo formalmente como palabra clave en concordancia de frase o exacta.
4. **Pausa de Keywords Ineficientes (Criterio de Gasto)**:
   - Si una palabra clave ha gastado el equivalente a **2x o 3x el CPA objetivo** sin registrar ninguna conversión, pausarla inmediatamente.

---

### 🅰️ A — Anuncios y Creativos (Ads & Assets)
1. **Eficacia del Anuncio (Ad Strength)**:
   - Mantener los RSA en nivel *Bueno* o *Excelente*.
2. **Rotación de Títulos y Descripciones**:
   - En el informe de *Recursos de anuncios*, identificar títulos o descripciones con rendimiento *Bajo* (según la evaluación de Google) y reemplazarlos por nuevos ganchos, llamados a la acción o diferenciadores.
3. **Auditoría de Recursos (Extensiones)**:
   - Verificar que todos los grupos y campañas tengan activos enlaces de sitio, texto destacado, fragmentos estructurados, imágenes y llamadas actualizados.

---

### 🅾️ O — Otros, Experimentos y Landing Pages (Others & Experiments)
1. **Experimentos de Google Ads (A/B Testing Oficial)**:
   - Probar nuevas estrategias de puja (ej: Maximizar Conversiones vs tCPA) usando la herramienta de *Experimentos* con división de tráfico 50/50 durante 4 a 6 semanas.
2. **Revisión de Métricas Competitivas (Auction Insights)**:
   - Verificar si nuevos competidores han entrado a la subasta o han subido sus cuotas de superposición.
3. **Optimización de Landing Page**:
   - Testear variaciones de titulares, formularios más cortos o nuevos botones de WhatsApp para aumentar la tasa de conversión global del sitio.

---

## 3. Calendario y Rutinas de Optimización Recomendadas

| Frecuencia | Tareas Clave del Método PEKAO |
| :--- | :--- |
| **Diario (5-10 min)** | Revisión de anomalías de gasto (picos inesperados), aprobación de anuncios y estado general de facturación/alertas. |
| **Semanal (30-45 min)** | **K**: Revisión profunda del informe de términos de búsqueda y agregado de negativas.<br>**P**: Ajustes de presupuesto y revisión de CPAs por campaña. |
| **Quincenal (1 hora)** | **A**: Análisis de rendimiento de recursos y actualización de copies RSA.<br>**E**: Reorganización de grupos sobrecargados. |
| **Mensual (2 horas)** | **O**: Análisis de Auction Insights, configuración de experimentos A/B, revisión de Quality Score histórico y reporte de rentabilidad global. |
