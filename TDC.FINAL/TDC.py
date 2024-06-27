# main.py
import libreria as lb
OpUser=0
Nom=""
Con=0
ConCon=0
BusAdmin=0
print("Hola bienvenidos a 'Tienda de caza generica'.")
print("Inicie sesión para entrar (si no es así regístrese).")
print()
print("""--------CACERÍA GENERICA--------
1.- Registrarse.
2.- Iniciar sesión.
--------------------------------""")
OpUser=int(input(">> "))
while OpUser!=3:
    if OpUser==1:
        OpUser=lb.registrar_usuario()
    elif OpUser==2:
        OpUser,Nom=lb.iniciar_sesion()
print(f"Bienvenido usuario {Nom} a la 'tienda de cacería generica'.")
print("Seleccione que acción desea hacer:")
print(""" ----------MENU----------
1.- Compra de artículos.
2.- Inventario.
3.- Áreas de caza (cercana o lejana).
4.- Salir.
------------------------""")
Op1=int(input(">> "))
while Op1!=4:
    if Op1==1:  
        print("Ha seleccionado 'Compra de artículos', a continuación están los siguientes artículos:")
        print("""-------COMPRA DE ARTICULOS-------
1.- Armas (arcos, pistolas, rifles, etc...) .
2.- Munición (de las armas ya mencionadas) .
3.- Trampas.
---------------------------------""")
        Op2=int(input(">> "))
        if Op2==1:
            print("Usted ha seleccionado Armas, a continuación están las armas disponibles:")
            print("""-------COMPRA DE ARMAS-------
1.- Arcos $100.000.
2.- Pistolas $750.000.
3.- Rifles $1.049.000.
------------------------------""")
            Op3=int(input(">> "))
            if Op3==1:
                print("Usted ha comprado un Arco de $100.000.")
                print("Gracias por su compra.")
            elif Op3==2:
                print("Usted ha comprado una Pistola $750.000.")
                print("Gracias por su compra.")
            elif Op3==3:
                print("Usted ha comprado un Rifle $1.049.000.")
                print("Gracias por su compra.")
        elif Op2==2:
            print("Usted ha seleccionado Munición, a continuación están las armas disponibles:")
            print("""--------MUNICION--------
1.- Munición de Arcos [x1] $5.500.
2.- Munición de Pistolas [x20] $12.000.
3.- Munición de Rifles [x20] $20.000.
------------------------""")
            Op3=int(input(">> "))
            if Op3==1:
                print("Ha seleccionado 'Munición de Arcos [x1]', ingrese la cantidad de munición que desea comprar:")
                CanMunArcos=int(input(">> "))
                print(f"Usted ha seleccionado una cantidad de {CanMunArcos} Munición, con un total de ${lb.Cal_Ar(CanMunArcos)}.")
            elif Op3==2:
                print("Ha seleccionado 'Munición de Pistolas [x20]', ingrese la cantidad de munición que desea comprar:")
                CanMunPistolas=int(input(">> "))
                print(f"Usted ha seleccionado una cantidad de {CanMunPistolas} Munición, con un total de ${lb.Cal_Pi(CanMunPistolas)}.")
            elif Op3==3:
                print("Ha seleccionado 'Munición de Rifles [x20]', ingrese la cantidad de munición que desea comprar:")
                CanMunRifles=int(input(">> "))
                print(f"Usted ha seleccionado una cantidad de {CanMunRifles} Munición, con un total de ${lb.Cal_Ri(CanMunRifles)}.")

        elif Op2==3:
                print("Usted a seleccionado Trampas, a continuacion estan las Trampas disponibles:")
                print("""--------TRAMPAS--------
1.-Trampa animales aereos [No letal] $7.850.
2.-Trampa animales terrestres [No letal] $9.990.
-----------------------""")
                Op3=int(input(">> "))
                if Op3==1:
                    print("A selecionado 'Trampa animales aereos [No letal]', ingrese la cantidad de trampas que desea comprar:")
                    CanTAA=int(input(">>"))
                    print(f"Usted ha comprado {CanTAA} de trampa/s de animales aereos, con un total de ${lb.Trampa_Ae(CanTAA)}.")
                    
                elif Op3==2:
                    print("A selecionado 'Trampa animales terrestres [No letal]', ingrese la cantidad de trampas que desea comprar:")
                    CanTAT=int(input(">>"))
                    print(f"Usted ha comprado {CanTAT} de trampa/s de animales terrestres, con un total de ${lb.Trampa_Te(CanTAT)}.")
    elif Op1==2:
        print("Ha seleccionado 'Inventario', a continuación seleccione que desea hacer:")
        print("""-------INVENTARIO-------
1.- Ver Inventario
2.- Añadir Inventario
-----------------------""")
        Op2=int(input(">> "))
        if Op2==1:
            print("Armas:")
            print("Arcos = ",{lb.InvArc})
            print("Rifles = ",{lb.InvRif})
            print("Pistolas = ",{lb.InvPis})
            print("Municiones:")
            print("Municion Arcos = ",{lb.InvMunArc})
            print("Municion Rifles = ",{lb.InvMunRif})
            print("Municion Pistolas = ",{lb.InvMunPis})
            print("Trampas:")
            print("Trampas animales Terrestres = ",{lb.InvTT})
            print("Trampas animales Aereos = ",{lb.InvTA})
        elif Op2==2:
            while lb.Intentos!=0:
                    print("Para acceder al inventario y añadir objeto a este, debe ingresar la contraseña de Administrador")
                    BusAdmin=input(">> ")
                    if BusAdmin in lb.Admin:
                        print("Se ha verificado correctamente la contraseña")
                        print("De que objeto desea añadir:")
                        print("1.- Arcos = ",{lb.InvArc})
                        print("2.- Rifles = ",{lb.InvRif})
                        print("3.- Pistolas = ",{lb.InvPis})
                        print("4.- Municion Arcos = ",{lb.InvMunArc})
                        print("5.- Municion Rifles = ",{lb.InvMunRif})
                        print("6.- Municion Pistolas = ",{lb.InvMunPis})
                        print("7.- Trampas animales Terrestres = ",{lb.InvTT})
                        print("8.- Trampas animales Aereos = ",{lb.InvTA})
                        CanInv=int(input(">> "))
                        if CanInv==1:
                            print("Cuanto desea añadir a los Arcos?")
                            CanInvAña=int(input(">> "))
                            lb.InvArc=lb.InvArc+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Arcos: ",lb.InvArc)
                        elif CanInv==2:
                            print("Cuanto desea añadir a los Rifles?")
                            CanInvAña=int(input(">> "))
                            lb.InvRif=lb.InvRif+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Rifles: ",lb.InvRif)
                        elif CanInv==3:
                            print("Cuanto desea añadir a los Pistolas?")
                            CanInvAña=int(input(">> "))
                            lb.InvPis=lb.InvPis+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Pistolas: ",lb.InvPis)
                        elif CanInv==4:
                            print("Cuanto desea añadir a los municion Arcos?")
                            CanInvAña=int(input(">> "))
                            lb.InvMunArc=lb.InvMunArc+CanInvAña                                
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Municion Arcos: ",lb.InvMunArc)
                        elif CanInv==5:
                            print("Cuanto desea añadir a las Municiones Rifles?")
                            CanInvAña=int(input(">> "))
                            lb.InvMunRif=lb.InvMunRif+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Municion Rifles: ",lb.InvMunRif)
                        elif CanInv==6:
                            print("Cuanto desea añadir a los municion Pistolas?")
                            CanInvAña=int(input(">> "))
                            lb.InvMunPis=lb.InvMunPis+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Municion Pistolas: ",lb.InvMunPis)
                        elif CanInv==7:
                            print("Cuanto desea añadir a los Trampa Terrestre?")
                            CanInvAña=int(input(">> "))
                            lb.InvTT=lb.InvTT+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Trampas Terrestres: ",lb.InvTT)
                        elif CanInv==8:
                            print("Cuanto desea añadir a las Trampas Aereas?")
                            CanInvAña=int(input(">> "))
                            lb.InvTA=lb.InvTA+CanInvAña
                            print("Se a añadido correctamente, esta es la cantidad actual.")
                            print("Trampas Aereas: ",lb.InvTA)
                    else:
                        print("No se ha podido ingrar correctamente, regresando a menu...")
                        lb.Intentos=0
    elif Op1==3:
        print("Ha seleccionado 'Áreas de caza (cercana o lejana)', a continuación seleccione que desea hacer:")
        print("""-------Áreas de caza-------
                Aqui se le presentaran multiples zonas de caceria dependiendo de que si tiene un medio de transporte propio para llegar alli o no. Ademas de los animales de la zona.end=
                1.- Sin Vehiculo (Solo zonas cercanas.)
                2.- Con Vehiculo (Zonas cercanas y lejanas)""")
        Op2=int(input(">> "))
        if Op2==1:
            print("A seleccionado *Sin Vehiculo*")
            print("Zonas disponibles: Zona Centro - Zona norte")
            print("")
            print("En la Zona Centro se presentan los siguientes animales:")
            print(lb.ZonaC)
            print("")
            print("En la Zona Norte se presentan los siguientes animales:")
            print(lb.ZonaN)
            print("")
        elif Op2==2:
            print("A seleccionado *Con Vehiculo*")
            print("Zonas disponibles: Zona Centro - Zona Norte - Zona Sur - Zona Austral")
            print("")
            print("En la Zona Centro se presentan los siguientes animales:")
            print(lb.ZonaC)
            print("")
            print("En la Zona Norte se presentan los siguientes animales:")
            print(lb.ZonaN)
            print("")
            print("En la Zona Sur se presentan los siguientes animales:")
            print(lb.ZonaS)
            print("")
            print("En la Zona Austral se presentan los siguientes animales:")
            print(lb.ZonaAus)                
            print("")