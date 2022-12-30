""""
Descripción:
Ejercicio 1.
Perimetro y Area del Rectangulo
Dadas dos longitudes ingresadas por el usuario que corresponden a los lados de un rectángulo,
calcular el perímetro y el área del mismo.
Autor:
Erick Sebastian Mora Lara
"""

def ingresarLados():
    """
    Es un procedimiento que solicita el ingreso de los lados por teclado,
    se combina con la funcion validarNumeros(), para validar unicamente
    el ingreso de datos numericos
    ------------
        No Recibe parametros de entrada
    
    Retorna:
    ------------
        Retorna una lista que contiene los dos lados ingresados (lado1, lado2)
    """
    ladosLista = [] #Definir lista vacia para almacenar el largo y ancho del rectangulo
    print("Vamos a Calcular el Perimetro y Area de un Rectangulo: ")
    print("Necesitas conocer la dimension del Largo y Ancho")
    #Mensaje de Inicio
    #Ciclo For que itera dos veces para solicitar el Ingreso de dos datos por teclado
    for i in range(2):
        print("Ingrese el lado ",i+1,": ")
        lados= validarNumeros() #El ingreso se fusiona con la validacion de numeros reales mayores a 0
        ladosLista.append(lados) #Se almacenan ambos lados en una lista y se retorna dicha lista para el calculo en las funciones
    return ladosLista

def validarNumeros():
    """
    Es un procedimiento generico alternativo para realizar validacion de numeros se lee un tipo de
    dato ingresado y se intenta su conversion a flotante (float), si es numero se transforman y pasa a la
    validacion para verificar que el numero sea mayor que 0.
    Si la conversion falla, se emplea el uso de Excepciones para imprimir un mensaje de Error
    ------------
        No Recibe parametros de entrada
    
    Retorna:
    ------------
        Retorna un valor entero (numero) que es el dato ingresado transformado a (int)
    """
    while True:
        num = input()
        try:
            num = float(num)
            if num >0:
                return num
            else:
                print("Solo numeros mayores a 0")    
        except ValueError:
            print("Solo se aceptan Reales")     

def perimetroRectangulo(lado1, lado2):
    """
    Es un procedimiento que recibe como datos dos lados de un rectangulo
    y con ellos calcula su perimetro haciendo la suma de sus dos lados multiplicados por 2
    ------------
        Recibe como parametros dos lados de un rectangulo, validados para que sean solo de tipo numerico
    
    Retorna:
    ------------
        Retorna el valor del perimetro obtenido mediante la operacion de suma
    """
    perimetroRec = lado1*2+lado2*2
    print("El perimetro del Rectangulo Ingresado es: ",perimetroRec)

def areaRectangulo(lado1, lado2):
    """
    Es un procedimiento que recibe como datos dos lados de un rectangulo
    y con ellos calcula su area haciendo la multiplicacion de ambos
    ------------
        Recibe como parametros dos lados de un rectangulo, validados para que sean solo de tipo numerico
    
    Retorna:
    ------------
        Retorna el valor del area obtenido mediante la operacion
    """
    areaRec = lado1*lado2
    print("El Area del Rectangulo Ingresado es: ",areaRec)

if __name__ == '__main__':
    """
    Funcion Main, aqui se declararan las variables principales y se llamara a las funciones necesarias para 
    ejecutar el programa

    """
    ancho, largo = ingresarLados() #Se declaran dos variables correspondientes a los lados 
    #Con ambas variables ingresadas y validadas se llama a las funciones de Perimetro y Area
    perimetroRectangulo(ancho, largo)
    areaRectangulo(ancho, largo)