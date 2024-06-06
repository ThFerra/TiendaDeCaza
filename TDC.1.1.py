Usuarios=["ju216749340","th212147895"]
Contraseñas=["contragen1",""]#aqui pon tu contraseña
ContraseñaCon=[]
Inventario=[]
OpUser=0
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
if OpUser==1:
    print("Usted ha seleccionado registrarse en el programa de la 'tienda de cacería generica'.")
    print()
    print("Para registrarse, el nombre de usuario debe ser las primeras 2 letras del nombre y  el rut de este sin puntos o guiones, ej:")
    print("'th212147895'.")
    Nom=(input(">> "))
    Usuarios.append(Nom)
    len(Nom)
    if len(Nom)==11:
        print("Ahora que ha elegido el nombre, ingrese la contraseña a usar.")
        print("La contraseña puede tener letras, numeros y signos, pero debe serde un minimo de 8 caracteres y un maximo de 12")
        Con=(input(">> "))
        Contraseñas.append(Con)
        len(Con)
        if len(Con)>7 and len(Con)<13:
            while ConCon!=Con: 
                print("Confirme su contraseña nuevamente:")
                ConCon=input(">> ")
                ContraseñaCon.append(ConCon)
                if ConCon!=Con:
                    print("Reintente ingresar la contraseña")
                    ContraseñaCon.pop()
                    ConCon=input(">> ")
                else:
                    print("")
        else:
            print("Tu contraseña no está en el rango establecido. intente nuevamente.")
            Contraseñas.pop()
            Con=input(">> ")
    else:
        print("Tu nombre de usuario no sigue con las indicaciones.")
