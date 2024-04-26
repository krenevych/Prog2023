from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):
    @abstractmethod
    def visit_military_base(self,base):
        pass
    @abstractmethod
    def visit_general_staff(self, staff):
        pass
