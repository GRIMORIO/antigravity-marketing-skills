# Sistemas de Layout, Responsividad y Ergonomía

## 1. Regla de Espaciado Fluido con `clamp()`
Evita anchos rígidos en píxeles. Usa funciones fluidas de CSS:
```css
/* Barra lateral adaptable */
--sidebar-width: clamp(380px, 26vw, 460px);

/* Tipografía de títulos */
font-size: clamp(1.1rem, 2vw + 0.5rem, 1.6rem);
```

## 2. Drawer Móvil con Backdrop Blur
En pantallas `< 992px`, la barra lateral debe convertirse en un drawer deslizante suave:
```css
@media (max-width: 992px) {
    .sidebar {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: min(390px, 90vw);
        transform: translateX(-100%);
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        z-index: 850;
    }
    .sidebar.open {
        transform: translateX(0);
        box-shadow: 20px 0 60px rgba(0, 0, 0, 0.85);
    }
}
```

## 3. Scrollbar Estética Invisible/Discreta
```css
.scroll-container::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
.scroll-container::-webkit-scrollbar-track {
    background: transparent;
}
.scroll-container::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.12);
    border-radius: 9999px;
}
.scroll-container::-webkit-scrollbar-thumb:hover {
    background: rgba(168, 85, 247, 0.4);
}
```
