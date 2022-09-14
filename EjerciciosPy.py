import sys
from datetime import date, datetime #The datetime module supplies classes for manipulating dates and times.
from msilib.schema import tables


def receive_integer_as_input():
    """Función auxiliar que verifica que la entrada del usuario sea un 
    número entero y lo regresa""" 
    try:
        x = int(input("Ingresa un número entero: "))
        return x
    except:
        print("La entrada no es un núumero entero.") 

def receive_number_as_input():
    """Función auxiliar que verifica que la entrada del usuario sea un 
    número real y lo regresa""" 
    try:
        x = float(input("Ingresa un número: "))
        return x
    except:
        print("La entrada recibida no es un número.")
        
def receive_multiple_numbers():
    """Función auxliar que verifica que la entrada proporcionada por el
    usuario sea una lista de números y la regresa"""
    try:
        numbers = list(map(int or float, input("Ingresa una lista de números: ").split()))
        return numbers
    except:
        print("La lista de argumentos no corresponde con una lista de números.")
        
def receive_multiple_integers():
    """Función auxliar que verifica que la entrada proporcionada por el
    usuario sea una lista de números enteros y la regresa
    """
    try:
        entrada = input("Ingresa una lista de números enteros: ")
        lista_entrada = entrada.split(",")
        lista_entrada_a_numeros = map(int, lista_entrada)
        #numbers = list(map(int, input("Ingresa una lista de números enteros: ").split(",")))
        return list(lista_entrada_a_numeros)
    except:
        print("La lista de argumentos no corresponde con una lista de números enteros.")

def ejercicio01():
    '''1. Hacer un programa que evalúe y diga si un numero ingresado por el usuario es par o impar'''
    num = input("Proporciona un número entero ")
    try: 
        num2 = int(num)
        if (num2 % 2 == 0):
            print("El numero",num,"es par")
        else:
            print("El numero", num, "es impar")
    except ValueError:
        print("No ingresasté un entero")

def ejercicio02():
    '''Hacer un programa que dado un entero no negativo, diga  si ese entero corresponde a la clase  de altura de do , do#, re , etc'''
    nota = input("Teclea un numero que corresponda a la nota ")
    try: 
        num = int(nota)
        if (num >= 0 and num <= 128 ):
            num= num%12
            if(num == 0):
                nota = "do"
            if(num == 1):
                nota = "do#"
            if(num == 2):
                nota = "re"
            if(num == 3):
                nota = "re#"
            if(num == 4):
                nota = "mi"
            if(num == 5):
                nota = "fa"
            if(num == 6):
                nota = "fa#"
            if(num == 7):
                nota = "sol"
            if(num == 8):
                nota = "sol#"
            if(num == 9):
                nota = "la"
            if(num == 10):
                nota = "la#"
            if(num == 11):
                nota = "si"
            print("El numero corresponde a la tecla",num)
        else:
            print("ingresa un numero")

    except ValueError:
        print("No ingresasté un entero")

    print(nota)

def ejercicio03():
    """3. Dados dos enteros, dar su producto y si este producto es mayor que 1000, dar la suma de los dos números."""
    try: 
        num1 = int(input("Proporciona un número entero "))
        num2 = int(input("Proporciona otro número entero "))
        producto = num1 * num2
        print("El producto de",num1,"y", num2,"es:",producto)
        if(producto > 1000):
            suma = num1 +num2
            print("Y la suma de ",num1,"y",num2, "es: ",suma)
    except ValueError:
        print("No ingresasté un entero")
 

