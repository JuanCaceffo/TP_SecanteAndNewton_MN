import math
import numpy

def f(x):
    return x**4
def f1(x):
    return 4*x**3
def impresionDePasos(x1,x,pasos):
    print (f"paso : {pasos} -------- [x1,x] = {round(abs(x1-x),3)} -------- raizActual = {round(x1,3)} -------- f(raizActual) = {round(f(x1),3)}")

def newton(x,epsilon):
    pasos = 0
    #anidamos funcion par apoder utilizar variables no locales
    def secante():
        try:
            return x1 - ((f(x1)*(x1-x))/(f(x1)-f(x)))
        except ZeroDivisionError:
            print(f"error: f({x}) = 0, no se puede dividir por 0")
            exit(6)
    #------------------------- fin secante ----------------------------------    
    while(True):    
        try:
            x1 = x - (f(x)/f1(x))
        except ZeroDivisionError:
            print(f"error: f'({x}) = 0, no se puede dividir por 0")
            exit(6)
        if (abs(x-x1) <= epsilon):
            break
        x = secante()
        pasos += 1 
        impresionDePasos(x,x1,pasos)
    return (x1)
    
def dataEntry():
    x = float(input("ingrese un numero cercano a la raiz buscada"))
    while (True):
        epsilon = float(input("ingrese un intervalo de error aceptado"))  
        if(epsilon > 0):
            break
        else:
            print("ingrese un epsilon positivo")    
    return (x,epsilon)

def main():
    (x,epsilon) = dataEntry()
    raiz = newton(x,epsilon)
    print(f"raiz aproximada con error menor a epsilon = {raiz}")

main()  