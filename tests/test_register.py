from fixture.constants.constants import ResponseText
from fixture.controller import Controller
from fixture.register.model import RegisterUser, RegisterUserResponse


class TestRegister:
    """
    Steps:
    1. Generate random email and password
    2. Push post request to api for registation
    3. Check answer body
    3. Check status code
    4. Check response message
    """
    def test_register_user_valid_data(self, app: Controller) -> None:
        data = RegisterUser.random()
        res = app.register.registration(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == ResponseText.RESPONSE_MESSAGE
