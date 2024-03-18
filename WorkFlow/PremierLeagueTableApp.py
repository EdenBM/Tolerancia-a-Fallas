from prefect import Flow, task
import httpx
from colorama import Fore, Style  # Importa colorama para colores de consola
from tabulate import tabulate  # Importa tabulate para imprimir la tabla

@task
def descargar_datos(url):
    # Descarga los datos de la API
    headers = {
        'X-RapidAPI-Key': "1f624a3292msh62ce9a89a5ac94cp1780b5jsned12b0cff64a",
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

@task
def limpiar_datos(datos):
    # Procesa y limpia los datos obtenidos
    standings = datos["response"][0]["league"]["standings"][0]
    cleaned_data = []
    for team_info in standings:
        team_name = team_info["team"]["name"]
        points = team_info["points"]
        goals_diff = team_info["goalsDiff"]
        form = team_info["form"]
        cleaned_data.append({"Pos": len(cleaned_data) + 1, "Team": team_name, "Points": points, "Dif": goals_diff, "Form": form})
    return cleaned_data

@task
def analizar_datos(datos):
    # Imprime la tabla de clasificación con colores
    table = tabulate(datos, headers="keys", tablefmt="fancy_grid", showindex=False)
    table_with_colors = apply_color_to_table(table)
    print(Fore.BLUE + "Premier League Standings:" + Style.RESET_ALL)
    print(table_with_colors)

def apply_color_to_table(table):
    # Aplica colores a diferentes partes de la tabla
    table_lines = table.split("\n")
    for idx, line in enumerate(table_lines):
        if idx == 0:
            # Encabezado de la tabla
            table_lines[idx] = Fore.YELLOW + line + Style.RESET_ALL
        else:
            # Celdas de datos
            if idx % 2 == 0:
                table_lines[idx] = Fore.WHITE + line + Style.RESET_ALL
            else:
                table_lines[idx] = Fore.CYAN + line + Style.RESET_ALL
    return "\n".join(table_lines)

@Flow
def flujo():
    # Define el flujo de trabajo Prefect
    datos_descargados = descargar_datos(url="https://api-football-v1.p.rapidapi.com/v3/standings?season=2023&league=39")
    datos_limpios = limpiar_datos(datos=datos_descargados)
    analizar_datos(datos=datos_limpios)

if __name__ == "__main__":
    # Ejecuta el flujo de trabajo
    flujo._run()
