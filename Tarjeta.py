class Tarjeta:
    def __init__(self):
        self._saldo = 0.0
        self._identificado = False
        self._numeroIntentos = 0


    def verificar_pin(self, pin_cifrado):
        pin = 5555
        if self._numeroIntentos >2:
            print("Tu tarjeta se ha bloqueado, por varios códigos erroneos")
        else:
            pin_descifrado = self.descifrar(pin_cifrado)
            if pin == pin_descifrado:
                self._identificado = True
            self._numeroIntentos += 1

    def descifrar(self, monto_cifrado):
        clave = "1968235407"
        monto = ""
        for numero in monto_cifrado:
            if numero == ".":
                monto = monto + numero
            else:
                numero_descifrado = str(clave[int(numero)])
                monto = monto + numero_descifrado
        monto = float(monto)
        return monto
    def escribir(self, monto_cifrado):
        if self._identificado == True:
            monto = self.descifrar(monto_cifrado)
            self._saldo += monto

            print(f"saldo actualizado: {self._saldo: 2f}")
        else:
            print("Pin incorrecto")

    def leer(self):
        if self._identificado == True:
            print(f"saldo actual: {self._saldo: 2f}")
            return self._saldo
        else:
            print("Pin incorrecto")

class Cajero:

    def cifrar(self, monto):
        clave = "1968235407"
        nuevomonto = ""
        for numero in monto:
            if numero == ".":
                nuevomonto = nuevomonto + numero
            else:
                posicion = clave.index(numero)
                nuevomonto = nuevomonto + str(posicion)
        return nuevomonto

    def __init__(self):
        self.tarjeta = Tarjeta()

    def ejecutar(self):
        pin = input("Introduce el pin: ")
        pin_cifrado = self.cifrar(pin)
        self.tarjeta.verificar_pin(pin_cifrado)
        while True:
            print("\n1, Depositar saldo")
            print("2, Consultar saldo")
            print("3, Repetir código")
            print("4, Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                try:
                    monto = (input("Ingrese el monto a ejecutar: "))
                    if float(monto) < 0:
                        print("El monto no puede ser negativo")
                    else:
                        nuevomonto = self.cifrar(monto)
                        self.tarjeta.escribir(nuevomonto)
                except ValueError:
                    print("Por favor, ingresa un número válido")
            elif opcion == "2":
                self.tarjeta.leer()
            elif opcion == "3":
                nuevo_pin = input("Vuelva a ingresar el PIN: ")
                self.tarjeta.verificar_pin(self.cifrar(nuevo_pin))
                
            elif opcion == "4":
                print("Saliendo del programa")
                break
            else:
                print("Opción no válida, intentelo de nuevo")

if __name__ == "__main__":
    cajero = Cajero()
    cajero.ejecutar()