from socket import *
import hashlib
import time
import string

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Servidor TCP Listo')

def findHashCombination(targetHash):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'  # Letras minúsculas y números
    startTime = time.time()  # Inicio de tiempo
    combinationsTested = 0

    # Probar combinaciones hasta encontrar la correcta
    for caracter1 in characters:
        for caracter2 in characters:
            for caracter3 in characters:
                for caracter4 in characters:
                    combinationStr = caracter1 + caracter2 + caracter3 + caracter4

                    # Calcular hash MD5
                    hashMd5 = hashlib.md5(combinationStr.encode()).hexdigest()
                    combinationsTested += 1
                    print(f"Probando: '{combinationStr}' -> Hash: {hashMd5}")

                    # Verificar si el hash coincide
                    if hashMd5 == targetHash:
                        endTime = time.time()
                        totalTime = endTime - startTime
                        print(f"Combinación: '{combinationStr}'")
                        print(f"Hash: {hashMd5}")
                        print(f"Tiempo total: {totalTime:.3f} segundos")
                        return combinationStr, hashMd5, combinationsTested, totalTime

    # Si no se encontró
    endTime = time.time()
    totalTime = endTime - startTime
    return None, targetHash, combinationsTested, totalTime

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print(f"\nConexión establecida desde: {addr}")

        sentence = connectionSocket.recv(1024)
        receivedHash = sentence.decode().strip()
        print(f"Hash recibido: {receivedHash}")

        combination, hashValue, testedCount, searchTime = findHashCombination(receivedHash)

        # Enviar respuesta al cliente
        if combination:
            responseMessage = f"{combination}"
        else:
            responseMessage = "No encontrado"

        connectionSocket.send(responseMessage.encode())
        connectionSocket.close()

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")

serverSocket.close()