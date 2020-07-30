import http.server
import socket
import socketserver

PORT = 80


def get_interface_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        interface_ip = get_interface_ip()
        host = self.address_string()

        page_format = """
        <body>
          <p>
            <ul>
              <li>Source : {}</li>
              <li>Destination : {}</li>
            </ul>
          </p>
        </body>
        """.format(interface_ip, host)
        self.wfile.write(bytes(page_format, "utf8"))


if __name__ == '__main__':
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("Serving at {}".format(PORT))
    httpd.serve_forever()
