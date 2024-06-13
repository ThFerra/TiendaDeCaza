#TDC1.13 re-update

Usuarios=["jo216749340","th212147895"]
Contraseñas=["contragen1","papasfritask"]
ContraseñaCon=["contragen1","papasfritask"]
Inventario=[]
OpUser=0
OpUser2=0
Nom=0
Con=0
ConCon=0
print("Hola bienvenidos a 'Tienda de caza generica'.")
print("inicie sesión para entrar (si no es asi registrese)")
print()
print("""--------CACERÍA GENERICA--------
1.-Registrarse.
2.-Iniciar sesión.
--------------------------------""")
OpUser=int(input(">> "))
while OpUser!=3:
    if OpUser==1:
        print("Usted ha seleccionado registrarse en el programa de la 'tienda de cacería generica'.")
        print()
        print("Para registrarse, el nombre de usuario debe ser las primeras 2 letras del nombre y  el rut de este sin puntos o guiones, ej:")
        print("'th212147895'.")
        Nom=input(">> ")
        Usuarios.append(Nom)
        len(Nom)
        if len(Nom)==11:
            print("Ahora que ha elegido el nombre, ingrese la contraseña a usar.")
            print("La contraseña puede tener letras, numeros y signos, pero debe serde un minimo de 8 caracteres y un maximo de 12")
            Con=input(">> ")
            Contraseñas.append(Con)
            len(Con)
            if len(Con)>7 and len(Con)<13:
                while ConCon!=Con: 
                    print("Confirme su contraseña nuevamente:")
                    ConCon=input(">> ")
                    ContraseñaCon.append(ConCon)
                    if len(ConCon)!=len(Con):
                        print("ERROR: Las contraseñas no coinciden")
                        ContraseñaCon.pop()
                        ConCon=input(">> ")
                        ContraseñaCon.append(ConCon)
                    else:
                        print("Bien, todo está correcto, ahora inicie sesión para entrar al programa.")
                        print("Redireccionando a 'Iniciar sesión'...")
                        OpUser=2

            else:
                print("Tu contraseña no está en el rango establecido. intente nuevamente.")
                Contraseñas.pop()
                Con=input(">> ")
                Contraseñas.append(Con)
        else:
            print("Tu nombre de usuario no sigue con las indicaciones.")
            Usuarios.pop()
            Nom=input(">> ")
            Usuarios.append(Nom)
    elif OpUser==2:
        LogIn=0
        while LogIn!=1:
            print("Usted ha seleccionado iniciar sesion en el programa de la 'tienda de cacería generica'.")
            print()
            print("Para confirmar su identidad, ingrese su nombre de usuario")
            Nom=input(">> ")
            if Nom in Usuarios:
                print(f"Para confirmar su identidad como '{Nom}', ingrese la contraseña de la cuenta.")
                Con=input(">> ")
                if Con in Contraseñas:
                    LogIn=1
                    OpUser=3
                else:
                    print("Contraseña incorrecta, si no tiene una registrese.")
                    print("Redireccionando a 'Registrarse'...")
                    LogIn=1
                    OpUser=1
            else: 
                print("Nombre de usuario no encontrado, si no tiene cuenta de usuario registrese.")
                print("Redireccionando a 'Registrarse'...")
                LogIn=1
                OpUser=1
#Entrega 13/06/2024 (Primera opcion en proceso)
import libreria as lb
print(f"Bienvenido usuario {Nom} a la 'tienda de cacería generica'")
print("Seleccione que accion desea hacer:")
print(""" ----------MENU----------
1.- Compra de artículos.
2.- Inventario.
3.- Areas de caza (cercana o lejana).
4.- Salir.
------------------------""")
Op1=int(input(">> "))
if Op1==1:  
    print("A seleccionado 'Compra de artículos', a continuacion estan los siguientes articulos:")
    print("""
1.- Armas (arcos, pistolas, rifles, etc...) 
2.- Munición (De las armas ya mencionadas) 
3.- Trampas)""")
    Op2=int(input(">> "))
    if Op2==1:
        print("Usted a seleccionado Armas, a continuacion estan las armas disponibles:")
        print("""
1.-Arcos $100.000
2.-Pistolas $750.000
3.-Rifles $1.049.000""")
        Op3=int(input(">> "))
        if Op3==1:
            print("Usted a comprado un Arco de $100.000")
            print("Gracias por su compra.")
        elif Op3==2:
            print("Usted a comprado una Pistola $750.000")
            print("Gracias por su compra.")
        elif Op3==2:
            print("Usted a comprado una Rifle $1.049.000")
            print("Gracias por su compra.")
    elif Op1==2:
        print("Usted a seleccionado Municion, a continuacion estan las armas disponibles")
        print("""
1.-Municion de Arcos [x1] $5.500
2.-Municion de Pistolas [x20] $12.000
3.-Municion de Rifles [x20] $20.000""")
        Op3=int(input(">> "))
        if Op3==1:
            print("A selecionado 'Municion de Arcos [x1]', ingrese la cantidad de municion que desea comprar:")
            CanMunArcos=int(input(">> "))
            lb.Calculos
            print("Usted a selecionado un cantidad de ",CanMunArcos," Municion, con un total de $",lb.TCMA)
        if Op3==2:
            print("A selecionado 'Municion de Arcos [x1]', ingrese la cantidad de municion que desea comprar:")
            CanMunPistolas=int(input(">> "))
            print("Usted a selecionado un cantidad de ",CanMunPistolas," Municion, con un total de $",lb.TCMP)
        if Op3==3:
            print("A selecionado 'Municion de Arcos [x1]', ingrese la cantidad de municion que desea comprar:")
            CanMunRifles=int(input(">> "))
            print("Usted a selecionado un cantidad de ",CanMunRifles," Municion, con un total de $",lb.TCMR)
