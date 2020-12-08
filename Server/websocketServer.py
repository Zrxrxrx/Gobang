import asyncio
import websockets
import json
import sys
sys.path.append("..")
from game import Game, players
import ai
from config import size, Ai_max_depth

async def recv_msg(websocket):
    g = None
    while True:
        recv_text = await websocket.recv()
        data = json.loads(recv_text)
        if(data['type']=='start'):
            g = Game(players['human'], size=data['data'])
            await sendTable(websocket,g.table.getArray())
        if(data['type']=='chess'):
            g.put_chess(data['data'][0], data['data'][1])
            await sendTable(websocket,g.table.getArray())
        if(data['type']=='aiplay'):
            x, y = ai.ai_step(g.table)
            d = g.put_chess(x, y)
            if d == False:
                print(x, y)
                print('AI error')
                break
            await sendTable(websocket,g.table.getArray())

async def sendTable(websocket,data):
    await websocket.send(json.dumps({'type':'data','data':data}))

async def main_logic(websocket, path):
    await recv_msg(websocket)

start_server = websockets.serve(main_logic, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()