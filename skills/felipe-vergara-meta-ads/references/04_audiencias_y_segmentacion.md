# Módulo 4 (Parte 3): Audiencias y Segmentación en Meta Ads

## 1. Los 4 Tipos de Audiencias en Meta Ads

Meta Ads permite estructurar la segmentación en 4 grandes familias:

### 1. Segmentación Detallada (Intereses y Comportamientos)
- **Concepto**: Seleccionar temas, marcas competidoras, páginas seguidas o comportamientos de compra (ej. *Compradores que interactuaron*).
- **Mejor práctica**: Agrupar intereses por temática compacta. Probar 1 concepto temático por conjunto de anuncios (ej. Conjunto A: Competidores directos; Conjunto B: Revistas/Medios del sector; Conjunto C: Software de la industria).
- **Públicos Advantage+ (Advantage+ Audience)**: Dejar que Meta use los intereses como una *sugerencia inicial* pero pueda expandirse si encuentra conversiones más baratas fuera del público.

### 2. Públicos Personalizados (Custom Audiences - Audiencias Propias)
- **Base de Datos de Clientes (Customer Match)**: Lista de emails y teléfonos de compradores o leads previos (subida cifrada con hash).
- **Tráfico Web (Píxel / CAPI)**:
  - Visitantes de los últimos 30, 60, 90 o 180 días.
  - Personas que vieron productos específicos (`ViewContent`).
  - Carritos abandonados (`AddToCart`) de los últimos 14 a 30 días.
  - Clientes que ya compraron (`Purchase` de los últimos 180 días) para exclusión o recompra.
- **Interacción en Redes (Engagement)**:
  - Personas que interactuaron con tu cuenta de Instagram o página de Facebook en los últimos 90-365 días.
  - Personas que vieron el 50%, 75% o 95% de tus videos.

### 3. Públicos Similares (Lookalikes / LAL)
- **Concepto**: Meta analiza a tu mejor público de origen y busca en su base de usuarios al 1%, 2%, 5% o 10% más parecido en intereses y hábitos de navegación.
- **Los Mejores Públicos Similares**:
  1. LAL 1% de Compradores con Mayor Valor (Customer LTV).
  2. LAL 1% de Todos los Compradores (`Purchase`).
  3. LAL 1% de Personas que iniciaron pago (`InitiateCheckout`).
  4. LAL 1%-2% de Leads cualificados.

### 4. Segmentación Abierta (Broad Targeting)
- **Concepto**: Sin intereses ni públicos similares; solo definir país/ciudad, edad y género.
- **¿Por qué funciona hoy?**: La IA de Meta y el algoritmo de Andromeda analizan el contenido visual y el texto de tu anuncio (Machine Learning) para mostrarlo automáticamente a las personas con mayor probabilidad de convertir.
- **Requisito**: Requiere creativos con un gancho (hook) muy específico que filtre a la audiencia desde el primer segundo.

---

## 2. Regla de Exclusiones Obligatorias (Evitar Desperdicio de Presupuesto)

En campañas de prospección en frío (TOFU):
- ❌ **Excluir siempre a Compradores de los últimos 180 días** (a menos que sea una campaña específica de recompra).
- ❌ **Excluir a personas que ya interactuaron o visitaron la web en los últimos 30 días** si se tiene una campaña dedicada de retargeting (BOFU).
