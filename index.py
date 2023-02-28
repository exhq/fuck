from http.server import BaseHTTPRequestHandler, HTTPServer
import constants
import json
from functools import cache
hostName = "localhost"

@cache
def config(key):
    with open('config.json', 'r') as f:
        config_data = json.load(f)
        return config_data.get(key, None)

lmao = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789/+"

def check(x: str):
    return all(i in lmao for i in x)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        if self.path == "/" or check(self.path):
            self.wfile.write(constants.true(self.path.replace(
                "fuck/", "").replace("+", " ")[1:]).encode("utf-8"))
        else:
            self.wfile.write(constants.false.encode("utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, config("port")), MyServer)
    print("Server started http://%s:%s" % (hostName, config("port")))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")