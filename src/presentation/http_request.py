class HttpRequest:

    def __init__(
            self,
            headers: dict = None, 
            body: dict = None, 
            query_params: dict = None,
            path_params: dict = None,
            url = None,
            ipv4 = None,
            ):
        
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
   