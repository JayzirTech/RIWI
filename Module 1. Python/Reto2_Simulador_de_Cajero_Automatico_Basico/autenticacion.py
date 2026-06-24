from configuracion_inicial import Configuracion_Inicial


def Autenticacion():
    Saldo, UsuarioRegistrado, PinRegistrado, Fallas=Configuracion_Inicial()
    print("Por favor, indicanos tus credenciales")
    print("")
    FallasDeUsuario=0

    while FallasDeUsuario<Fallas:
        Usuario=input("Usuario: ")
        Pin=input("Pin: ")
        if(Usuario==UsuarioRegistrado and Pin==PinRegistrado):
            print("Correcto")
            break
        else:
            print("Incorrecto, intente de nuevo")
            FallasDeUsuario+=1
            print(FallasDeUsuario)
    print("Hecho")
