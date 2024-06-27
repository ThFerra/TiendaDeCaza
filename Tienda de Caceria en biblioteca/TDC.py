# main.py
import libreria as lb
OpUser=0
Nom=""
Con=0
ConCon=0
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
        while Op2!=4:
            print("Ha seleccionado 'Compra de artículos', a continuación están los siguientes artículos:")
            print("""-------COMPRA DE ARTICULOS-------
                1.- Armas (arcos, pistolas, rifles, etc...) .
                2.- Munición (de las armas ya mencionadas) .
                3.- Trampas.
                4.-Salir
                ---------------------------------""")
            Op2=int(input(">> "))
            if Op2==1:
                while Op3!=4:
                    print("Usted ha seleccionado Armas, a continuación están las armas disponibles:")
                    print("""-------COMPRA DE ARMAS-------
                            1.- Arcos $100.000.
                            2.- Pistolas $750.000.
                            3.- Rifles $1.049.000.
                            4.- Salir
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
                while Op3!=4:
                    print("Usted ha seleccionado Munición, a continuación están las armas disponibles:")
                    print("""--------MUNICION--------
                            1.- Munición de Arcos [x1] $5.500.
                            2.- Munición de Pistolas [x20] $12.000.
                            3.- Munición de Rifles [x20] $20.000.
                            4.- Salir
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
                while Op3!=3:
                    print("Usted a seleccionado Trampas, a continuacion estan las Trampas disponibles:")
                    print("""--------TRAMPAS--------
                            1.- Trampa animales aereos [No letal] $7.850.
                            2.- Trampa animales terrestres [No letal] $9.990.
                            3.- Salir
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
    if Op1==2:
        while Op2!=3:
            print("Ha seleccionado 'Inventario', a continuación seleccione que desea hacer:")
            print("""-------INVENTARIO-------
                1.- Ver Inventario
                2.- Añadir Inventario
                3.- Salir
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
    if Op1==3:
        while Op2!=3:
            print("Ha seleccionado 'Áreas de caza (cercana o lejana)', a continuación seleccione que desea hacer:")
            print("""-------Áreas de caza-------
                Aqui se le presentaran multiples zonas de caceria dependiendo de que si tiene un medio de transporte propio para llegar alli o no. Ademas de los animales de la zona.end=
                1.- Sin Vehiculo (Solo zonas cercanas.)
                2.- Con Vehiculo (Zonas cercanas y lejanas)
                3.- Salir""")
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
            if Op2==2:
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