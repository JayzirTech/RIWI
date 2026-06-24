#Validación De Reglas 
'''
La tarea #8 según la distribución funcional sugerida es la "Validación de reglas de negocio". Esta es una de las partes más críticas del código, ya que actúa como el "cerebro" que decide si una operación es lícita o no, antes de que el saldo sea modificado.

Aquí te detallo qué podrías implementar específicamente para cumplir con los criterios de aceptación del documento:

1. Control de Montos Negativos
El sistema prohíbe estrictamente operaciones con valores menores a cero.

Tu función debe: Recibir el monto ingresado por el usuario y verificar que sea mayor a 0.

Mensaje de error: Si el usuario intenta depositar o retirar −50, debes lanzar una alerta tipo: "Monto inválido. El valor debe ser positivo".

2. Validación de Saldo Disponible
No se pueden realizar retiros que superen el saldo actual en la cuenta.

Tu función debe: Comparar el monto_a_retirar contra el saldo_actual.

Lógica: Si monto_a_retirar > saldo_actual, la operación debe ser rechazada.


Contexto: Recuerda que el sistema inicia con un saldo fijo de $1000.
'''

def permiso(valor_deposito=0, valor_retiro=0, valor_cuenta=0):                          
    conf = False

    if(valor_retiro<=0 or valor_deposito<=0):                                     #El valor a retirar debe ser positivo
        print("Por favor, digite un cantidad mayor de 0")

    elif(valor_cuenta<valor_retiro):                                              #Regla de fondos insuficientes
        print("Fondos insuficientes")
        
    elif(valor_cuenta-valor_retiro<5):                                            #Regla de monto minimo en la cuenta
        print("Fondos insuficientes. Por favor, digite una cantidad mayor de retiro")

    else: conf = True


    return conf