def ejercicio04():
    """ 4. Dados dos números (posiblemente decimales), regresar el mayor de ellos. Repetir el ejercicio, ahora con tres números."""
    try: 
        num1 = float(input("Proporciona un número entero "))
        num2 = float(input("Proporciona otro número entero "))
    
        if(num1 == num2):
            print("Los dos numeros son iguales, por lo que no hay mayor")
            sys.exit() #para terminar la ejecucion del programa 
        if(num1 > num2):
            print("El número mayor es",num1)
        else:
            print("El nnúmero mayor es",num2)
    except ValueError:
        print("No ingresasté un numero")
    try: 
        num1 = float(input("Proporciona un primer número entero "))
        num2 = float(input("Proporciona un dos segundo número entero: "))
        num3 = float(input("Proporciona un dos tercer número entero: "))
    
        if(num1 > num2 and num1 > num3):
            print("El número mayor es: ",num1)
        elif(num2 > num1 and num2 > num3):
            print("El número mayor es",num2)
        elif(num3 > num1 and num3 > num2):
            print("El número mayor es: ",num3)
        else:
            print("No hay numero mayor")
    except ValueError:
        print("No ingresasté un numero")
   



def ejercicio05():
    '''5. Hacer un programa que pida un número entre 1 y 99. Si el número está fuera de este rango, mostrar el mensaje “Número fuera de rango”.'''
    try:
        num = int(input("Proporciona un número entre el 1 y 99 "))
        if((num < 0) or (num >= 100) ):
            print("Número fuera de rango")

    except ValueError: 
        print("No ingresasté un numero")

def ejercicio06():
    '''6. Hacer un programa que pida una contraseña y muestre los mensajes “Contraseña correcta” o “Contraseña incorrecta”, según sea el caso. '''

    contrasenia = input("Teclea tu contraseña\n ")
    contrasenia2 = input("Teclea nuevamente la contraseña\n ")
    if(contrasenia == contrasenia2):
        print("Contraseña correcta ")
    else:
        print("Contraseña incorrecta ")

def ejercicio07():

    fecha_de_nacimiento = input("Escribe tu fecha de nacimiento en este formato 'Dia-mes-año': ")
    nombre = input("Ingresa tu nombre :")
    apellido_paterno = input("Ingresa tu apellido paterno :")
    apellido_materno = input("Ingresa tu apellido materno: ")
    '''Pedir a un usuario su fecha de nacimiento y su nombre, apellido paterno y apellido materno. Después
    regresar la siguiente información, en este orden: apellido paterno, apellido materno, nombre, edad y si
    es niño, adulto o anciano.
    '''
    fecha = fecha_de_nacimiento.split('-')
    day,month,year = int(fecha[0]),int(fecha[1]),int(fecha[2])

    today = date.today()
    #print(today)
    birth = date(year,month,day)
    age = (today-birth).days/365
    #print(age)
    age = int(age)
    print(age)
    if(age < 18):
        longevidad = "niño"
    elif(age >= 18 and age<60):
        longevidad = "adulto"
    else:
        longevidad = "anciano"
    #age = int((today))
    print(f"Tu apellido paterno es: {apellido_paterno} \nTu apellido materno: {apellido_materno} \nTu nombre es: {nombre}\nTienes {age} años y eres",longevidad)
    
    
def ejercicio08():
    '''8. Hacer un programa que pida al usuario la temperatura, aclarando si se trata de oC (grados Celsius)
    ó oF (grados Fahrenheit). Después, convertir el dato ingresado a la otra escala térmica, y mostrar el
    resultado, aclarando si son ºC ó ºF.'''
    print("Bienvenido al convertido de temperatura\n¿Qué deseas hacer?\n[1]Convertir de Celsius a Fahrenheit\n[2]Convertir de Fahrenheit a Celsius")
    opcion = int(input("Teclea 1 o 2 segun lo que desees hacer: "))
    if(opcion == 1):
        print("Muy bien, convertiremos de Celsius a Fahrenheit 🤓")
        temperatura = int(input("Teclea la temperatura en Celsius(Un valor numerico): "))
        temperatura_convertida = temperatura*1.8 + 32
        print(temperatura,"ºC, es equivalente a: ",round(temperatura_convertida,2),"ºF")
    
    elif(opcion == 2):
        print("Muy bien, convertiremos de Fahrenheit a Celsius")
        temperatura = int(input("Teclea la temperatura en Fahrenheit(Un valor numerico): "))
        temperatura_convertida = (temperatura-32)/1.8
        print(temperatura,"ºF, es equivalente a:",round(temperatura_convertida,2),"ºC ")


