import asyncio
import websockets
import json
import game
# 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
async def recv_msg(websocket):
    g = None
    while True:
        recv_text = await websocket.recv()
        await websocket.send("get")
        data = json.loads(recv_text)
        
        if(data['type']=='start'):
            g = game.Game(size=data['data'])
            await websocket.send(','.join(str(i) for i in g.getRawTable()))
        if(data['type']=='chess'):
            g.chess(data['data'][0],data['data'][1])
            await websocket.send(','.join(str(i) for i in g.getRawTable()))
            if(g.checkWin(data['data'][0],data['data'][1])):
                await websocket.send("win")
        

# 服务器端主逻辑
# websocket和path是该函数被回调时自动传过来的，不需要自己传
async def main_logic(websocket, path):
    await recv_msg(websocket)

# 把ip换成自己本地的ip
start_server = websockets.serve(main_logic, '127.0.0.1', 5678)
# 如果要给被回调的main_logic传递自定义参数，可使用以下形式
# 一、修改回调形式
# import functools
# start_server = websockets.serve(functools.partial(main_logic, other_param="test_value"), '10.10.6.91', 5678)
# 修改被回调函数定义，增加相应参数
# async def main_logic(websocket, path, other_param)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()