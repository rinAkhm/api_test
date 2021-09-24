from requests import Response

from common.deco import logging as log
from fixture.register.model import RegisterUser
from fixture.res_validator import Validator


class Register(Validator):
    def __init__(self, app):
        self.app = app

    POST_REGISTER = "/register"

    @log("register user")
    def registration(self, data: RegisterUser, type_response=None) -> Response:
        res = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_REGISTER}",
            json=data.to_dict(),
        )
        return self.structure(res, type_response=type_response)
