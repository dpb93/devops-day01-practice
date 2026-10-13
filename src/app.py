import http.server
import socketserver

PORT = 8080


class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DevOps Capstone Application</title>
        </head>
        <body style="font-family: Arial, sans-serif;
                     text-align: center;
                     margin-top: 50px;
                     background: #eef2f5;">
            <h1>DevOps Microservice Portal</h1>
            <p>Running on Python 3 Standard HTTP Server</p>
            <p>Ready for Docker Containerization (Day 02)</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        print(f"DevOps Application listening on port {PORT}...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

