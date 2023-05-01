"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Wolf Paulus
Contributed: Jordan Wallschlaeger

Altered to check if the inputted number is divisible by 7. It has also been changed to accept json requests.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import is_div7
import json

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            status, content = 200, "OK"
            if self.headers.get('accept') == "application/json":
                content = json.dumps({"status": status, "health": "OK"})
            else:
                content = "OK"

        elif self.path == "/" or self.path.startswith("/?number="):
            status = 200
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            result = f"{number} is {'not divisible by 7' if is_div7(int(number)) else 'divisible by 7'}." if number.isnumeric() else ""
            if self.headers.get('accept') == "application/json":
                content = json.dumps({"status": status, "number": number, "result": result})
            else:
                with open('./src/response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    content = f.read().format(path=self.path, time=asctime(), result=result)
        else:
            status, content = 404, "Not Found"
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
