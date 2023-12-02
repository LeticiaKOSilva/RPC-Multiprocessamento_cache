from rpc.server import Server

server = Server('', 6001)
server.createThread()