def ejercicio9():
    """Considerando los números 0, 1, ... , 9, mostrar la suma de cada uno con el anterior"""
    print('número + número anterior= suma')
    for i in range(1,10):
        suma = i + i-1
        print(i, "+", i-1, "=", suma)
        
def ejercicio10():
    """Dada una lista de números, regresar un valor booleano (verdadero o falso) que indique si el primernúmero y el último son iguales."""
    numeros = receive_multiple_integers()
    if (numeros[0] == numeros[-1]):
        return True
    else:
        return False


def ejercicio11():
    '''11. Dada una lista de enteros, mostrar sólo los números divisibles por 5. Repetir el ejercicio, ahora para un
    número k dado por el usuario.'''
    lista= receive_multiple_integers()
    for i in lista:
        if(i%5 == 0):
            print(i)
    print("Los numeros anteriores son divisibles por 5")
    divisor = int(input("Ahora establece el divisor para obtener los numeros divisibles por ese número: "))
    lista= receive_multiple_integers()
    for i in lista:
        if(i%divisor == 0):
            print(i)


def ejercicio12():
    '''Pedir al usuario una cadena y mostrar el número de veces que una palabra dada por el usuario aparece
    en dicha cadena. '''
    cadena = input("Ingresa una cadena: ")
    palabra = input("Ingresa la palabra que se contara cuantas veces esta contenida en la cadena: ")
    lista = cadena.split(" ")

    count = 0
    for i in range(0, len(lista)):
        if(palabra == lista[i]):
            count = count + 1

    print("El número de veces que se repite",palabra,"en la cadena, son",count,"veces")

def ejercicio13():
    '''Imprime un patron
    '''

    for i in range(1,6):
        for k in range(1,i+1):
            print("* ",end="")
        print()

    tamaño_piramide = int(input("Teclea un número del 0-10 :"))
    if(tamaño_piramide >= 11 or tamaño_piramide <= 0):
        print("Introdujisté un número fuera de rango")
        sys.exit()
        
    
    tamaño_piramide = tamaño_piramide + 1
    for i in range(1,tamaño_piramide):
        for k in range(1,i+1):
            print("* ",end="")
        print()
    
def ejercicio14():
    ''' Dadas dos listas de enteros, crear una nueva lista que contenga sólo los números impares de la primera
    lista y los números pares de la segunda.'''
    l1 = receive_multiple_integers()
    l2 = receive_multiple_integers()
    l3 = [n for n in l1 if n%2]+[n for n in l2 if not n%2]
    print(l3)

def ejercicio15():
    '''Imprimir la tabla de multiplicar de un número dado.'''
    factor =int(input("Teclea un número del cual deseeas saber su tabla de multiplicación: "))
    for f in range(1, 11):
	    print(f'{factor} x {f} =  {factor * f}')

def ejercicio16():
    '''Imprimir las tablas de multiplicar del 1 al 10.'''
    for factor in range(1,11):
        for f in range(1,11):
	        print(f'{factor} x {f} =  {factor * f}')
        print()

def main(): 
    
    #ejercicio01
    #ejercicio02()
    #ejercicio03()
    #ejercicio04()
    #ejercicio05()
    #ejercicio06()
    ejercicio07()
    #ejercicio08()
    #ejercicio9()
    #print(ejercicio10())
    #ejercicio11()
    #ejercicio12()
    #ejercicio13()
    #ejercicio14()
    #ejercicio15()
    #ejercicio16()
            
if __name__ == "__main__":
    main()