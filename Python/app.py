from flask import Flask, render_template, request # se importa flask 

app = Flask(__name__) # se crea una instancia de la clase Flask

@app.route('/', methods=['GET', 'POST']) # se define la ruta de la aplicación
def index(): # se define la función principal
    resultado = None # variable para almacenar el resultado
    filas = 0 # variable para almacenar el número de filas
    columnas = 0 # variable para almacenar el número de columnas

    if request.method == 'POST': # se envia el formulario
        filas = int(request.form['filas']) # se obtiene el número de filas
        columnas = int(request.form['columnas']) # se obtiene el número de columnas

        matriz1 = [] # variable para almacenar la matriz 1
        matriz2 = [] # variable para almacenar la matriz 2

        for i in range(filas): # se recorren las filas
            fila = [int(x) for x in request.form.getlist(f'matriz1_{i}')] # se obtienen los valores de la matriz 1
            matriz1.append(fila) # se agrega la fila a la matriz 1

        for i in range(filas): # se recorren las filas
            fila = [int(x) for x in request.form.getlist(f'matriz2_{i}')] # se obtienen los valores de la matriz 2
            matriz2.append(fila) # se agrega la fila a la matriz 2

        # Sumar las matrices
        resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)] # se suman las matrices

    return render_template('index.html', resultado=resultado, filas=filas, columnas=columnas) # se renderiza la página

if __name__ == '__main__': # se ejecuta el archivo principal
    app.run(debug=True) # se inicia el servidor
