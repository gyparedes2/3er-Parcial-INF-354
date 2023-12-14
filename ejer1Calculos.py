import csv

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

    # Calcular la cantidad en porcentaje de vinos blancos y rojos
    white_count = wine_types.count("white")
    red_count = wine_types.count("red")
    white_percentage = (white_count / len(wine_types)) * 100
    red_percentage = (red_count / len(wine_types)) * 100

    # Imprimir la cantidad en porcentaje de vinos blancos y rojos
    print(f"Porcentaje de vinos blancos: {white_percentage:.2f}%")
    print(f"Porcentaje de vinos rojos: {red_percentage:.2f}%")

    # Convertir la columna "type" en una lista numérica
    type_numeric = [0 if t == 'white' else 1 for t in wine_types]

    # Imprimir resultados para otras columnas numéricas
    columnas = [type_numeric, fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                density, pH, sulphates, alcohol, quality]
    nombres_columnas = ['Tipo', 'Acidez fija', 'Acidez volátil', 'Ácido cítrico',
                        'Azúcar residual', 'Cloruros', 'Dióxido de azufre libre',
                        'Dióxido de azufre total', 'Densidad', 'pH', 'Sulfatos',
                        'Alcohol', 'Calidad']

    for i in range(len(columnas)):
        columna = columnas[i]
        nombre = nombres_columnas[i]
        media = sum(columna) / len(columna)
        moda = max(set(columna), key=columna.count)
        cuartiles = [sorted(columna)[int(len(columna) * q)] for q in [0.25, 0.5, 0.75]]
        percentiles = [sorted(columna)[int(len(columna) * p)] for p in [0.1, 0.25, 0.5, 0.75, 0.9]]

        # Imprimir los resultados
        print(f'{nombre.capitalize()}:')
        print(f'  Media: {media:.2f}')
        print(f'  Moda: {moda}')
        print(f'  Cuartiles: {cuartiles}')
        print(f'  Percentiles: {percentiles}')
