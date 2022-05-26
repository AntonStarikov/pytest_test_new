from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculator_division(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_multiply_calculator_subtraction(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_multiply_calculator_adding(self):
        assert self.calc.adding(self, 5, 5) == 10
