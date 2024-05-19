from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4():
    def __init__(self, driver_handle: DriverHandlerInterface) -> None:
        self.__driver_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        arithmetic_mean = self.__calculate_mean(input_data)

        response = self.__format_result(arithmetic_mean)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body or not isinstance(body['numbers'], list):
            raise HttpUnprocessableEntityError('Body mal formatado')

        input_data = body['numbers']
        return input_data

    def __calculate_mean(self, numbers: List[float]) -> float:
        arithmetic_mean = self.__driver_handle.arithmetic_mean(numbers)
        return arithmetic_mean

    def __format_result(self, arithmetic_mean:float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "arithmetic_mean": arithmetic_mean
            }
        }
