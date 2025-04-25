from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PetListerView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        body_response = self.__controller.delete(name)
        
        return HttpResponse(status_code=204, body=body_response)