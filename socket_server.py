from rpc.server import Server

server = Server('', 6002)
server.createThread()