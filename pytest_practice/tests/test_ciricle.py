import src.shapes as shapes
import pytest
import math

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up for {method}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print(f"Tearing down after {method}")

    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

    
