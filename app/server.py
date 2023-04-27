from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2


hostName = "0.0.0.0"
hostPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def __init__(self, connection):
        self.db = connection

    def __call__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM sreality_flats LIMIT 500")
            flats = cursor.fetchall()

            if self.path == "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                message = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><h1>Flats</h1><table><tr><th>Title</th><th>Image</th></tr>'
                for flat in flats:
                    message += "<tr><td>{}</td><td><img src='{}'></td></tr>".format(flat[1], flat[2])
                message += "</table></body></html>"
                self.wfile.write(bytes(message, "utf8"))
            else:
                self.send_response(404)
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                bytes('{"error": "Something happend when processing the request: ' + str(e) + '"}', "utf8"))

connection = psycopg2.connect(database="devdb",user="devuser",password="devpass",host="db",port="5432")
connection.autocommit = True


if __name__ == "__main__":
    webServer = HTTPServer((hostName, hostPort), MyServer(connection))
    print("Server started http://%s:%s" % (hostName, hostPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped...")