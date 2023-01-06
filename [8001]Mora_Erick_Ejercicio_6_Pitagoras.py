"""
Descripción:
Ejercicio 6.
Calcular la hipotenusa de un triangulo rectangulo mediante la funcion de pitagoras 
h^2 = a^2 + b^2
Autor:
Erick Sebastian Mora Lara
"""

def validarNumeros():
    """
    Es un procedimiento generico alternativo para realizar validacion de numeros enteros
    los datos ingresados se leen como string (str) y si son numeros se verifican
    y se transforman en tipo de datos entero (int), en este variante de funcion
    se maneja el uso de una excepcion para el ingreso de datos que no son numericos:
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

def menuOpciones():
        print("Vamos a calcular un lado del triangulo usando la funcion de pitagoras")
        print("Necesitamos conocer al menos dos lados del triangulo:")
        print("1.- 2 Catetos")
        print("2.- Hipotenusa y Cateto")
        print("3.- Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        return opcion

def seleccionOpcion(opcion):
    while True:
        if opcion == "1":
            dosCatetos()
        elif opcion == "2":
            catetoHipotenusa()
        elif opcion == "3":
            salir()
        else:
            print("Opción inválida. Inténtelo de nuevo.")
            
def dosCatetos(): 
	print("Ingresa el valor del Cateto Uno")
	catetoUno = validarNumeros()
	print("Ingresa el valor del Cateto Dos")
	catetoDos = validarNumeros()
	
	resHipotenusa = (catetoUno**2 + catetoDos**2)**0.5
	
	print("El valor de la Hipotenusa es: ",resHipotenusa)
	
def catetoHipotenusa():
	hipotenusa = 0 
	catetoUno = 0
	while(catetoUno>=hipotenusa):
		print("Ingresa el Valor de la Hipotenusa: ")
		hipotenusa = validarNumeros() 
		print("Ingresa el Valor de un Cateto: ")
		catetoUno = validarNumeros()
		if(catetoUno>= hipotenusa):
				print("Los catetos no pueden ser mas grandes que la hipotenusa, Ingresa otro valor")
		catetoDos = (hipotenusa**2 - catetoUno**2)**0.5
        
			
	print("El valor del cateto restante es: ",catetoDos)

def salir():
    print("Saliendo")
    exit()
		
if __name__ == '__main__':
    nuevoMenu = menuOpciones()
    seleccionOpcion(nuevoMenu)