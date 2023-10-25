import pytest
from project import get_name, transaction_format, nett

# Test get_name function
class MockInput:
    def __init__(self, inputs):
        self.inputs = iter(inputs)

    def __call__(self, prompt):
        try:
            return next(self.inputs)
        except StopIteration:
            raise EOFError

def test_get_name(monkeypatch):
    input_data = ["Alice", "Bob", "Charlie"]
    mock_input = MockInput(input_data)
    monkeypatch.setattr('builtins.input', mock_input)

    result_names = []

    while True:
        try:
            get_name(result_names)
        except EOFError:
            break

    expected_names = ["alice", "bob", "charlie"]

    assert result_names == expected_names
    
# Test transaction_format function
def test_transaction_format():
    valid_input = "John, $100.50"
    invalid_input = "Invalid input"
    assert transaction_format(valid_input) is not None
    assert transaction_format(invalid_input) is None

# Test nett function
def test_nett():
    ledger = {'Alice': 100.50, 'Bob': 50.25, 'Charlie': 75.75}
    expected_result = {'Alice': 25.00, 'Bob': -25.25, 'Charlie': 0.25}
    result = nett(ledger)
    for key in expected_result:
        assert result[key] == expected_result[key]

if __name__ == '__main__':
    pytest.main()

