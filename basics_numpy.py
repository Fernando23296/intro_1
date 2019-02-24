#BASICS OF NUMPY
import numpy as np
#Crear una matriz llena de unos
#primer valor numero de filas, segundo valor numero de columnas

unos = np.ones((3,4))
print(unos)

#Crear una matriz de ceros
zeros = np.zeros((3,4))
print(zeros)

#Crear una matriz de numeros randomicos
randoms = np.random.random((3,4))
print(randoms)
#--------
print("_"*5)
#Crear una matriz vacia
vacia = np.empty((3,3))
print(vacia)
#Matriz con un solo valor en todo
todo = np.full((3,4),8)
print(todo)

#--------Matrices con valores espaciados------
'''Aca se desea que la matriz 
empiece en 0 y termine en 30, 
con pasos de cinco en cinco'''
espacio_1 = np.arange(0,30,5)
print(espacio_1)
'''Aca se desea que la matriz 
tenga cinco valores, que se encuentre
entre cero y dos'''
espacio_2 = np.linspace(0,2,5)
print(espacio_2)

#MATRIZ IDENTIDAD
identidad_1 = np.eye(4,4)
print(identidad_1)

identidad_2 = np.identity(4)
print(identidad_2)

#COMO INSPECCIONAR MATRICES
#Para encontrar dimensiones
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a.ndim)
