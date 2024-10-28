from http.server import BaseHTTPRequestHandler, HTTPServer
import sys


class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Проверяем путь запроса
        if self.path == "/healthz":
            # Отправляем ответ 200 OK
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"200 OK\n")
        else:
            # Отправляем ответ 404 Not Found для остальных путей
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found\n")


def run_server(port=8080):
    # Настраиваем адрес и порт сервера
    server_address = ("", port)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print(f"Server is running on port {port}...")

    try:
        # Запускаем сервер
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
        httpd.server_close()
        sys.exit(0)


if __name__ == "__main__":
    run_server()
