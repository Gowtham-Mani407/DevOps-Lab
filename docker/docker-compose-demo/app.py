from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

DATA_DIR = Path("/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DATA_FILE = DATA_DIR / "message.txt"


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/write":

            DATA_FILE.write_text(
                "Hello Gowtham! This data is stored in Docker Volume.\n"
            )

            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                b"Data written to Docker volume successfully!"
            )

        elif self.path == "/read":

            if DATA_FILE.exists():

                content = DATA_FILE.read_text()

                self.send_response(200)
                self.end_headers()
                self.wfile.write(content.encode())

            else:

                self.send_response(404)
                self.end_headers()
                self.wfile.write(
                    b"No data found in volume."
                )

        else:

            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                b"Welcome to Docker Volume Demo!"

            )


server = HTTPServer(("0.0.0.0", 8000), MyHandler)

print("Server running on port 8000...")

server.serve_forever()
