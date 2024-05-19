from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

"""
Os arquivos precisam ter _test no final do nome.
As funcões precisam conter test_ no início do nome.
Comando para executar pytest: pytest -s -v
"""

class MockRequest():
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({ "number": 1})
    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 14.25

def test_calculate_with_body_error():
    mock_request = MockRequest({ "something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as exinfo:
        calculator_1.calculate(mock_request)

    assert str(exinfo.value) == "Body mal formatado"
