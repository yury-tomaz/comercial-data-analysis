class HttpResponse:

    def __init__(self, status_code: int, body: dict = None):
        self.status_code = status_code
        self.body = body