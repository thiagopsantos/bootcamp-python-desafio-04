from typing import List
from pytest import raises
from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest():
    def __init__(self, payload) -> None:
        self.json = payload

class MockDriverHandler():
    def arithmetic_mean(self, numbers: List[float]) -> float:
        return 2.5

def test_calculate():
    mock_request = MockRequest({
        "numbers": [1,1,1]
    })

    driver = MockDriverHandler()
    calculator = Calculator4(driver)

    response = calculator.calculate(mock_request)

    assert response == { "data": { "Calculator": 4, "arithmetic_mean": 2.5 }
}

def test_calculate_unprocessable_entity_error():
    mock_request = MockRequest({
        "number": 1
    })

    driver = MockDriverHandler()
    calculator = Calculator4(driver)

    with raises(HttpUnprocessableEntityError) as exinfo:
        calculator.calculate(mock_request)

    assert str(exinfo.value) == 'Body mal formatado'

def test_calculate_integration():
    mock_request = MockRequest({
        "numbers": [5,10,15, 20]
    })

    driver = NumpyHandler()
    calculator = Calculator4(driver)

    response = calculator.calculate(mock_request)

    assert response == { "data": { "Calculator": 4, "arithmetic_mean": 12.5 } }
