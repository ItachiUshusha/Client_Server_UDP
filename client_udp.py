import socket

# принимаем адрес и порт сервера от пользователя
HOST_PORT = input("Введите адрес сервера в формате localhost:12345 -> ").split(":")
HOST = HOST_PORT[0]
PORT = int(HOST_PORT[1])

# создаем объект сокета
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # подключаемся к серверу и отправляем сообщение
    s.connect((HOST, PORT))
    print("Успешное соединение с сервером ", HOST_PORT[0] + ":" + HOST_PORT[1])

    message = input(" -> ")

    # cоздаем цикл который проверяет введено ли ключевое слово при котором программа прекращает работу
    while message != "EXIT()":

        # отправляем данные на сервер
        s.sendto(message.encode("utf-8"), (HOST, PORT))

        # принимаем сообщение от сервера
        message, adress = s.recvfrom(1024)

        # если сервер прислал ключевое слово, то происходит выход из цикла
        if message.decode("utf-8") == "EXIT()":
            break

        print("Ответ от сервера", HOST_PORT[0] + ":" + HOST_PORT[1], ":", message.decode("utf-8"))
        message = input(" -> ")

    # если пользователь разорвал соединение, то закрываем сокет
    try:
        s.sendto(message.encode("utf-8"), (HOST, PORT))
        print("Разорвано соединение с сервером", HOST_PORT[0] + ":" + HOST_PORT[1])
        s.close()
    # если сервер разорвал соединение, то закрываем сокет
    except AttributeError:
        print("Разорвано соединение с сервером", HOST_PORT[0] + ":" + HOST_PORT[1])
        s.close()
