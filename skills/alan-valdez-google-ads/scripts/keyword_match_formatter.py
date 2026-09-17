#!/usr/bin/env python3
"""
Keyword Match Formatter - Herramienta de Soporte Metodología Alan Valdez
Convierte listas de términos en formatos de concordancia para Google Ads:
- Exacta: [keyword]
- Frase: "keyword"
- Negativa: -keyword o -"keyword"
- Amplia: keyword
"""

import sys
import argparse

def clean_term(term: str) -> str:
    # Quitar corchetes, comillas y espacios extra
    return term.strip(" \t\n\r[]\"'-+")

def format_keywords(raw_keywords, match_types):
    results = {}
    cleaned_list = [clean_term(k) for k in raw_keywords if clean_term(k)]
    
    # Deduplicar preservando orden
    seen = set()
    unique_keywords = []
    for k in cleaned_list:
        lower_k = k.lower()
        if lower_k not in seen:
            seen.add(lower_k)
            unique_keywords.append(k)

    if 'exact' in match_types or 'all' in match_types:
        results['exact'] = [f"[{k}]" for k in unique_keywords]
    if 'phrase' in match_types or 'all' in match_types:
        results['phrase'] = [f'"{k}"' for k in unique_keywords]
    if 'broad' in match_types or 'all' in match_types:
        results['broad'] = [k for k in unique_keywords]
    if 'negative' in match_types or 'all' in match_types:
        results['negative'] = [f'-"{k}"' if " " in k else f"-{k}" for k in unique_keywords]

    return results

def main():
    parser = argparse.ArgumentParser(description="Formatea palabras clave para Google Ads (Metodología Alan Valdez)")
    parser.add_argument("keywords", nargs="*", help="Palabras clave separadas por espacio o ingresadas en línea de comandos")
    parser.add_argument("-t", "--type", choices=["all", "exact", "phrase", "broad", "negative"], default="all", help="Tipo de concordancia a generar")
    parser.add_argument("-f", "--file", help="Ruta a un archivo de texto con palabras clave (una por línea)")

    args = parser.parse_args()

    input_keywords = []
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                input_keywords = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        except Exception as e:
            print(f"Error al leer archivo: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.keywords:
        input_keywords = args.keywords
    else:
        # Modo interactivo / stdin
        print("Ingresa tus palabras clave (una por línea o separadas por comas). Presiona Ctrl+D (EOF) para finalizar:")
        try:
            for line in sys.stdin:
                parts = line.replace(",", "\n").split("\n")
                for p in parts:
                    if p.strip():
                        input_keywords.append(p.strip())
        except KeyboardInterrupt:
            pass

    if not input_keywords:
        print("No se proporcionaron palabras clave.")
        return

    formatted = format_keywords(input_keywords, [args.type])

    print("\n" + "="*50)
    print("RESULTADO DE PALABRAS CLAVE FORMATEADAS")
    print("="*50)

    for mtype, kw_list in formatted.items():
        type_names = {
            'exact': 'CONCORDANCIA EXACTA [ ]',
            'phrase': 'CONCORDANCIA DE FRASE " "',
            'broad': 'CONCORDANCIA AMPLIA',
            'negative': 'PALABRAS CLAVE NEGATIVAS'
        }
        print(f"\n--- {type_names.get(mtype, mtype.upper())} ({len(kw_list)} términos) ---")
        for kw in kw_list:
            print(kw)

if __name__ == "__main__":
    main()
