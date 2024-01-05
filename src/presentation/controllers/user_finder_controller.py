from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.presentation.http_response import HttpResponse
from src.presentation.http_request import HttpRequest

class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__user_finder = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params['first_name'] 

        response = self.__user_finder.find(first_name)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
    
    