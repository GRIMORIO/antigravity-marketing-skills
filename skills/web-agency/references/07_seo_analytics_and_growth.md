# Perfil 7: SEO, Analytics & Growth Engineer

El **SEO, Analytics & Growth Engineer** es el responsable de maximizar la visibilidad orgánica en motores de búsqueda, optimizar las tasas de conversión (CRO) e instrumentar la capa de datos (*dataLayer / Analytics*) para medir con precisión cada interacción del usuario.

---

## 🔍 1. SEO Técnico On-Page de Élite

### Estructura Canónica del `<head>` HTML5

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Primario -->
    <title>Cursos de Google Ads y Meta Ads | Academia de Tráfico Digital</title>
    <meta name="description" content="Aprende a escalar tus campañas de Google Ads y Facebook Ads con estrategias avanzadas de Alan Valdez y Felipe Vergara. Accede a lecciones en video y recursos descargables.">
    <link rel="canonical" href="https://misitioweb.com/cursos/">
    <meta name="robots" content="index, follow, max-image-preview:large">

    <!-- Open Graph (Facebook, LinkedIn, WhatsApp) -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://misitioweb.com/cursos/">
    <meta property="og:title" content="Cursos de Google Ads y Meta Ads | Academia Digital">
    <meta property="og:description" content="Domina la compra de tráfico digital con casos prácticos y metodologías probadas.">
    <meta property="og:image" content="https://misitioweb.com/assets/og-preview.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Cursos de Google Ads y Meta Ads | Academia Digital">
    <meta name="twitter:description" content="Domina la compra de tráfico digital con casos prácticos y metodologías probadas.">
    <meta name="twitter:image" content="https://misitioweb.com/assets/og-preview.jpg">

    <!-- Favicon & PWA Icons -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <meta name="theme-color" content="#090D16">
</head>
```

---

## 📊 2. Datos Estructurados Schema.org (JSON-LD)

Implementación de marcado semántico para enriquecer los snippets de Google (*Rich Snippets*):

### Schema de Curso / Producto Educativo
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Especialización en Google Ads & Paid Search",
  "description": "Domina la creación, optimización y escalado de campañas en Google Ads aplicando la metodología PEKAO.",
  "provider": {
    "@type": "Organization",
    "name": "Academia de Tráfico Digital",
    "sameAs": "https://misitioweb.com"
  },
  "instructor": {
    "@type": "Person",
    "name": "Alan Valdez"
  },
  "educationalLevel": "Intermediate to Advanced",
  "inLanguage": "es"
}
</script>
```

---

## 📈 3. Arquitectura de Analítica (Google Tag Manager & dataLayer)

Estandarización de eventos en el `dataLayer` para Google Analytics 4 (GA4), Meta Pixel y Google Ads:

### Inicialización de dataLayer
```html
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
</script>
```

### Eventos Clave de Conversión

```javascript
// 1. Evento de Inicio de Sesión / Registro
window.dataLayer.push({
    event: 'login',
    user_id: 'usr_10293',
    method: 'local_credentials'
});

// 2. Evento de Reproducción de Lección (Video Progress)
window.dataLayer.push({
    event: 'video_progress',
    course_name: 'Google Ads Alan Valdez',
    module_name: 'Módulo 1 - Fundamentos',
    lesson_name: '01. Introducción al Algoritmo',
    video_percent: 50
});

// 3. Evento de Lección Completada (Milestone)
window.dataLayer.push({
    event: 'lesson_complete',
    course_name: 'Google Ads Alan Valdez',
    lesson_name: '01. Introducción al Algoritmo',
    total_course_progress: 25.5
});

// 4. Evento de Descarga de Recurso
window.dataLayer.push({
    event: 'file_download',
    file_name: 'Plantilla_Calculo_ROAS.xlsx',
    file_extension: 'xlsx'
});
```

---

## 🚀 4. Conversion Rate Optimization (CRO) Best Practices

1. **CTA Primario Visible Above-the-Fold:** El botón de acción principal debe ser evidente sin necesidad de hacer scroll en el 100% de las resoluciones.
2. **Prueba Social (Social Proof) Dinámica:** Badges de alumnos activos, testimonios con foto real y valoraciones en estrellas.
3. **Reducción de Fricción en Formularios:**
   - Reducir inputs al mínimo indispensable (solo Nombre y Email en el registro inicial).
   - Permitir acceso rápido de 1 clic mediante perfiles guardados o botones OAuth (Google Sign-In).
4. **Micro-Copys de Confianza:** Textos de apoyo bajo los CTAs ("Acceso instantáneo", "Garantía de satisfacción", "Sin spam").
