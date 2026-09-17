#!/usr/bin/env python3
"""
Meta Scaling Calculator - Herramienta de Escalado Seguro (Metodología Felipe Vergara)
Calcula el plan de escalado vertical seguro (+15% a +20% cada 48h) y la distribución de presupuesto
entre etapas de embudo (TOFU, MOFU, BOFU).
"""

import sys
import argparse

def calculate_scaling_plan(presupuesto_inicial, tasa_incremento_pct=20.0, dias_entre_aumentos=2, ciclos=6):
    plan = []
    presupuesto_actual = presupuesto_inicial
    tasa_decimal = 1.0 + (tasa_incremento_pct / 100.0)

    for c in range(1, ciclos + 1):
        dia_inicio = (c - 1) * dias_entre_aumentos + 1
        dia_fin = c * dias_entre_aumentos
        gasto_ciclo = presupuesto_actual * dias_entre_aumentos
        plan.append({
            "ciclo": c,
            "dias": f"Días {dia_inicio:02d}-{dia_fin:02d}",
            "presupuesto_diario": presupuesto_actual,
            "gasto_ciclo": gasto_ciclo
        })
        presupuesto_actual *= tasa_decimal

    return plan

def calculate_funnel_distribution(presupuesto_total):
    return {
        "tofu_presupuesto": presupuesto_total * 0.75,
        "tofu_pct": 75,
        "mofu_presupuesto": presupuesto_total * 0.15,
        "mofu_pct": 15,
        "bofu_presupuesto": presupuesto_total * 0.10,
        "bofu_pct": 10
    }

def print_scaling_report(presupuesto_inicial, plan, funnel):
    print("="*70)
    print("      PLAN DE ESCALADO VERTICAL SEGURO Y DISTRIBUCIÓN DE EMBUDO")
    print("                   (Metodología Felipe Vergara)")
    print("="*70)
    print(f"• Presupuesto Diario Base Inicial: ${presupuesto_inicial:,.2f} / día")
    print(f"• Tasa de Incremento Seguro:       +20% cada 48 horas (sin romper aprendizaje)")
    print("-"*70)
    print("📈 PROYECCIÓN DE ESCALADO DÍA A DÍA:")
    for paso in plan:
        print(f"  [{paso['ciclo']}] {paso['dias']}: Presupuesto Diario: ${paso['presupuesto_diario']:,.2f}/día  (Inversión en 48h: ${paso['gasto_ciclo']:,.2f})")
    
    ultimo_presupuesto = plan[-1]['presupuesto_diario']
    crecimiento = ((ultimo_presupuesto - presupuesto_inicial) / presupuesto_inicial) * 100
    print(f"\n  👉 Crecimiento total en {len(plan)*2} días: +{crecimiento:.1f}% de capacidad de inversión.")
    print("-"*70)
    print("🎯 DISTRIBUCIÓN RECOMENDADA DE EMBUDO (FULL-FUNNEL):")
    print(f"  • TOFU (Prospección en Frío - {funnel['tofu_pct']}%):  ${funnel['tofu_presupuesto']:,.2f} / día")
    print(f"  • MOFU (Nutrición / Interacción - {funnel['mofu_pct']}%): ${funnel['mofu_presupuesto']:,.2f} / día")
    print(f"  • BOFU (Remarketing Caliente - {funnel['bofu_pct']}%):  ${funnel['bofu_presupuesto']:,.2f} / día")
    print("="*70)

def main():
    parser = argparse.ArgumentParser(description="Calculador de Escalado Vertical para Meta Ads")
    parser.add_argument("-p", "--presupuesto", type=float, help="Presupuesto diario base inicial (USD/EUR/MXN)")
    parser.add_argument("-i", "--incremento", type=float, default=20.0, help="Porcentaje de incremento por ciclo (Default: 20%%)")
    parser.add_argument("-c", "--ciclos", type=int, default=6, help="Número de ciclos de 48h a proyectar (Default: 6 ciclos = 12 días)")

    args = parser.parse_args()

    presupuesto = args.presupuesto
    if presupuesto is None:
        try:
            print("--- Calculador de Escalado Meta Ads ---")
            p_in = input("Ingresa tu presupuesto diario actual para el anuncio/campaña ganadora ($): ")
            presupuesto = float(p_in.strip())
        except (ValueError, EOFError):
            print("Presupuesto inválido.")
            return

    plan = calculate_scaling_plan(presupuesto, args.incremento, 2, args.ciclos)
    funnel = calculate_funnel_distribution(presupuesto)
    print_scaling_report(presupuesto, plan, funnel)

if __name__ == "__main__":
    main()
