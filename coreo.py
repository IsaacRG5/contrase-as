correo = input("Ingrese su correo: ")

if correo.count("@") == 1:
    poscion_arroba = correo.index("@")
    punto_despues = False
    for carecter in correo[poscion_arroba + 1:]:
        if carecter == ".":
            punto_despues = True

    if punto_despues:
        print("Valido")
    else:
        print("ERROR : El punto debe de estar despues del @")
else:
    print("ERROR: Debe de tener una sola @")