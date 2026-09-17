# Módulo 6: El Semáforo de Decisiones (Metodología de Optimización de Felipe Vergara)

## 1. Fundamentos del Semáforo de Decisiones

El **Semáforo de Decisiones** es la regla sistemática creada por Felipe Vergara para eliminar la subjetividad y el miedo en la gestión de Meta Ads. Permite saber con exactitud cuándo apagar un anuncio, cuándo modificar la oferta/página web y cuándo escalar el presupuesto.

```text
🔴 SEMÁFORO ROJO: Pausar o Corregir Errores Críticos (No es rentable o no gasta)
🟡 SEMÁFORO AMARILLO: Optimizar Fricciones (Rentabilidad al límite / Fugas de embudo)
🟢 SEMÁFORO VERDE: Escalar con Confianza (Rentable, volumen constante, CPA óptimo)
```

---

## 2. Diagnóstico del Semáforo Rojo 🔴 (Causas y Acciones)

Un elemento entra en **Semáforo Rojo** cuando:
1. **Nivel Anuncio**:
   - Ha gastado el equivalente a **1.5x o 2x el CPA Objetivo** sin conseguir ninguna conversión -> **PAUSAR DE INMEDIATO**.
   - El CTR (único en el enlace) es menor al 0.8% - 1.0% en móvil -> El creativo o el gancho inicial es aburrido y no detiene el scroll.
   - El CPC en el enlace es demasiado alto para el margen del producto.
2. **Nivel Conjunto de Anuncios**:
   - El conjunto ha gastado 2x el CPA objetivo sin conversiones -> Pausar conjunto o probar nuevo ángulo de audiencia.
   - **Fatiga de Anuncios (Frecuencia > 3.5 en prospección)**: La audiencia está saturada y los costes se disparan.
3. **Nivel Destino / Landing Page (Fuga Crítica)**:
   - **Tasa de Conexión de Clics a Visitas**: Compara `Clics en el enlace` vs `Visitas a la página de destino (Landing Page Views)`.
   - Si la pérdida es mayor al **25% - 30%** (ej. 100 clics y solo 60 visitas registradas), el sitio web carga lento (> 3 segundos) o hay un fallo técnico en el servidor.
4. **Nivel Oferta**:
   - Tienes muchas visitas a la web y carritos agregados, pero cero compras -> La oferta no convence, el envío es muy caro o hay falta de pasarelas de pago locales confiables.
5. **No Hay Impresiones (Gasto Cero)**:
   - El anuncio está rechazado, el método de pago falló, la puja manual es demasiado baja o la audiencia es excesivamente pequeña (<10,000 personas).

---

## 3. Diagnóstico del Semáforo Amarillo 🟡 (Optimización)

Un elemento entra en **Semáforo Amarillo** cuando:
- El CPA está cerca del punto de equilibrio (Breakeven) o fluctúa entre rentable y no rentable.
- Buen CTR en el anuncio (> 1.5%), pero baja tasa de conversión en la landing page (< 2%).

### Acciones para Semáforo Amarillo:
- Optimizar la experiencia de la página web (agregar botón de WhatsApp flotante, simplificar formulario).
- Probar un nuevo gancho (Hook) en los primeros 3 segundos de video conservando el resto del video ganador.
- Probar un nuevo ángulo de copy enfocado en derribar la objeción principal (precio o desconfianza).

---

## 4. Diagnóstico del Semáforo Verde 🟢 (Escalamiento)

Un elemento entra en **Semáforo Verde** cuando:
- El CPA está de forma consistente por debajo del CPA objetivo durante al menos 3 a 5 días consecutivos.
- El ROAS supera el objetivo mínimo con al menos 10-15 conversiones registradas.
- La frecuencia se mantiene baja (< 2.0 en prospección).

### Acciones para Semáforo Verde:
- **Escalar Verticalmente**: Incrementar el presupuesto entre un **15% y un 20%** cada 48 a 72 horas.
- **Escalar Horizontalmente**: Duplicar el anuncio o Post ID hacia nuevas audiencias (Lookalikes, Broad o países vecinos).

---

## 5. Ventana de Atribución y Configuración de Columnas

Para aplicar el Semáforo de Decisiones con precisión, configura estas columnas personalizadas en el Administrador de Anuncios:
1. Nombre del anuncio / conjunto
2. Entrega e Importe gastado
3. Resultados (Compras / Clientes potenciales)
4. Coste por resultado (CPA)
5. Valor de conversión de compras / ROAS de compras
6. Clics en el enlace (únicos)
7. CTR (único en el enlace)
8. CPC (coste por clic en el enlace)
9. Visitas a la página de destino (Landing Page Views)
10. Pagos iniciados / Artículos agregados al carrito
11. Frecuencia
- **Atribución recomendada**: 7 días después de hacer clic o 1 día después de ver (7-day click or 1-day view).
