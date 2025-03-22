import asyncio
import datetime
import random
import websockets

async def myServ(ws, path=None):  # Make 'path' optional
    while True:
        now = 'Vamke2102983' + datetime.datetime.utcnow().isoformat()
        await ws.send(now)
        await asyncio.sleep(1 + random.random() * 3)

async def main():
    # Create a WebSocket server on port 12345
    start_server = await websockets.serve(myServ, 'localhost', 12345)
    print("WebSocket server started on ws://localhost:12345")
    await start_server.wait_closed()  # Keep the server running

# Run the server
if __name__ == "__main__":
    asyncio.run(main())