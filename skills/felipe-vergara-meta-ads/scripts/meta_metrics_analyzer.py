#!/usr/bin/env python3
"""
Meta Metrics Analyzer - Diagnóstico del Semáforo de Decisiones (Metodología Felipe Vergara)
Analiza el rendimiento de un anuncio, conjunto de anuncios o campaña de Facebook/Instagram Ads
y emite un diagnóstico formal con estado del Semáforo (Rojo, Amarillo, Verde) y acciones recomendadas.
"""

import sys
import argparse

def analyze_traffic_light(gasto, conversiones, cpa_objetivo, clics_enlace=None, visitas_landing=None, ctr_enlace=None, frecuencia=None):
    cpa_actual = (gasto / conversiones) if conversiones > 0 else gasto
    drop_off_pct = None
    if clics_enlace and visitas_landing and clics_enlace > 0:
        drop_off_pct = ((clics_enlace - visitas_landing) / clics_enlace) * 100.0

    diagnosticos = []
    estado = "VERDE"
    color_emoji = "🟢"

    # 1. Regla crítica de Conversiones y CPA
    if conversiones == 0:
        if gasto >= (1.5 * cpa_objetivo):
            estado = "ROJO"
            color_emoji = "🔴"
            diagnosticos.append(f"Gasto excesivo (${gasto:,.2f}) sin conversiones superando 1.5x el CPA objetivo (${cpa_objetivo:,.2f}). ACCIÓN: Pausar de inmediato.")
        else:
            estado = "AMARILLO"
            color_emoji = "🟡"
            diagnosticos.append(f"Gasto en fase de prueba (${gasto:,.2f}) aún por debajo de 1.5x CPA objetivo. Dejar recopilar datos.")
    else:
        if cpa_actual > (1.3 * cpa_objetivo):
            estado = "ROJO"
            color_emoji = "🔴"
            diagnosticos.append(f"CPA actual (${cpa_actual:,.2f}) está más de un 30% por encima del objetivo (${cpa_objetivo:,.2f}). No rentable.")
        elif cpa_actual > cpa_objetivo:
            estado = "AMARILLO"
            color_emoji = "🟡"
            diagnosticos.append(f"CPA actual (${cpa_actual:,.2f}) ligeramente por encima del objetivo (${cpa_objetivo:,.2f}). Optimizar fricciones.")
        else:
            diagnosticos.append(f"CPA actual (${cpa_actual:,.2f}) es rentable y está por debajo del objetivo (${cpa_objetivo:,.2f}).")

    # 2. Diagnóstico de CTR en el enlace
    if ctr_enlace is not None:
        if ctr_enlace < 0.8:
            if estado != "ROJO":
                estado = "AMARILLO"
                color_emoji = "🟡"
            diagnosticos.append(f"CTR en el enlace bajo ({ctr_enlace:.2f}% < 0.8%). El creativo o gancho de 3s no detiene el scroll suficientemente.")
        elif ctr_enlace >= 1.5:
            diagnosticos.append(f"Excelente CTR en el enlace ({ctr_enlace:.2f}%). El creativo y el gancho funcionan muy bien.")

    # 3. Diagnóstico de Fuga Web (Drop-off Clics vs Visitas)
    if drop_off_pct is not None:
        if drop_off_pct > 25.0:
            if estado != "ROJO":
                estado = "AMARILLO"
                color_emoji = "🟡"
            diagnosticos.append(f"Fuga técnica en la web: Pérdida del {drop_off_pct:.1f}% entre clics ({clics_enlace}) y visitas ({visitas_landing}). La web tarda más de 3s en cargar o hay error técnico.")

    # 4. Diagnóstico de Frecuencia / Saturación
    if frecuencia is not None:
        if frecuencia > 3.5:
            if estado != "ROJO":
                estado = "AMARILLO"
                color_emoji = "🟡"
            diagnosticos.append(f"Frecuencia alta ({frecuencia:.2f}). Audiencia saturada. Riesgo de fatiga creativa.")

    # Conclusión de Escalamiento si es Verde
    if estado == "VERDE":
        diagnosticos.append("Cumple todos los criterios del Semáforo Verde: Iniciar escalado vertical (+20% presupuesto) o escalado horizontal.")

    return {
        "estado": estado,
        "color_emoji": color_emoji,
        "gasto": gasto,
        "conversiones": conversiones,
        "cpa_actual": cpa_actual,
        "cpa_objetivo": cpa_objetivo,
        "ctr_enlace": ctr_enlace,
        "drop_off_pct": drop_off_pct,
        "frecuencia": frecuencia,
        "diagnosticos": diagnosticos
    }

def print_analysis(res):
    print("="*70)
    print(f"      DIAGNÓSTICO DEL SEMÁFORO DE DECISIONES: {res['color_emoji']} SEMÁFORO {res['estado']}")
    print("                      (Método Felipe Vergara)")
    print("="*70)
    print(f"• Importe Gastado:     ${res['gasto']:,.2f}")
    print(f"• Conversiones:        {res['conversiones']}")
    if res['conversiones'] > 0:
        print(f"• CPA Actual:          ${res['cpa_actual']:,.2f}")
    else:
        print(f"• CPA Actual:          Sin conversiones")
    print(f"• CPA Objetivo:        ${res['cpa_objetivo']:,.2f}")
    if res['ctr_enlace'] is not None:
        print(f"• CTR en el Enlace:    {res['ctr_enlace']:.2f}%")
    if res['frecuencia'] is not None:
        print(f"• Frecuencia:          {res['frecuencia']:.2f}")
    if res['drop_off_pct'] is not None:
        print(f"• Pérdida Clics->Web:  {res['drop_off_pct']:.1f}%")
    print("-"*70)
    print("📋 CONCLUSIONES Y ACCIONES RECOMENDADAS:")
    for d in res['diagnosticos']:
        print(f"  👉 {d}")
    print("="*70)

def main():
    parser = argparse.ArgumentParser(description="Analizador de Métricas Meta Ads - Semáforo de Decisiones")
    parser.add_argument("-g", "--gasto", type=float, required=True, help="Importe total gastado ($)")
    parser.add_argument("-c", "--conversiones", type=int, default=0, help="Número de conversiones obtenidas")
    parser.add_argument("-t", "--cpa-objetivo", type=float, required=True, help="CPA máximo objetivo permitido ($)")
    parser.add_argument("--clics", type=int, help="Clics en el enlace (únicos)")
    parser.add_argument("--visitas", type=int, help="Visitas a la página de destino (Landing Page Views)")
    parser.add_argument("--ctr", type=float, help="CTR único en el enlace (%%)")
    parser.add_argument("--frecuencia", type=float, help="Frecuencia promedio de entrega")

    args = parser.parse_args()

    res = analyze_traffic_light(
        gasto=args.gasto,
        conversiones=args.conversiones,
        cpa_objetivo=args.cpa_objetivo,
        clics_enlace=args.clics,
        visitas_landing=args.visitas,
        ctr_enlace=args.ctr,
        frecuencia=args.frecuencia
    )
    print_analysis(res)

if __name__ == "__main__":
    main()
