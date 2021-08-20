def main():
    #escribe tu código abajo de esta línea

    edad =int(input("Ingresa tu edad: "))

    if edad > 0 and edad<= 120:
        if edad >= 18:
            iden = input("¿Tienes identificación oficial? (s/n): ")
            if iden == "s":
                print("Trámite de licencia concedido")
            elif iden == "n":
                print("No cumples requisitos")
            else:
                print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

if __name__ == '__main__':
    main()
