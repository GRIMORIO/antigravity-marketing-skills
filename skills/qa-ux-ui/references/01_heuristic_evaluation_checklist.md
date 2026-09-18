# Checklist de Evaluación Heurística (10 Heurísticas de Nielsen)

## 1. Visibilidad del Estado del Sistema
- [ ] ¿El usuario sabe en todo momento qué lección, pestaña o sección está activa? (Indicador luminoso, borde de acento).
- [ ] ¿Hay indicadores de progreso visibles? (Barras de carga, contadores `(3/12 completadas)`).
- [ ] ¿Las operaciones asíncronas muestran spinners o esqueletos de carga?

## 2. Coincidencia entre el Sistema y el Mundo Real
- [ ] ¿Los iconos son universales e intuitivos? (Play ▶ para reproducir, Checkmark ✓ para completado, Documento 📄 para PDF).
- [ ] ¿El lenguaje utilizado es claro y en el idioma del usuario, sin jerga interna del sistema?

## 3. Control y Libertad del Usuario
- [ ] ¿El usuario puede cerrar fácilmente cajones/drawers laterales haciendo clic en el backdrop o con botón de cierre?
- [ ] ¿Puede retroceder o reiniciar lecciones con un solo clic?
- [ ] ¿Puede alternar entre velocidad de video o saltar 10s adelante/atrás?

## 4. Consistencia y Estándares
- [ ] ¿Los colores de estado se mantienen en toda la plataforma? (Verde = completado, Violeta = activo, Rojo = alerta/PDF).
- [ ] ¿Los módulos y lecciones comparten la misma estructura tipográfica y padding?

## 5. Prevención de Errores
- [ ] ¿Se previene la pérdida de progreso mediante guardado automático periódico en LocalStorage y Backend?
- [ ] ¿Los botones destructivos o irreversibles solicitan confirmación previa?

## 6. Reconocimiento antes que Recuerdo
- [ ] ¿El título del módulo se muestra claramente en cada sección sin obligar al usuario a memorizar el número?
- [ ] ¿Las opciones de navegación y atajos están visibles o accesibles con un icono de ayuda?

## 7. Flexibilidad y Eficiencia de Uso
- [ ] ¿Existen atajos de teclado para usuarios avanzados? ([Espacio] para pausar, [Flechas] para buscar).
- [ ] ¿Existe un buscador en tiempo real para saltar directamente a cualquier lección?

## 8. Diseño Estético y Minimalista
- [ ] ¿Se eliminó información redundante o innecesaria? (Evitar repetir etiquetas genéricas como "VIDEO" en cada fila).
- [ ] ¿Existe suficiente espacio en blanco ("breathing room") para evitar saturación visual?

## 9. Ayuda a los Usuarios a Reconocer, Diagnosticar y Recuperarse de Errores
- [ ] En caso de fallo de red o video, ¿se muestra un banner amigable con botón de "Reintentar Reproducción"?

## 10. Ayuda y Documentación
- [ ] ¿Se ofrece una tarjeta o sección de ayuda contextual con los atajos y recomendaciones de uso?
