import asyncio
import websockets
import json
import game
import sys
sys.path.append("..")
import ai
# 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
async def recv_msg(websocket):
    g = None
    while True:
        recv_text = await websocket.recv()
        await websocket.send("get")
        data = json.loads(recv_text)
        if(data['type']=='start'):
            g = game.Game(size=data['data'])
            aichess = ai.chessOne(g.tableTree)
            g.chess(aichess[0],aichess[1])
            await websocket.send(json.dumps({'type':'data','data':g.getRawTable()}))
            aichess = ai.chessOne(g.tableTree)
            await websocket.send(json.dumps({'type':'predict','data':aichess[2]}))
            #await websocket.send(','.join(str(i) for i in g.getRawTable()))
        if(data['type']=='chess'):
            #下棋
            g.chess(data['data'][0],data['data'][1])
            #返回棋盘
            await websocket.send(json.dumps({'type':'data','data':g.getRawTable()}))
            aichess = ai.chessOne(g.tableTree)
            await websocket.send(json.dumps({'type':'predict','data':aichess[2]}))
            #检查胜利
            if(g.checkWin(data['data'][0],data['data'][1])):
                await websocket.send("you win")
        if(data['type']=='aiplay'):
            aichess = ai.chessOne(g.tableTree)
            g.chess(aichess[0],aichess[1])
            await websocket.send(json.dumps({'type':'data','data':g.getRawTable()}))
            aichess = ai.chessOne(g.tableTree)
            await websocket.send(json.dumps({'type':'predict','data':aichess[2]}))
            #检查胜利
            if(g.checkWin(aichess[0],aichess[1])):
                await websocket.send("you fail")
            
# 服务器端主逻辑
# websocket和path是该函数被回调时自动传过来的，不需要自己传
async def main_logic(websocket, path):
    await recv_msg(websocket)

# 把ip换成自己本地的ip
start_server = websockets.serve(main_logic, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()