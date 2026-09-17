# Módulo 2: Fundamentos, Sistema de Subastas, Quality Score y KPIs

## 1. El Sistema de Subasta de Google Ads y el Ad Rank

A diferencia de una subasta tradicional donde solo gana el mejor postor económico, en Google Ads la posición de un anuncio está determinada por el **Ad Rank (Ranking del Anuncio)**:

$$\text{Ad Rank} = \text{CPC Máximo Ofertado} \times \text{Nivel de Calidad (Quality Score)} + \text{Impacto Estimado de Recursos (Extensiones)}$$

### Fórmula del Coste Real por Clic (CPC Real):
Google utiliza la subasta de segundo precio generalizada:

$$\text{CPC Real a Pagar} = \frac{\text{Ad Rank del competidor inmediatamente inferior}}{\text{Tu Nivel de Calidad}} + 0.01\$$

> [!TIP]
> Si tu Nivel de Calidad es 10/10 y tu competidor tiene 5/10, tú pagarás **la mitad** de lo que él paga por clic para ocupar la misma o mejor posición.

---

## 2. Los 3 Pilares del Nivel de Calidad (Quality Score: 1 a 10)

El Quality Score se evalúa en una escala del 1 al 10 para cada palabra clave activa:

1. **CTR Esperado (Expected CTR)**:
   - Probabilidad histórica de que tu anuncio reciba un clic cuando se muestre para esa keyword.
   - *Cómo mejorarlo*: Usar keywords en el título del anuncio, llamados a la acción claros y diferenciadores potentes.
2. **Relevancia del Anuncio (Ad Relevance)**:
   - Grado de coincidencia temática entre la palabra clave y el texto del anuncio.
   - *Cómo mejorarlo*: Crear grupos de anuncios temáticos hiper-específicos (no mezclar conceptos distintos en un mismo grupo).
3. **Experiencia en la Página de Destino (Landing Page Experience)**:
   - Relevancia del contenido web con la búsqueda, velocidad de carga (móvil y desktop), transparencia, navegación intuitiva y baja tasa de rebote.
   - *Cómo mejorarlo*: Título de la página coincidente con el anuncio, carga en menos de 2.5 segundos y contenido claro.

---

## 3. Jerarquía y Niveles de una Cuenta de Google Ads

```text
Nivel 1: Cuenta de Google Ads (Email, Facturación, Zona Horaria, Moneda)
 └── Nivel 2: Campañas (Objetivo, Presupuesto Diario, Redes, Idiomas, Geolocalización, Estrategia de Puja)
      └── Nivel 3: Grupos de Anuncios (Temática específica, Segmentación)
           ├── Palabras Clave (Concordancias exactas, frase, amplia y negativas)
           ├── Anuncios (RSA - Responsive Search Ads con 15 títulos y 4 descripciones)
           └── Recursos / Extensiones (Sitelinks, Llamadas, Callouts, Imágenes, etc.)
```

---

## 4. KPIs y Métricas Esenciales en Google Ads

### Métricas de Volumen y Coste
- **Impresiones**: Número de veces que el anuncio apareció en pantalla.
- **Clics**: Número de interacciones de clic en el anuncio.
- **CTR (Click-Through Rate)**: $\frac{\text{Clics}}{\text{Impresiones}} \times 100$. Un buen CTR en búsqueda supera el 4% - 8% (en marca supera el 15%).
- **CPC Medio (Cost Per Click)**: $\frac{\text{Coste Total}}{\text{Clics}}$.

### Métricas de Negocio y Conversión
- **Conversiones**: Acciones de valor completadas (ventas, leads, llamadas, WhatsApps).
- **Tasa de Conversión (CR - Conversion Rate)**: $\frac{\text{Conversiones}}{\text{Clics}} \times 100$.
- **CPA (Cost Per Acquisition / Coste por Conversión)**: $\frac{\text{Coste Total}}{\text{Conversiones}}$.
- **Valor de Conversión**: Ingresos monetarios generados por las conversiones.
- **ROAS (Return On Ad Spend)**: $\frac{\text{Valor de Conversión}}{\text{Coste Total}} \times 100$ (o multiplicador: ej. 5x = 500%).

### Métricas de Cuota de Mercado
- **Search Impression Share (Cuota de Impresiones de Búsqueda)**: % de impresiones obtenidas vs impresiones totales para las que eras apto a competir.
- **Search Lost IS (Budget)**: % de impresiones perdidas por falta de presupuesto diario.
- **Search Lost IS (Rank)**: % de impresiones perdidas por bajo Ad Rank (Quality Score o pujas bajas).

---

## 5. Cómo Calcular el Presupuesto Inicial Recomendado

Para que una campaña pueda recopilar suficiente significancia estadística inicial, se debe calcular el presupuesto diario mínimo con la siguiente regla:

$$\text{Presupuesto Diario Mínimo} \ge \text{CPC Estimado} \times 10 \text{ clics/día}$$
$$\text{Presupuesto Diario Óptimo} \ge \text{CPA Estimado Deseado} \times 2 \text{ conversiones/día}$$
