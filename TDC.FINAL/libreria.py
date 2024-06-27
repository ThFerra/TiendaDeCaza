# libreria.py
Usuarios=["jo216749340", "th212147895"]
Contraseñas=["contragen1", "papasfritask"]
ContraseñaCon=["contragen1", "papasfritask"]
def registrar_usuario():
    print("Usted ha seleccionado registrarse en el programa de la 'tienda de cacería generica'.")
    print()
    print("Para registrarse, el nombre de usuario debe ser las primeras 2 letras del nombre y el rut de este sin puntos o guiones, ej:")
    print("'th212147895'.")
    Nom=input(">> ")
    Usuarios.append(Nom)
    if len(Nom)==11:
        print("Ahora que ha elegido el nombre, ingrese la contraseña a usar.")
        print("La contraseña puede tener letras, números y signos, pero debe ser de un mínimo de 8 caracteres y un máximo de 12.")
        Con=input(">> ")
        Contraseñas.append(Con)
        if 7<len(Con)<13:
            ConCon=""
            while ConCon!=Con: 
                print("Confirme su contraseña nuevamente:")
                ConCon=input(">> ")
                if ConCon!=Con:
                    print("ERROR: Las contraseñas no coinciden")
                else:
                    ContraseñaCon.append(ConCon)
                    print("Bien, todo está correcto, ahora inicie sesión para entrar al programa.")
                    print("Redireccionando a 'Iniciar sesión'...")
                    return 2
        else:
            print("Tu contraseña no está en el rango establecido. Intente nuevamente.")
            Contraseñas.pop()
            return 1
    else:
        print("Tu nombre de usuario no sigue con las indicaciones.")
        Usuarios.pop()
        return 1

def iniciar_sesion():
    LogIn=0
    while LogIn!=1:
        print("Usted ha seleccionado iniciar sesión en el programa de la 'tienda de cacería generica'.")
        print()
        print("Para confirmar su identidad, ingrese su nombre de usuario")
        Nom=input(">> ")
        if Nom in Usuarios:
            print(f"Para confirmar su identidad como '{Nom}', ingrese la contraseña de la cuenta.")
            Con=input(">> ")
            if Con in Contraseñas:
                LogIn=1
                return 3,Nom
            else:
                print("Contraseña incorrecta, si no tiene una regístrese.")
                print("Redireccionando a 'Registrarse'...")
                return 1,None
        else: 
            print("Nombre de usuario no encontrado, si no tiene cuenta de usuario regístrese.")
            print("Redireccionando a 'Registrarse'...")
            return 1,None
        
def Cal_Ar(cantidad):
    return cantidad*5500
def Cal_Pi(cantidad):
    return cantidad*12000
def Cal_Ri(cantidad):
    return cantidad*20000

def Trampa_Ae(CanTAA):
    return CanTAA*7850
def Trampa_Te(CanTAT):
    return CanTAT*9990

#Inventario
#Contador para cada cosa, mensaje de error cuando compre mas de lo que hay, y entonces muestre lo disponible, inventario como lista que se divida entre las categorias de compra.
#Verificar que la cantidad a comprar no sea mayor a la cantidad del inventario
#Armas: Arcos, Rifles, Pistolas
#Mun: MunArcos, MunRifles, MunPistolas
#Trampas: Terrestres, Aereas
#ARMAS
InvArc=10
InvRif=10
InvPis=10
#MUN
InvMunArc=50
InvMunRif=10
InvMunPis=10
#TRAMPAS
InvTT=15
InvTA=15

Inventario=[InvArc,InvRif,InvPis,InvMunArc,InvMunRif,InvMunPis,InvTT,InvTA]
Admin=["contragen1", "papasfritask"]

Intentos=1
CanInv=0

ZonaN=["Yeco","Pato Juarjual","Codorniz","Tórtola cordillerana","Tórtola","Paloma de alas blancas","Diuca","Faisán"]
ZonaC=["Perdiz chilena","Yeco","Pato criollo","Pato real","Pato jergón grande","Pato jergón chico","Codorniz","Tórtola"]
ZonaS=["Perdiz chilena","Pato real","Pato jergón grande","Pato jergón chico","Pato colorado","Codorniz","Tagua","Zorzal"]
ZonaAus=["Yeco","Caiquén","Pato jergón grande","Pato jergón chico","Traro","Codorniz","Zorzal","Jilguero"]