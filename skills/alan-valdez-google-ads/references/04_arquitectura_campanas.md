# Módulo 4: Arquitectura de Campañas, Configuración y Estrategias de Puja

## 1. Estructuras de Campañas Ganadoras

La arquitectura de una cuenta determina cómo se distribuye el presupuesto y qué tan preciso es el control del rendimiento.

### Modelo A: Estructura por Intención y Tipo de Tráfico (Recomendado)
```text
Campaña 1: [Búsqueda] - Marca (Brand)
 └── Grupo: Nombre de la Empresa / Marca Registrada (Concordancia exacta y frase)

Campaña 2: [Búsqueda] - Servicios / Productos Principales (Core Generic)
 ├── Grupo 1: Servicio A - Alta Intención
 ├── Grupo 2: Servicio B - Alta Intención
 └── Grupo 3: Servicio C - Alta Intención

Campaña 3: [Búsqueda] - Competidores (Opcional)
 └── Grupo 1: Competidor A, Competidor B (Concordancias exactas con página comparativa)

Campaña 4: [PMax o Shopping o Remarketing] - Rendimiento y Escala
```

### Modelo B: Estructura por Ubicación Geográfica (Para Negocios Locales / Multisede)
- Separar campañas si las ciudades/regiones tienen presupuestos independientes o CPCs muy dispares (ej. Campaña Madrid vs Campaña Barcelona o Campaña CDMX vs Campaña Monterrey).

---

## 2. Configuración Inicial Crítica (Evitar Errores de Novato)

Al configurar una campaña de búsqueda en Google Ads, aplica siempre estos ajustes:

1. **Redes**:
   - ✅ Red de Búsqueda activada.
   - ❌ **Desactivar siempre la opción "Incluir la Red de Display de Google"** (esta casilla mezcla inventario de baja calidad en campañas de búsqueda y arruina métricas y presupuesto).
   - Socios de búsqueda de Google (Google Search Partners): Probar al inicio, pero monitorear por separado y pausar si el CPA es elevado.
2. **Ubicaciones (Segmentación Geográfica)**:
   - Cambiar la opción predeterminada de *"Presencia o interés"* a **"Presencia: personas que se encuentran en tus ubicaciones incluidas o que las visitan con frecuencia"**. Esto evita que personas de otros países que solo buscaron información reciban tus anuncios locales.
3. **Idiomas**:
   - Seleccionar el idioma principal del mercado (ej. Español) y también **Inglés** (ya que muchos usuarios tienen sus navegadores o teléfonos configurados en inglés).
4. **Rotación de Anuncios**:
   - Configurar en *"Optimizar: preferir los anuncios con mejor rendimiento"*.

---

## 3. Estrategias de Puja y Cuándo Utilizar Cada Una

| Estrategia de Puja | Tipo | Cuándo Usarla (Fase del Proyecto) | Objetivo y Cuidados |
| :--- | :--- | :--- | :--- |
| **Maximizar Clics (con límite de CPC)** | Automatizada básica | **Fase 1 (Día 1 a 30)**: Cuentas nuevas sin historial de conversiones. | Obtener el máximo tráfico inicial posible dentro del presupuesto. **Obligatorio fijar un límite de CPC máximo** para evitar que Google pague CPCs inflados. |
| **CPC Manual (+ CPC Mejorado opcional)** | Manual | **Fase 1**: Cuando se requiere control quirúrgico de cada puja por palabra. | Permite controlar cuánto pagar exactamente por cada keyword. Requiere gestión activa. |
| **Maximizar Conversiones** | Smart Bidding (IA) | **Fase 2**: Cuenta con +15-20 conversiones mensuales registradas. | El algoritmo de Google busca conseguir la mayor cantidad de conversiones gastando todo el presupuesto diario. |
| **CPA Objetivo (tCPA)** | Smart Bidding (IA) | **Fase 2 / 3**: Cuenta madura (+30 conversiones/mes) con CPA histórico estable. | Consigue la mayor cantidad de conversiones al coste por adquisición deseado. Fija un tCPA realista basado en los últimos 30 días (no un CPA ficticio e inalcanzable). |
| **Maximizar Valor de Conversión / ROAS Objetivo (tROAS)** | Smart Bidding (IA) | **E-commerce / Cuentas de valor variable**: Con +50 ventas/mes y valores dinámicos. | Optimiza para obtener el mayor retorno de inversión en ingresos. Ejemplo: Si tu objetivo es un 400% de ROAS, fijar 400% como tROAS. |

---

## 4. Distribución de Presupuestos entre Campañas

- **70% - Campañas Core / Alta Intención**: Campañas de búsqueda con términos transaccionales comprobados.
- **20% - Campañas de Escala / Rendimiento**: Performance Max, Shopping o Remarketing.
- **10% - Campañas de Experimentación / Marca**: Campañas de prueba de nuevas keywords, competidores o anuncios de video.
