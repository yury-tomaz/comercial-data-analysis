from abc import ABC, abstractmethod
from src.presentation.http_response import HttpResponse
from src.presentation.http_request import HttpRequest

class ControllerInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: pass