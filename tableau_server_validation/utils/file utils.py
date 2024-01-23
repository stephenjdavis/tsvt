import csv
import pytest

def add(a, b):
    return a + b

def read_test_data(file_path):
    test_data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            test_data.append(tuple(map(int, row)))
    return test_data

@pytest.mark.parametrize("input_a, input_b, expected_result", read_test_data('test_data.tsv'))
def test_addition(input_a, input_b, expected_result):
    try:
        result = add(input_a, input_b)
        assert result == expected_result
    except AssertionError as e:
        # Report test failure to TeamCity
        print(f"##teamcity[testStarted name='test_addition({input_a}, {input_b}, {expected_result})']")
        print(f"##teamcity[testFailed name='test_addition({input_a}, {input_b}, {expected_result})' message='{str(e)}']")
        print("##teamcity[testFinished name='test_addition']")

if __name__ == "__main__":
    # This is needed to prevent errors when running the script outside of pytest
    pytest.main()
