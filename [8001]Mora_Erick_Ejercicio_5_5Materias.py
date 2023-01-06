"""
Descripción:
Ejercicio 5.
Ingresar las calificaciones de 5 materias, y calcular el total, el promedio y porcentaje 
Autor:
Erick Sebastian Mora 
"""

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
            if num >=0 and num<21:
                return num
            else:
                print("Las notas deben ser entre 0 y 20")    
        except ValueError:
            print("Solo se aceptan Reales")  
            
def ingresarMaterias():
	listaMaterias = []
	for i in range(5):
		print("Ingrese el nombre de la Materia ",i+1,": ")
		materias = input()
		listaMaterias.append(materias)
	return listaMaterias

def ingresarCalificaciones():
	listaMaterias = ingresarMaterias()
	listaCalificaciones = []
	for materia in listaMaterias:
		print("Ingrese la calificacion de ",materia,": ")
		nota = validarNumeros()
		listaCalificaciones.append(nota)
	return listaCalificaciones

def totalCalificaciones():
	totalNotas = 0
	promedioNotas = 0
	porcentNotas = 0
	listaCalificaciones = ingresarCalificaciones()
	for notas in listaCalificaciones:
		totalNotas = totalNotas + notas
	print("La Sumatoria de las Notas Ingresadas es: ",totalNotas)
	promedioNotas=totalNotas/5
	print("El Promedio de las Notas es: ",promedioNotas)
	porcentNotas = (promedioNotas*100)/20
	print("El porcentaje de las notas es del: ",porcentNotas,"%")


if __name__ == '__main__':
	totalCalificaciones()

 		
 		
 