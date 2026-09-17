# 🚀 Antigravity Digital Marketing Skills Suite

Suite completa de **Skills y Agentes Especialistas en Publicidad Digital y Tráfico Pago** para Google Antigravity, desarrollada a partir de las metodologías avanzadas de **Alan Valdez** (Google Ads) y **Felipe Vergara** (Meta Ads / Facebook & Instagram Ads).

---

## 📂 Estructura del Repositorio

```text
.
├── rules/                                   # Directrices globales para agentes
│   ├── google_ads_guidelines.md             # Estándares de diseño y auditoría Google Ads
│   └── meta_ads_guidelines.md               # Estándares del Semáforo y CAPI Meta Ads
├── skills/
│   ├── alan-valdez-google-ads/              # 🔴 Especialista en Google Ads
│   │   ├── SKILL.md                         # Manifiesto y activación del skill
│   │   ├── references/                      # 10 manuales técnicos profundos
│   │   │   ├── 01_estrategia_y_trifecta.md
│   │   │   ├── 02_fundamentos_subastas_kpis.md
│   │   │   ├── 03_investigacion_y_keywords.md
│   │   │   ├── 04_arquitectura_campanas.md
│   │   │   ├── 05_anuncios_rsa_y_recursos.md
│   │   │   ├── 06_medicion_conversiones_gtm.md
│   │   │   ├── 07_metodo_pekao_optimizacion.md
│   │   │   ├── 08_landing_pages_alta_conversion.md
│   │   │   ├── 09_performance_max_y_otras_redes.md
│   │   │   └── 10_consultoria_y_prompts_ia.md
│   │   ├── templates/                       # Plantillas y checklists
│   │   │   ├── auditoria_cuenta_checklist.md
│   │   │   ├── estructura_campana_template.md
│   │   │   ├── negative_keywords_universal.txt
│   │   │   └── propuesta_comercial_template.md
│   │   └── scripts/                         # Herramientas ejecutables
│   │       ├── cpc_roas_calculator.py
│   │       └── keyword_match_formatter.py
│   │
│   └── felipe-vergara-meta-ads/             # 🔵 Especialista en Meta Ads
│       ├── SKILL.md                         # Manifiesto y activación del skill
│       ├── references/                      # 12 manuales técnicos profundos
│       │   ├── 01_trafficker_y_ciclos_de_venta.md
│       │   ├── 02_investigacion_7_maletas.md
│       │   ├── 03_triangulo_dorado_y_oferta.md
│       │   ├── 04_audiencias_y_segmentacion.md
│       │   ├── 05_copywriting_niveles_consciencia.md
│       │   ├── 06_los_10_artes_que_venden.md
│       │   ├── 07_lanzamiento_cbo_vs_abo.md
│       │   ├── 08_semaforo_de_decisiones.md
│       │   ├── 09_escalado_horizontal_vertical.md
│       │   ├── 10_pixel_capi_y_medicion.md
│       │   ├── 11_meta_advantage_y_ia.md
│       │   └── 12_ventas_por_whatsapp_business.md
│       ├── templates/                       # Plantillas y checklists
│       │   ├── auditoria_meta_ads_checklist.md
│       │   ├── estructura_meta_campaign_template.md
│       │   ├── guion_cierre_whatsapp_template.md
│       │   └── semaforo_decisiones_cheatsheet.md
│       └── scripts/                         # Herramientas ejecutables
│           ├── meta_metrics_analyzer.py
│           └── meta_scaling_calculator.py
└── README.md
```

---

## 🎯 Resumen de Habilidades

### 1. Especialista en Google Ads (`alan-valdez-google-ads`)
- **Filosofía**: La *Trifecta del Éxito* (Tráfico Calificado + Oferta/Landing + Medición/PEKAO).
- **Framework de Optimización**: Método **P.E.K.A.O.** (Presupuestos, Estructura, Keywords, Anuncios, Otros).
- **Formatos**: Búsqueda Adaptable (RSA), Performance Max (PMax), Google Shopping, Display y YouTube Ads.
- **Tracking Avanzado**: Google Tag Manager (GTM), Conversiones Mejoradas (Enhanced Conversions) y GA4.

### 2. Especialista en Meta Ads (`felipe-vergara-meta-ads`)
- **Filosofía**: El *Triángulo Dorado* (Oferta 50%, Creativo 30%, Audiencia 20%).
- **Framework de Optimización**: El **Semáforo de Decisiones** (🔴 Rojo: Pausar, 🟡 Amarillo: Optimizar, 🟢 Verde: Escalar).
- **Creativos y Copy**: Los *10 Tipos de Artes Ganadores*, ganchos de 3s y los *5 Niveles de Consciencia*.
- **Escalado Seguro**: Protocolo de escalado vertical (+20% cada 48h) y horizontal (Lookalikes, Broad, DABA).
- **Ventas Conversacionales**: Estrategia de cierre y embudos Click-to-WhatsApp Business.

---

## 💻 Herramientas de Línea de Comandos (CLI)

### Google Ads
```bash
# Formatear lista de palabras clave a concordancia exacta, frase y negativas
python3 skills/alan-valdez-google-ads/scripts/keyword_match_formatter.py "curso google ads" "agencia sem"

# Calcular métricas de rentabilidad (CPA de equilibrio, Breakeven ROAS y Presupuesto diario)
python3 skills/alan-valdez-google-ads/scripts/cpc_roas_calculator.py -t 500 -m 70 -c 4.5
```

### Meta Ads
```bash
# Proyectar plan de escalado seguro sin romper la fase de aprendizaje (+20% cada 48h)
python3 skills/felipe-vergara-meta-ads/scripts/meta_scaling_calculator.py -p 50 -i 20 -c 6

# Analizar métricas con diagnóstico del Semáforo de Decisiones
python3 skills/felipe-vergara-meta-ads/scripts/meta_metrics_analyzer.py -g 150 -c 10 -t 20 --clics 350 --visitas 320 --ctr 2.1 --frecuencia 1.4
```

---

## 🛠️ Instalación y Uso en Antigravity

Este repositorio funciona de forma nativa como el directorio `.agents/` en cualquier workspace de Google Antigravity, o puede instalarse globalmente copiando los contenidos a `~/.gemini/config/`.
