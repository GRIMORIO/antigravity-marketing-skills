#!/usr/bin/env python3
"""
CPC & ROAS Calculator - Herramienta de Métricas de Google Ads (Metodología Alan Valdez)
Calcula métricas clave para la planificación y optimización de campañas:
- CPA Máximo Permitido / Breakeven CPA
- Breakeven ROAS (ROAS de equilibrio según margen)
- CPC Máximo sugerido según Tasa de Conversión
- Presupuesto Diario Mínimo Recomendado para significancia estadística
"""

import sys
import argparse

def calculate_metrics(ticket_medio, margen_pct, tasa_conv_pct, conv_diarias_deseadas=2):
    margen_decimal = margen_pct / 100.0
    tasa_conv_decimal = tasa_conv_pct / 100.0

    # Beneficio bruto por venta/cliente
    beneficio_bruto = ticket_medio * margen_decimal

    # CPA de equilibrio (Breakeven CPA): Todo el margen se va en adquirir al cliente (ganancia $0)
    breakeven_cpa = beneficio_bruto

    # ROAS de equilibrio (Breakeven ROAS)
    breakeven_roas = (1.0 / margen_decimal) * 100 if margen_decimal > 0 else 0.0

    # CPA Objetivo para ganar un 50% de margen neto
    cpa_objetivo_50 = beneficio_bruto * 0.50

    # CPC Máximo Recomendado según tasa de conversión y CPA objetivo
    cpc_max_breakeven = breakeven_cpa * tasa_conv_decimal
    cpc_max_objetivo = cpa_objetivo_50 * tasa_conv_decimal

    # Presupuesto diario mínimo sugerido
    presupuesto_diario_min = breakeven_cpa * conv_diarias_deseadas
    presupuesto_mensual_min = presupuesto_diario_min * 30.4

    return {
        "ticket_medio": ticket_medio,
        "margen_pct": margen_pct,
        "beneficio_bruto": beneficio_bruto,
        "tasa_conv_pct": tasa_conv_pct,
        "breakeven_cpa": breakeven_cpa,
        "breakeven_roas": breakeven_roas,
        "cpa_objetivo_50": cpa_objetivo_50,
        "cpc_max_breakeven": cpc_max_breakeven,
        "cpc_max_objetivo": cpc_max_objetivo,
        "presupuesto_diario_min": presupuesto_diario_min,
        "presupuesto_mensual_min": presupuesto_mensual_min
    }

def print_report(res):
    print("="*65)
    print("       REPORTE DE VIABILIDAD Y MÉTRICAS GOOGLE ADS")
    print("                  (Método Alan Valdez)")
    print("="*65)
    print(f"• Valor Promedio / Ticket Medio (LTV):  ${res['ticket_medio']:,.2f}")
    print(f"• Margen de Beneficio Bruto:            {res['margen_pct']:.1f}% (${res['beneficio_bruto']:,.2f})")
    print(f"• Tasa de Conversión Estimada (Web):    {res['tasa_conv_pct']:.2f}%")
    print("-"*65)
    print("📊 MÉTRICAS DE EQUILIBRIO (BREAKEVEN):")
    print(f"  - CPA de Equilibrio (Máximo Permisible): ${res['breakeven_cpa']:,.2f}")
    print(f"  - ROAS de Equilibrio (Mínimo requerido): {res['breakeven_roas']:.1f}% ({res['breakeven_roas']/100:.2f}x)")
    print(f"  - CPC Máximo Permitido (a Breakeven):    ${res['cpc_max_breakeven']:,.2f}")
    print("-"*65)
    print("🎯 MÉTRICAS OBJETIVO RECOMENDADAS (50% Margen de Beneficio Neto):")
    print(f"  - CPA Objetivo Sugerido (tCPA):          ${res['cpa_objetivo_50']:,.2f}")
    print(f"  - CPC Máximo Recomendado en Subasta:     ${res['cpc_max_objetivo']:,.2f}")
    print("-"*65)
    print("💰 RECOMENDACIÓN DE PRESUPUESTO INICIAL:")
    print(f"  - Presupuesto Diario Sugerido (2 conv/día): ${res['presupuesto_diario_min']:,.2f} / día")
    print(f"  - Presupuesto Mensual Recomendado:          ${res['presupuesto_mensual_min']:,.2f} / mes")
    print("="*65)

def main():
    parser = argparse.ArgumentParser(description="Calculadora de CPA, ROAS y Presupuesto para Google Ads")
    parser.add_argument("-t", "--ticket", type=float, help="Ticket medio o valor de vida del cliente (USD/EUR/MXN)")
    parser.add_argument("-m", "--margen", type=float, default=100.0, help="Margen de beneficio bruto en porcentaje (por defecto 100%% para servicios)")
    parser.add_argument("-c", "--conversion", type=float, default=3.0, help="Tasa de conversión esperada en la landing page %% (por defecto 3.0%%)")
    parser.add_argument("-d", "--conversiones-diarias", type=float, default=2.0, help="Meta de conversiones deseadas por día (por defecto 2)")

    args = parser.parse_args()

    ticket = args.ticket
    margen = args.margen
    conv = args.conversion

    if ticket is None:
        try:
            print("--- Calculadora de Métricas Google Ads ---")
            ticket_in = input("Ingresa el Ticket Medio / Valor de un cliente ($): ")
            ticket = float(ticket_in.strip())
            margen_in = input("Ingresa tu Margen de Beneficio Bruto % [Default 100% para servicios]: ")
            if margen_in.strip():
                margen = float(margen_in.strip())
            conv_in = input("Ingresa la Tasa de Conversión estimada de tu web % [Default 3%]: ")
            if conv_in.strip():
                conv = float(conv_in.strip())
        except (ValueError, EOFError):
            print("\nValores inválidos o cancelado.")
            return

    res = calculate_metrics(ticket, margen, conv, args.conversiones_diarias)
    print_report(res)

if __name__ == "__main__":
    main()
