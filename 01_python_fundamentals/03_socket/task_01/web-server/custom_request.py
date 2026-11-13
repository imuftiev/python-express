class Request:
    def __init__(self, method, path, ver, headers, rfile):
        self.method = method
        self.path = path
        self.ver = ver
        self.headers = headers
        self.rfile = rfile
