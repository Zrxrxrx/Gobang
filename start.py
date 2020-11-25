import webbrowser
from Server.server import Server as baseServer
#文件服务器
baseServer()
webbrowser.open("http://localhost:8888")