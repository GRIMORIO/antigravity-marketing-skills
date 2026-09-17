# Checklist de Auditoría de Cuentas de Google Ads (Método Alan Valdez)

Utiliza este checklist estructurado para auditar cuentas existentes de Google Ads e identificar fugas de presupuesto y oportunidades de optimización inmediata.

---

## 1. Configuración de Cuenta y Medición (Tracking)
- [ ] **Acciones de Conversión Primarias**: ¿Las conversiones principales (compras, leads, WhatsApp, llamadas) están marcadas como *Primarias*?
- [ ] **Acciones Secundarias**: ¿Las microconversiones (vistas de página, descargas) están como *Secundarias* para no contaminar las pujas automáticas?
- [ ] **Google Tag Manager (GTM)**: ¿Está instalado correctamente con la etiqueta de *Vinculación de Conversiones (Conversion Linker)* en todas las páginas?
- [ ] **Conversiones Mejoradas (Enhanced Conversions)**: ¿Están activadas y enviando datos hash de email/teléfono para compensar pérdidas de cookies?
- [ ] **Google Analytics 4**: ¿Está vinculado correctamente y exportando audiencias a Google Ads?

---

## 2. Configuración de Campañas
- [ ] **Separación de Redes**: ¿La casilla *"Incluir la Red de Display de Google"* está **DESACTIVADA** en todas las campañas de Búsqueda?
- [ ] **Ubicación Geográfica**: ¿La opción de segmentación está configurada en **"Presencia"** (en lugar de "Presencia o Interés")?
- [ ] **Idiomas**: ¿Están seleccionados tanto el idioma local (Español) como el **Inglés**?
- [ ] **Estrategia de Puja Adecuada**:
  - Cuentas nuevas / sin historial: ¿Tienen *Maximizar Clics con CPC Límite* o *CPC Manual*?
  - Cuentas con +30 conv/mes: ¿Tienen *CPA Objetivo* o *Maximizar Conversiones* configurados con valores realistas?
- [ ] **Pérdida de Impresiones por Presupuesto**: ¿El `Search Lost IS (budget)` está por debajo del 15-20% en campañas clave?

---

## 3. Estructura y Palabras Clave
- [ ] **Grupos de Anuncios Temáticos**: ¿Cada grupo de anuncios tiene entre 5 y 15 palabras clave estrechamente relacionadas (sin mezclar intenciones)?
- [ ] **Concordancias Controladas**: ¿Se evita el uso indiscriminado de concordancia amplia sin Smart Bidding? ¿Predominan `"frase"` y `[exacta]`?
- [ ] **Listas de Palabras Clave Negativas**:
  - ¿Existe una lista maestra de negativas aplicada a nivel de cuenta?
  - ¿Se excluyen términos como *gratis*, *empleo*, *pdf*, *tutorial*?
- [ ] **Informe de Términos de Búsqueda**: ¿Se revisan las búsquedas reales al menos una vez por semana?
- [ ] **Canibalización Interna**: ¿Hay palabras clave idénticas compitiendo entre diferentes grupos de anuncios?

---

## 4. Anuncios y Recursos (Extensiones)
- [ ] **Anuncios RSA Activos**: ¿Hay al menos 1 o 2 anuncios adaptables de búsqueda con calificación de eficacia *Buena* o *Excelente* por grupo?
- [ ] **Message Match**: ¿Los 3 primeros títulos del anuncio contienen las palabras clave exactas del grupo?
- [ ] **Recursos de Enlaces de Sitio (Sitelinks)**: ¿Hay al menos 4 sitelinks activos con descripciones completas y URLs únicas?
- [ ] **Recursos de Texto Destacado (Callouts)**: ¿Hay al menos 4-6 textos destacados con beneficios y diferenciadores?
- [ ] **Recursos de Llamada y Ubicación**: ¿Están configurados el teléfono y la ficha de Google Business Profile (si aplica negocio local)?
- [ ] **Recursos de Imagen**: ¿Se han subido imágenes atractivas en formato 1:1 y 1.91:1?

---

## 5. Landing Page y Experiencia de Usuario
- [ ] **Página de Destino Dedicada**: ¿El tráfico llega a una landing page específica en lugar de la home genérica?
- [ ] **Coincidencia de Titular (H1)**: ¿El titular de la landing repite la promesa del anuncio y la keyword buscada?
- [ ] **Llamada a la Acción Única**: ¿Existe un solo objetivo claro (formulario, llamada, WhatsApp) sin fugas ni menús distractores?
- [ ] **Velocidad y Móvil**: ¿Carga en menos de 3 segundos en dispositivos móviles?
- [ ] **Página de Agradecimiento**: ¿Existe una URL `/gracias` donde dispara el evento de conversión?
