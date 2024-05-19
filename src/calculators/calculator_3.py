from typing import Dict, List
from functools import reduce
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequest

class Calculator3():
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)

        response = self.__format_result(variance)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body or not isinstance(body['numbers'], list):
            raise HttpUnprocessableEntityError('Body mal formatado')

        input_data = body['numbers']
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = reduce(lambda a, b: a * b, numbers)
        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequest('Falha no processo: Variância menor que multiplicação')

    def __format_result(self, variance:float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "variance": variance,
                "Sucess": True
            }
        }
