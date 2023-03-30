"""
La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo 
de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos: cada carácter deberá ser encriptado a ocho caracteres;
se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
"""


import hashlib

class RebelEncryption:
    def __init__(self):
        self.char_to_ascii = {}
        self.ascii_to_char = {}
        for i in range(32, 126):
            char = chr(i)
            ascii_val = str(i)
            bin_val = bin(i)[2:].zfill(8)
            hashed_val = hashlib.sha256(bin_val.encode()).hexdigest()
            self.char_to_ascii[char] = hashed_val
            self.ascii_to_char[ascii_val] = char

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char in self.char_to_ascii:
                encrypted_message += self.char_to_ascii[char]
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for i in range(0, len(encrypted_message), 64):
            block = encrypted_message[i:i+64]
            ascii_val = ""
            for j in range(0, 64, 8):
                hashed_val = block[j:j+8]
                for k, v in self.char_to_ascii.items():
                    if v == hashed_val:
                        ascii_val += str(ord(k))
                        break
            if ascii_val in self.ascii_to_char:
                decrypted_message += self.ascii_to_char[ascii_val]
        return decrypted_message


# Prueba del código
if __name__ == "__main__":
    rebel_encryption = RebelEncryption()
    message = "La princesa Leia ha enviado un mensaje urgente desde la base rebelde"
    encrypted_message = rebel_encryption.encrypt(message)
    decrypted_message = rebel_encryption.decrypt(encrypted_message)

    print("Mensaje original:", message)
    print("Mensaje encriptado:", encrypted_message)
    print("Mensaje desencriptado:", decrypted_message)
