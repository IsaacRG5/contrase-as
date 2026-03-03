#una mayuscula, 8 caracteres, 1 numero, signo especial
while True:

    contraseña = input("Dijite su contraseña: ")
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial =  False
    tiene_mini = False

    if len(contraseña)<=8:
        print("La contraseña debe de tener mas de 8 caracteres")
    else:
        for caracter in contraseña:
            if caracter.isupper():
                tiene_mayuscula = True
            elif caracter.isdigit():
                tiene_numero = True
            elif not caracter.isalnum():
                tiene_especial = True
        if tiene_mayuscula and tiene_numero and tiene_especial:
            print("Contraseña validad")
        else:
            print("La contraseña debe de tener")
            if not tiene_mayuscula:
                print("Al menos una letra mayuscula")
            if not tiene_numero:
                print("Al menos debe de tener un numero")
            if not tiene_especial:
                print("Al menos debe de tener un caracter especial")
                continue
            confirme_contraseña =input("Dijite de nuevo su contraseña: ")
            if contraseña == confirme_contraseña :
                    print("COINCIDCEN")
            else:
                    print("NO CONCIDEN")
        
            

