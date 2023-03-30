"""
La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo 
de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos: cada carácter deberá ser encriptado a ocho caracteres;
se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “{” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
"""


class Encriptador:
    def __init__(self):
        self.tabla_encriptacion = {}
        self.tabla_desencriptacion = {}

    def generar_tabla_encriptacion(self):
        caracteres = list(range(32, 126)) # Caracteres desde " " hasta "}"
        for c in caracteres:
            cadena_encriptada = self.__encriptar_caracter(chr(c))
            self.tabla_encriptacion[chr(c)] = cadena_encriptada

    def generar_tabla_desencriptacion(self):
        for clave, valor in self.tabla_encriptacion.items():
            self.tabla_desencriptacion[valor] = clave

    def __encriptar_caracter(self, caracter):
        codigo = ord(caracter)
        binario = bin(codigo)[2:].zfill(8) # Convertir el código a binario con 8 bits
        encriptado = ""
        for bit in binario:
            encriptado += str(int(bit) ^ 1) # Encriptar cambiando 1 por 0 y viceversa
        return encriptado * 8 # Repetir la cadena encriptada 8 veces para tener 64 bits (8 caracteres)

    def encriptar_mensaje(self, mensaje):
        mensaje_encriptado = ""
        for c in mensaje:
            if c in self.tabla_encriptacion:
                mensaje_encriptado += self.tabla_encriptacion[c]
            else:
                mensaje_encriptado += c
        return mensaje_encriptado

    def desencriptar_mensaje(self, mensaje_encriptado):
        mensaje_desencriptado = ""
        for i in range(0, len(mensaje_encriptado), 64):
            cadena_encriptada = mensaje_encriptado[i:i+64]
            if cadena_encriptada in self.tabla_desencriptacion:
                mensaje_desencriptado += self.tabla_desencriptacion[cadena_encriptada]
            else:
                mensaje_desencriptado += cadena_encriptada
        return mensaje_desencriptado



if __name__ == "__main__":
    # Crear un objeto Encriptador
    encriptador = Encriptador()

    # Generar las tablas de encriptación y desencriptación
    encriptador.generar_tabla_encriptacion()
    encriptador.generar_tabla_desencriptacion()

    # Encriptar un mensaje
    mensaje = "Hola rebelión!"
    mensaje_encriptado = encriptador.encriptar_mensaje(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)

    # Desencriptar el mensaje encriptado
    mensaje_desencriptado = encriptador.desencriptar_mensaje(mensaje_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)