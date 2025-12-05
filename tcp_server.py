import asyncio

HOST= "127.0.0.1"
PORT = 8888

clients = set()

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    clients.add(writer)
    print(f"Client connected: {addr}")
    
    try:
        while True:
            data = await reader.readline()
            if not data:
                break
            message = data.decode().strip()
            print(f"Received from {addr}: {message}")
            # Broadcast the message to all connected clients
            
            for w in list(clients):
                try:
                    w.write(f"{addr}: {message}\n".encode())
                    await w.drain()
                except Exception:
                    clients.discard(w)
    except asyncio.CancelledError:
        pass
    finally:
        print(f"Client disconnected: {addr}")
        clients.discard(writer)
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped manually")