# Módulo 5: Lanzamiento de Campañas, Estructuras de Embudo y CBO vs ABO

## 1. CBO (Advantage Campaign Budget) vs ABO (Ad Set Budget)

Una de las decisiones arquitectónicas clave al crear campañas en Meta Ads:

| Criterio | ABO (Presupuesto por Conjunto de Anuncios) | CBO (Presupuesto de la Campaña Advantage) |
| :--- | :--- | :--- |
| **Control del Gasto** | Tú decides exactamente cuánto gasta cada conjunto de anuncios al día. | El algoritmo de Meta distribuye el presupuesto total automáticamente entre los conjuntos. |
| **Fase Recomendada** | **Fase de Testeo (Testing)**: Para garantizar que cada audiencia o concepto creativo reciba presupuesto y datos. | **Fase de Escalamiento (Scaling)**: Para que Meta asigne el capital a la audiencia más barata en tiempo real. |
| **Tamaño de Audiencia** | Adecuado para comparar audiencias de tamaños dispares (evita que una grande absorba todo el dinero). | Exige que las audiencias tengan tamaños similares para no sesgar el gasto. |

---

## 2. La Estructura de Embudo Completo (Full-Funnel): TOFU, MOFU, BOFU

```text
┌────────────────────────────────────────────────────────────────────────┐
│  TOFU (Top of Funnel) - Prospección en Frío (70% - 80% Presupuesto)    │
│  • Audiencias: Broad (Abierta), Intereses Temáticos, Lookalikes (1-2%)│
│  • Exclusiones: Compradores de 180 días, Visitantes web de 30 días.    │
│  • Objetivo: Conseguir nuevos clientes al menor CPA posible.          │
├────────────────────────────────────────────────────────────────────────┤
│  MOFU (Middle of Funnel) - Consideración / Nutrición (10% - 15%)       │
│  • Audiencias: Interacción en Instagram/Facebook (90d), Vistas video. │
│  • Creativos: Testimonios, Prensa, Comparativas, Casos de Estudio.    │
├────────────────────────────────────────────────────────────────────────┤
│  BOFU (Bottom of Funnel) - Remarketing Caliente (10% - 15%)            │
│  • Audiencias: Visitantes web (14-30d), Carritos Abandonados (7-14d). │
│  • Creativos: Catálogo Dinámico (DPA), Descuento especial, Garantías. │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Uso de IDs de Anuncios Existentes (Dark Posts y Social Proof)

Cuando pruebas un anuncio ganador en múltiples conjuntos de anuncios o campañas:
1. No crees el anuncio desde cero en cada conjunto (eso divide la prueba social en varios IDs).
2. Obtén el **ID de la publicación (Post ID)** desde el menú *Publicaciones de la página* en el Administrador de Anuncios.
3. En el nuevo conjunto de anuncios, selecciona *"Usar publicación existente"* e introduce el ID.
4. **Beneficio**: Todos los "Me gusta", comentarios y compartidos se acumulan en una sola publicación, disparando la prueba social percibida.

---

## 4. Estructura de Campañas de Prueba de Creativos (Sandbox Creativo)

Para testear nuevos anuncios sin alterar las campañas principales de escalado:
- **Campaña ABO de Testeo**: Presupuesto de $10 - $20 USD/día por conjunto.
- Cada conjunto contiene **1 concepto o formato visual** con 2 o 3 variaciones de copy.
- Dejar correr durante 3 a 5 días hasta acumular al menos 500-1,000 impresiones por anuncio.
- Si un anuncio cumple el **Semáforo Verde**, se exporta su Post ID hacia la campaña CBO de escalado principal.
