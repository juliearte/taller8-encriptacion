from socket import *
import hashlib
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#palabra de 4 letras
while True:
    sentence = input('Escriba una palabra de cuatro letras: ')
    if len(sentence) == 4:
        break
    else:
        print(f"Incorrecto, la palabra debe de tener solo 4 letras. Usted escribió {len(sentence)} letras.")

#cifrado
hashGenerator = hashlib.md5(sentence.encode(), usedforsecurity=True)
hashFinal = hashGenerator.hexdigest()
print(f"Mensaje codificado con MD5(): {hashFinal}")

clientSocket.send(hashFinal.encode())
modifiedSentence = clientSocket.recv(1024)
print(f"La palabra es: {modifiedSentence.decode()}")
clientSocket.close()