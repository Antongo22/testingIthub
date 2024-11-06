import pytest
import pandas as pd
from task1 import get_list

def expected_results():
    filename = "grades.csv"
    return get_list(filename)

class TestTask1:
    @pytest.mark.parametrize("expected, actual", expected_results())
    def test_final(self, expected, actual):
        assert expected == actual
