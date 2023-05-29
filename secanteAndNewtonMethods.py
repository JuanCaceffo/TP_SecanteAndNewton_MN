import math as m
def f(x):
    return m.sin(m.sqrt(((m.e**x)+3))/2)
def f1(x):
    return (m.e*m.cos(m.sqrt(((m.e**x)+3))/2))/(4*m.sqrt(((m.e**x)+3)))
def printSteps(x1,x,pasos):
    print (f"paso : {pasos} -------- [x1,x] = {round(abs(x1-x),3)} -------- raizActual = {round(x1,3)} -------- f(raizActual) = {round(f(x1),3)}")

#x = valor inicial
#tolerancia = valor del intervalo como temrino de parada de convergencia
def newton(x,tolerancia):
    pasos = 0
    #anidamos funcion para poder utilizar variables no locales
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
        if (abs(x-x1) <= tolerancia):
            break
        x = secante()
        pasos += 1 
        printSteps(x,x1,pasos)
    return (x1)
    
def dataEntry():
    x = float(input("ingrese un numero cercano a la raiz buscada: "))
    # Pedir al usuario la cantidad de decimales correctos
    #rango de exactitud de decimales posible
    RANGO_TOLERABLE = range(1,11)
    exactitud = int(input(f"ingrese la cantidad de decimales correctos que desea, (deben estar dentro del rango ({RANGO_TOLERABLE.start}..{RANGO_TOLERABLE.stop-1}): "))
    #verificar que la exactitud ingresada por el usuario este detro del rango
    while (not(exactitud in RANGO_TOLERABLE)):    
        exactitud = int(input(f"ingrese la cantidad de decimales correctos que desea, (deben estar dentro del rango ({RANGO_TOLERABLE.start}..{RANGO_TOLERABLE.stop-1}): "))
    #scamos el valor de paradad dada la exactitud
    tolerancia = "0."
    #agregamos tantos 0 como exactitud indicada
    for i in range(exactitud): tolerancia += "0"
    #agregamos un uno para indicar que es una fraccion
    tolerancia += "1"
    #convertimos a flotante para poder operar
    tolerancia = float(tolerancia)

    return (x,tolerancia,exactitud)

def main():
    (x,epsilon,exactitud) = dataEntry()
    raiz = newton(x,epsilon)
    print(f"raiz aproximada con una exactitud de {exactitud} decimales = {round(raiz,exactitud)}")

main()  