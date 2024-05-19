from typing import List
from abc import ABC, abstractmethod

class DriverHandlerInterface(ABC):

    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def arithmetic_mean(self, numbers: List[float]) -> float:
        pass
