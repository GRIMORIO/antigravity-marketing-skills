# Micro-interacciones, Animaciones y Feedback

## 1. La Curva de Aceleración de Élite
Nunca uses `transition: all 0.3s ease;` para elementos interactivos clave. Usa curvas bezier tipo iOS/macOS:
```css
--ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
transition: transform 0.22s var(--ease-spring), background 0.2s ease, border-color 0.2s ease;
```

## 2. Micro-traslación en Hover
```css
.interactive-card:hover {
    transform: translateY(-2px); /* Para tarjetas en grid */
}

.list-item:hover {
    transform: translateX(4px);  /* Para elementos de listas verticales */
}
```

## 3. Estado Activo Iluminado (Active Glow)
```css
.list-item.active {
    background: linear-gradient(90deg, rgba(168, 85, 247, 0.18) 0%, rgba(99, 102, 241, 0.06) 100%);
    border: 1px solid rgba(168, 85, 247, 0.35);
    border-left: 3.5px solid #A855F7;
    box-shadow: 0 2px 12px rgba(168, 85, 247, 0.15);
}
```
