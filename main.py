import funciones_externas as fun;
jugadores = {};

while True:
    print("***** MENU *****");
    print("1) Registrar Jugador");
    print("2) Buscar Jugador");
    print("3) Mostrar Estado Nutricional");
    print("4) Listar equipo completo");
    print("5) Contar jugadores por posicion");
    print("6) Salir del sistema");

    try:
        opc = int(input("Ingrese su opcion: "));
    except ValueError:
        print("La opción de menu debe ser un valor numerico del 1 al 6.");
        continue;

    if(opc == 1):
        if(len(jugadores) >= 11):
            print("La plantilla esta llena.");
        else:
            rut = input("Ingrese el rut del jugador a registrar: ");

            if(rut in jugadores):
                print("El jugador ya existe en el registro.");
                continue;
            else:
                try:
                    nombre = input("Ingrese el nombre del jugador: ");
                    validador = fun.validar_nombre(nombre);
                    if(validador):
                        raise ValueError;
                except ValueError:
                    print("El nombre no puede contener numeros.");
                try:
                    peso = float(input("Ingrese el peso del jugador: "));
                    if(peso <= 0):
                        raise ValueError;
            
                    altura = float(input("Ingrese la altura del jugador en metros: "));
                    if(altura <= 0):
                        raise ValueError;

                except ValueError:
                    print("El peso y la altura del jugador deben ser numeros positivos.");
                    continue;

                try:
                    posicion = int(input("Posición: 1.Arquero, 2.Defensa, 3.Medio Campo, 4.Delantero"));
                
                    if(posicion not in [1,2,3,4]):
                        raise ValueError;
                
                except ValueError:
                    print("La posición debe ser un numero del 1 al 4.");

                jugadores[rut] = {
                    "nombre": nombre,
                    "peso": peso,
                    "altura": altura,
                    "posicion": posicion
                };

                print("Jugador ingresado exitosamente!");


    elif(opc == 2):
        rut = input("Ingrese el rut del jugador que desea consultar: ");
        fun.buscar_jugador(rut);

    elif(opc == 3):
        rut = input("Ingrese el rut del jugador que desea consultar: ");
        fun.estado_nutricional(rut);

    elif(opc == 4):
        if(len(jugadores) == 0):
            print("No hay jugadores registrados en la plantilla.");
        else:
            for clave, valor in jugadores.items():
                print(f"Rut: {clave} - Nombre: {valor["nombre"]}, Peso: {valor["peso"]}, Altura: {valor["altura"]}, Posicion: {fun.validador_posicion(valor["posicion"])}");

    elif(opc == 5):
        contadores = {"Arquero": 0, "Defensa": 0, "Medio Campo": 0, "Delantero": 0};

        for valor in jugadores.values():
            puesto = fun.validador_posicion(valor["posicion"]);

            if(puesto in contadores):
                contadores[puesto] += 1;

        for clave, valor in contadores.items():
            print(f"{clave}: {valor}");

    elif(opc == 6):
        print("Cerrando el sistema.");
        break;

    else:
        print("Opcion invalida!");

tralalero tralala!



