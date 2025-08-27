# Diagrama de flujo del juego "Adivina el Número"

┌────────────────────┐
│ Inicio del juego │
└───────┬────────────┘
│
▼
┌───────────────────────────┐
│ Definir rango 1 a 100 │
└──────────┬────────────────┘
│
▼
┌───────────────────────────┐
│ intento = mitad del rango │
└──────────┬────────────────┘
│
▼
┌───────────────────────────┐
│ Usuario responde: │
│ mayor / menor / igual │
└──────────┬────────────────┘
│
┌──────────▼───────────┐
│ ¿Respuesta = igual? │──Sí──▶ Fin (número hallado)
└───────┬──────────────┘
│No
▼
┌───────────────────────────┐
│ Si mayor → rango inferior │
│ Si menor → rango superior │
└──────────┬────────────────┘
│
▼
(Repetir proceso)
