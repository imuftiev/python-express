from custom_http_server import CustomHTTPServer


def main():
    chs = CustomHTTPServer('localhost', 8080)
    chs.create_server()

main()