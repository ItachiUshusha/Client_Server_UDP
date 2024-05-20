import socket

HOST = ""  # IP адрес сервера
PORT = 27161  # номер TCP порта

# создаем объект сокета
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # применяется для привязки сокета к конкретному сетевому интерфейсу и номеру порта
    s.bind((HOST, PORT))

    print("UDP server up and listening")

    while True:
        # принимает сообщение от клиента в скобках указан максимальный размер получаемых данных
        message, address = s.recvfrom(1024)

        # проверка, ввел ли клиент ключевое слово, если да, то завершаем цикл
        if message.decode("utf-8") == "EXIT()":
            break

        print("Ответ пользователя:", address[0] + ":" + str(address[1]), message.decode("utf-8"))

        # отправляем клиенту ответ
        message = input(" -> ")

        # проверка, если на сервере ввели ключевое слово, то завершаем цикл
        if message == "EXIT()":
            break

        # отправляем сообщение клиенту
        s.sendto(message.encode("utf-8"), address)

    # если сервер разорвал соединение, то закрываем сокет
    try:
        s.sendto(message.encode("utf-8"), address)
        print("Разорвано соединение с клиентом", address[0] + ":" + str(address[1]))
        s.close()
    # если пользователь разорвал соединение, то закрываем сокет
    except AttributeError:
        print("Разорвано соединение с клиентом", address[0] + ":" + str(address[1]))
        s.close()
