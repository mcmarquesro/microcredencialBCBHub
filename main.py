#!/usr/bin/env python3

import sys
from rich.console import Console
console = Console()  # Objeto de rich para usar colores

def main():

    # Defino variables
    sam_path = sys.argv[1]

    total_read_counts = 0
    quality_read_counts = 0

    # Abro el fichero
    with open(sam_path, mode="r") as sam:
        print("Leyendo:", sam_path)

        # Extraigo líneas y me quedo con las que contienen lecturas
        for line in sam:

            if line.startswith("@"):
                continue

            total_read_counts += 1

            # Extraigo columnas y leo la columna 5 (MAPQ)
            column = line.strip().split("\t")
            values_MAPQ = int(column[4])

            if values_MAPQ == 60:
                quality_read_counts += 1

    # Calculo el porcentaje
    percentage_quality_counts = (quality_read_counts / total_read_counts) * 100

    # Output

    console.print()
    console.print("[bold red]RESUMEN: [/bold red]")
    console.print("─" * 40)
    console.print(f"[bold cyan]Total de lecturas alineadas: [/bold cyan][bold white]{total_read_counts}[/bold white]")
    console.print(f"[bold cyan]Lecturas con MAPQ = 60: [/bold cyan][bold white]{quality_read_counts}[/bold white]")
    console.print(f"[bold cyan]Porcentaje: [/bold cyan][bold white]{percentage_quality_counts:.1f}%[/bold white]")

main()




