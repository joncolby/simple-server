import SimpleHTTPServer
import SocketServer
import os

doc_root = '/var/www'

if os.path.exists(doc_root):
    os.chdir(doc_root)
else:
    os.chdir('/')

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
