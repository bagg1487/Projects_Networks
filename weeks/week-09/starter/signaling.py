import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONNECTIONS = set()
PEERS = {} 

async def handler(websocket):
    client_id = None
    
    try:
        async for message in websocket:
            data = json.loads(message)
            
            if data.get('type') == 'register':
                client_id = data.get('id')
                PEERS[client_id] = websocket
                logger.info(f"Client registered: {client_id}")
                await websocket.send(json.dumps({'type': 'registered', 'id': client_id}))
            
            elif data.get('type') == 'offer':
                target = data.get('target')
                if target in PEERS:
                    logger.info(f"Forwarding offer from {client_id} to {target}")
                    await PEERS[target].send(json.dumps({
                        'type': 'offer',
                        'from': client_id,
                        'sdp': data.get('sdp')
                    }))
            
            elif data.get('type') == 'answer':
                target = data.get('target')
                if target in PEERS:
                    logger.info(f"Forwarding answer from {client_id} to {target}")
                    await PEERS[target].send(json.dumps({
                        'type': 'answer',
                        'from': client_id,
                        'sdp': data.get('sdp')
                    }))
            
            elif data.get('type') == 'ice':
                target = data.get('target')
                if target in PEERS:
                    logger.info(f"Forwarding ICE candidate from {client_id} to {target}")
                    await PEERS[target].send(json.dumps({
                        'type': 'ice',
                        'from': client_id,
                        'candidate': data.get('candidate')
                    }))
            
            elif data.get('type') == 'message':
                target = data.get('target')
                if target in PEERS:
                    logger.info(f"Chat message from {client_id} to {target}")
                    await PEERS[target].send(json.dumps({
                        'type': 'message',
                        'from': client_id,
                        'text': data.get('text'),
                        'timestamp': data.get('timestamp')
                    }))
    
    except websockets.exceptions.ConnectionClosed:
        logger.info(f"Client {client_id} disconnected")
    finally:
        if client_id and client_id in PEERS:
            del PEERS[client_id]
        if websocket in CONNECTIONS:
            CONNECTIONS.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        logger.info("Signaling server started on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())