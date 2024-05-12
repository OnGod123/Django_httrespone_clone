import socket

def serve_file(file_path, port=8080):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(1)

    print(f"Server listening on port {port}...")

    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # Read the requested file
            with open(file_path, 'rb') as file:
                file_content = file.read()

            # Construct HTTP response with the file content
            response = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: application/octet-stream\r\n"
                b"Content-Length: " + str(len(file_content)).encode() + b"\r\n"
                b"\r\n"
                + file_content
            )

            # Send the response to the client
            client_socket.sendall(response)

        except FileNotFoundError:
            # If the file is not found, return a 404 response
            response = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found"
            client_socket.sendall(response)

        # Close the client socket
        client_socket.close()

    # Close the server socket
    server_socket.close()

if __name__ == "__main__":
    file_path = "/path/to/your/file.txt"
    serve_file(file_path)

