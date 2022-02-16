import socket


def request(verb, url, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 5000))
        sock.send(f"{verb} /{url} HTTP/1.1\r\n".encode())
        sock.send("Content-Type: text/plain\r\n".encode())
        sock.send(f"Content-Length: {len(value)}\r\n\r\n".encode())
        sock.send(f"{value}\r\n".encode())
        while True:
            s = sock.recv(4096).decode('utf-8')
            if s == '':
                break;
            postString = s.split("\n")

        sock.close()


if __name__ == '__main__':
    print("Quel est votre prénom ?")
    nom = input()

    while True:
        request("GET", "first_letter", "")
        content = input("Key/Text (Q to quit) :")
        if content == ("Q" or "q"):
            break
        else:
            items = content
            if len(items) > 1:
                request("POST", nom, items)
                request("GET", "", "")
