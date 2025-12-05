# tcp_client.py
import asyncio
import sys

HOST = "127.0.0.1"
PORT = 8888

async def tcp_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    print(f"Connected to {HOST}:{PORT}. Type messages and press Enter. Ctrl+C to quit.")

    async def listen():
        while True:
            data = await reader.readline()
            if not data:
                print("Server closed the connection.")
                return
            print(data.decode().rstrip())

    asyncio.create_task(listen())

    loop = asyncio.get_running_loop()
    try:
        while True:
            line = await loop.run_in_executor(None, sys.stdin.readline)
            if not line:
                break
            writer.write(line.encode())
            await writer.drain()
    except KeyboardInterrupt:
        pass
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_client())
