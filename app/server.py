from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "0.0.0.0"
hostPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Flats and images</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Here are the flats and images:</p>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_response(404)


print("Server works")

if __name__ == "__main__":
    print("Server works")
    webServer = HTTPServer((hostName, hostPort), MyServer)
    print("Server started http://%s:%s" % (hostName, hostPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped...")