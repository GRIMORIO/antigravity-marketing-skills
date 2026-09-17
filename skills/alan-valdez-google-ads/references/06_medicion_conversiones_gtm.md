# Módulo 6: Medición de Conversiones, Google Tag Manager (GTM), GA4 y Conversiones Avanzadas

## 1. Fundamentos de la Medición de Conversiones

Sin una medición precisa, el algoritmo de Google Ads optimiza a ciegas y las estrategias de puja inteligente (Smart Bidding) fallan.

### Tipos de Conversiones:
- **Macro Conversiones (Acciones Primarias de Negocio)**:
  - Compras finalizadas (e-commerce).
  - Formularios de cotización/contacto completados.
  - Llamadas telefónicas de más de 60 segundos.
  - Clics en botón de WhatsApp que inician conversación de ventas.
  - *Configurar siempre como acción "Principal" para optimización de pujas.*
- **Micro Conversiones (Acciones Secundarias de Interés)**:
  - Clics en enlaces externos, tiempo de permanencia > 2 min, descargas de PDF informativo, vistas de página clave.
  - *Configurar como acción "Secundaria" (solo para observación, sin alimentar las pujas automáticas).*

---

## 2. Métodos de Implementación de Tracking

Existen tres formas principales de implementar conversiones en Google Ads:

1. **Google Tag Manager (GTM) — Método Recomendado**:
   - Mayor flexibilidad, no requiere tocar el código del sitio en cada cambio, permite disparadores avanzados de clics, scroll, timers y dataLayer.
2. **Etiqueta de Google (Google Tag / gtag.js)**:
   - Código JavaScript insertado directamente en el `<head>` del sitio web y en la página de agradecimiento.
3. **Importación de Eventos desde Google Analytics 4 (GA4)**:
   - Permite vincular conversiones configuradas en GA4. 
   - *Nota*: La etiqueta nativa de Google Ads o GTM suele reportar con menor discrepancia y menor latencia de atribución que la importación de GA4.

---

## 3. Implementación Paso a Paso con Google Tag Manager (GTM)

### Paso 1: Etiqueta de Vinculación de Conversiones (Conversion Linker)
- Crear una etiqueta de tipo **Vinculación de conversiones** en GTM.
- Activador: **All Pages (Todas las páginas)**.
- *Propósito*: Almacena los datos de clic publicitario (`gclid`) en cookies de origen para evitar pérdidas por bloqueadores y cambios de navegador.

### Paso 2: Etiqueta de Conversión de Google Ads (Página de Agradecimiento / Thank You Page)
- Crear etiqueta: **Seguimiento de conversiones de Google Ads**.
- ID de Conversión: `AW-XXXXXXXXX`.
- Etiqueta de Conversión (Conversion Label): `AbCdEfGhIjKlMnOpQr`.
- Activador: **Vista de página** donde la URL contenga `/gracias`, `/thank-you` o `/confirmacion`.

### Paso 3: Conversión de Clics en Botón de WhatsApp
- Crear variable incorporada de GTM: `Click URL` o `Click Element`.
- Activador: **Solo enlaces** o **Todos los elementos** con condición:
  `Click URL` contiene `wa.me/` o `api.whatsapp.com/send` o clase CSS `.whatsapp-btn`.
- Crear etiqueta de conversión de Google Ads vinculada a este activador.

---

## 4. Conversiones Mejoradas (Enhanced Conversions)

Las conversiones avanzadas envían datos de clientes de origen (como email, teléfono, nombre y dirección) cifrados con algoritmo SHA-256 a Google en el momento de la conversión.

### ¿Por qué son indispensables hoy?
- Recuperan conversiones perdidas por restricciones de privacidad de Safari / iOS y cookies de terceros.
- Mejoran la precisión del modelado de conversiones y potencian el rendimiento de Smart Bidding en un 5% a 15%.

### Cómo configurarlas en GTM:
1. En la etiqueta de conversión de Google Ads, marcar la casilla *"Incluir datos proporcionados por el usuario desde tu sitio web"*.
2. Seleccionar o crear una variable de datos proporcionados por el usuario (User-Provided Data Variable).
3. Configurar la lectura de los campos (`email`, `phone_number`) mediante selectores CSS del formulario o variables de la capa de datos (`dataLayer`).

---

## 5. Vinculaciones Estratégicas de Cuentas

Para un ecosistema completo de Google Ads, vincula en la sección *Cuentas vinculadas*:
- **Google Analytics 4 (GA4)**: Para audiencias predictivas y análisis de embudo.
- **Google Tag Manager**: Para control centralizado de etiquetas.
- **Google Search Console**: Para ver datos orgánicos vs de pago en el informe de Búsqueda de pago y orgánica.
- **Google Merchant Center** (si es E-commerce): Para alimentar el feed de productos en Shopping y PMax.
- **Perfil de Empresa en Google (Google Business Profile)**: Para extensiones de ubicación local.
