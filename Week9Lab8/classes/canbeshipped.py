from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    
    @abstractmethod
    def can_be_shipped(self) -> bool:
        pass