from typing import Dict, List
from src.calculators.calculator_3 import Calculator3
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 1000000

def test_calculate_with_variance_error():
    mock_request = MockRequest({
        "numbers": [1,2,3,4,5]
    })

    driver = MockDriverHandlerError()
    calculator_3 = Calculator3(driver)

    with raises(Exception) as exinfo:
        calculator_3.calculate(mock_request)

    assert str(exinfo.value) == "Falha no processo: Variância menor que multiplicação"

def test_calculate_integration():
    mock_request = MockRequest({
        "numbers": [1,1,1,1,100]
    })

    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    response = calculator_3.calculate(mock_request)
    print()
    print(response)

    assert response == {'data': {'Calculator': 3, 'variance': 1000000, 'Sucess': True}}
