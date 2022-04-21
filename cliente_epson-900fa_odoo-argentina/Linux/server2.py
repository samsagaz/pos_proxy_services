from gevent import monkey
monkey.patch_all()

import os
from gevent.pywsgi import WSGIServer
import server

http_server = WSGIServer(('0.0.0.0', 5005), server)
http_server.serve_forever()

