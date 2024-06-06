Usuarios=["ju216749340","th212147895"]
Contraseñas=["contragen1","papasfritask"]#aqui pon tu contraseña
ContraseñaCon=[]
Inventario=[]
OpUser=0
Nom=0
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
elif OpUser==2:
    print("Usted ha seleccionado iniciar sesion en el programa de la 'tienda de cacería generica'.")
    print()
    print("Para confirmar su identidad, ingrese su nombre de usuario")
    Nom=input(">> ")
        if Nom in Usuarios==True:
            print("Para confirmar su identidad como '",Nom,"' ingrese la contraseña de la cuenta.")
            Con=input(">> ")
            while Con in Contraseñas==False:
                print("La contraseña ingresado no es correcta, intente nuevamente.")
                Con=input(">> ")

            if Con in Contraseñas==True:
                    print("Bienvenido usuario '",Nom,"' espero que tenga un buen dia.")
        else: #Seria bueno si hubiera un while para volver a las opciones de usuario.
            print("Nombre de usuario no encontrado, si no tiene cuenta de usuario registrese.")
