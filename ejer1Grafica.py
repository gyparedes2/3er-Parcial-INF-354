import csv
import matplotlib.pyplot as plt

# Abre el archivo CSV
with open('wine-quality-white-and-red.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)  # Saltar la fila de encabezado

    # Inicializa listas vacías para cada columna
    wine_types = []
    fixed_acidity = []
    volatile_acidity = []
    citric_acid = []
    residual_sugar = []
    chlorides = []
    free_sulfur_dioxide = []
    total_sulfur_dioxide = []
    density = []
    pH = []
    sulphates = []
    alcohol = []
    quality = []  # Agrega una lista para la calidad

    # Leer cada fila y agregar los valores a la lista correspondiente
    for row in reader:
        wine_types.append(row[0])
        fixed_acidity.append(float(row[1]))
        volatile_acidity.append(float(row[2]))
        citric_acid.append(float(row[3]))
        residual_sugar.append(float(row[4]))
        chlorides.append(float(row[5]))
        free_sulfur_dioxide.append(float(row[6]))
        total_sulfur_dioxide.append(float(row[7]))
        density.append(float(row[8]))
        pH.append(float(row[9]))
        sulphates.append(float(row[10]))
        alcohol.append(float(row[11]))
        quality.append(float(row[12]))  # Agrega la puntuación de calidad

    fig, axes = plt.subplots(
        nrows=4, ncols=3, figsize=(15, 10))  # Cambia nrows a 4
    fig.subplots_adjust(hspace=0.5)
    columnas = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                density, pH, sulphates, alcohol, quality]  # Agrega la calidad a la lista de columnas

    nombres_columnas = ['Acidez fija', 'Acidez volátil', 'Ácido cítrico',
                        'Azúcar residual', 'Cloruros', 'Dióxido de azufre libre',
                        'Dióxido de azufre total', 'Densidad', 'pH', 'Sulfatos',
                        'Alcohol', 'Calidad']  # Agrega "Calidad" a los nombres de columnas

    for i in range(len(columnas)):
        columna = columnas[i]
        nombre = nombres_columnas[i]

        if nombre == 'Calidad':  # Si la columna es la de calidad
                # Crear un gráfico de barras para mostrar la puntuación promedio de calidad para "white" y "red"
            ax = axes[i // 3, i % 3]
            promedio_white = sum([quality[j] for j in range(
                len(quality)) if wine_types[j] == "white"]) / wine_types.count("white")
            promedio_red = sum([quality[j] for j in range(
                len(quality)) if wine_types[j] == "red"]) / wine_types.count("red")
            ax.bar(["Blanco", "Rojo"], [promedio_white,
                    promedio_red], color=["blue", "red"])
            ax.set_title("Calidad Promedio")
            ax.set_ylabel('Calificación Promedio')
        else:
            # Filtrar los valores de la columna para "white" y "red"
            valores_white = [columna[j] for j in range(
                len(columna)) if wine_types[j] == "white"]
            valores_red = [columna[j] for j in range(
                len(columna)) if wine_types[j] == "red"]

            # Calcular promedio para "white" y "red"
            promedio_white = sum(valores_white) / len(valores_white)
            promedio_red = sum(valores_red) / len(valores_red)

            # Crear histogramas para "white" y "red" en subgráficos separados
            ax = axes[i // 3, i % 3]
            ax.hist(valores_white, alpha=0.5,
                    label="Blanco", color="blue", bins=15)
            ax.hist(valores_red, alpha=0.5,
                    label="Rojo", color="red", bins=15)
            ax.axvline(promedio_white, color='blue', linestyle='dashed', linewidth=2, label='Promedio Blanco')
            ax.axvline(promedio_red, color='red', linestyle='dashed', linewidth=2, label='Promedio Rojo')
            ax.set_title(nombre.capitalize())
            ax.set_xlabel(nombre)
            ax.set_ylabel('Frecuencia')
            ax.legend()

    plt.tight_layout()
    plt.show()
