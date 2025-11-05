import socket

PORT = 2025
BUFFER_SIZE = 1024
HOST = 'localhost'

BLAZER_ID = "mdoshi"
REQUESTED_FILE = f"{BLAZER_ID}.txt"
RECEIVED_FILE = f"{BLAZER_ID}-received.txt"
PROCESSED_FILE = f"{BLAZER_ID}-processed.txt"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"[CLIENT] Connected to {HOST}:{PORT}")

        # Send request
        client.sendall(REQUESTED_FILE.encode())
        print(f"[CLIENT] Requested file: {REQUESTED_FILE}")

        # Receive file
        received_data = client.recv(BUFFER_SIZE).decode()

        if received_data.startswith("ERROR"):
            print(f"[CLIENT] Server error: {received_data}")
            return

        # Save received file
        with open(RECEIVED_FILE, 'w') as file:
            file.write(received_data)
        print(f"[CLIENT] Saved received file as {RECEIVED_FILE}")

        # Process file (uppercase)
        processed_content = received_data.upper()
        with open(PROCESSED_FILE, 'w') as file:
            file.write(processed_content)
        print(f"[CLIENT] Saved processed file as {PROCESSED_FILE}")

        # Send processed file back
        client.sendall(f"PROCESSED:{processed_content}".encode())
        print(f"[CLIENT] Sent processed file back to server")

if __name__ == '__main__':
    main()
