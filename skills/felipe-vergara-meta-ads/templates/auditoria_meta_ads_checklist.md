# Checklist de Auditoría de Cuentas de Meta Ads (Método Felipe Vergara)

Utiliza este checklist exhaustivo para auditar cuentas de Facebook e Instagram Ads e identificar pérdidas de presupuesto y oportunidades de escalamiento.

---

## 1. Configuración de Medición y Píxel
- [ ] **Píxel de Meta Activo**: ¿El Píxel está instalado y disparando eventos estándar (`PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase` o `Lead`)?
- [ ] **API de Conversiones (CAPI)**: ¿La API de Conversiones está conectada vía servidor (GTM Server, Shopify o WordPress)?
- [ ] **Deduplicación de Eventos**: ¿Los eventos del Píxel y CAPI comparten el mismo `event_name` y `event_id` sin duplicar conteos?
- [ ] **Calidad de Coincidencia de Eventos (EMQ)**: ¿El puntaje de coincidencia de eventos clave (Purchase/Lead) es superior a **7.0 / 10** en el Administrador de Eventos?
- [ ] **Verificación de Dominio**: ¿El dominio del negocio está verificado en la Configuración del Negocio?

---

## 2. Estructura de Campañas y Arquitectura
- [ ] **Separación de Etapas del Embudo**: ¿Se cuenta con campañas claras de Prospección (TOFU) y Remarketing (BOFU)?
- [ ] **Exclusiones en Prospección**: ¿Se excluyen a los compradores de los últimos 180 días en las campañas frías para no pagar dos veces por el mismo cliente?
- [ ] **Uso Correcto de CBO vs ABO**: ¿Se utiliza ABO para testeo de creativos/audiencias y CBO o Advantage+ Shopping (ASC) para escalamiento?
- [ ] **Ventana de Atribución**: ¿Está configurada en 7 días tras clic o 1 día tras visualización (7-day click or 1-day view)?

---

## 3. Creativos y Anuncios
- [ ] **Diversidad de Formatos (Los 10 Tipos de Artes)**: ¿Se prueban videos UGC, demostraciones, testimonios, comparativas y carruseles?
- [ ] **Optimización para Móviles**: ¿Los creativos tienen formato 9:16 (Reels/Stories) y 1:1 (Feeds)?
- [ ] **Gancho de los Primeros 3 Segundos**: ¿Los videos tienen un gancho visual y texto claro al inicio para detener el scroll?
- [ ] **Uso de Publicaciones Existentes (Post IDs)**: ¿Se reutilizan los IDs de anuncios ganadores para consolidar la prueba social (likes y comentarios)?

---

## 4. Métricas y Diagnóstico del Semáforo
- [ ] **Frecuencia en Prospección**: ¿La frecuencia semanal se mantiene por debajo de 2.5 - 3.0 en audiencias frías?
- [ ] **Conexión Clics vs Visitas**: ¿La pérdida entre *Clics en el enlace* y *Visitas a la página de destino* es menor al 25%?
- [ ] **Control de Gasto sin Conversiones**: ¿Se han pausado los anuncios que gastaron más de 1.5x el CPA objetivo sin generar resultados?
- [ ] **Escalado Gradual**: ¿Los aumentos de presupuesto se realizan de forma segura (+15% a +20% cada 48h)?
