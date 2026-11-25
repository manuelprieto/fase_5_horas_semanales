# Fase 5 - Evaluación Final POA
# Problema 5: Horas trabajadas por semana y clasificación de la jornada laboral

UMBRAL_HORAS = 40  # Si el total semanal es mayor a 40 -> "Sobretiempo"


def calcular_total_y_clasificar(horas_diarias):
    """Recibe la lista de horas de lunes a viernes de un recurso.
    Retorna el total semanal y la clasificación de su jornada."""
    total = 0
    for horas in horas_diarias:  # estructura de repetición
        total = total + horas

    if total > UMBRAL_HORAS:  # estructura de control (decisión)
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"

    return total, clasificacion


def main():
    # Matriz: [Nombre del recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
    matriz = [
        ["Ana",    8, 9, 8, 10, 8],   # 43 -> Sobretiempo
        ["Carlos", 8, 8, 8, 8, 8],    # 40 -> Horario estándar
        ["Marta",  7, 8, 6, 8, 7],    # 36 -> Horario estándar
        ["Luis",   10, 9, 9, 8, 9],   # 45 -> Sobretiempo
    ]

    print("REPORTE DE HORAS SEMANALES")
    print("-" * 50)

    for fila in matriz:  # recorre cada recurso
        nombre = fila[0]
        horas = fila[1:]  # horas de lunes a viernes
        total, clasificacion = calcular_total_y_clasificar(horas)
        print(f"Recurso: {nombre} | Total horas: {total} | Jornada: {clasificacion}")


main()