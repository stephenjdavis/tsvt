import subprocess
import os
import sys
import pytest

def run_selected_tests(test_names):
    # Get the current working directory
    current_dir = os.getcwd()

    # Define the path to the tests directory
    tests_dir = os.path.join(current_dir, "tests")

    # Construct the list of test file paths
    test_files = [os.path.join(tests_dir, f"test_{name}.py") for name in test_names]

    # Construct the pytest command
    pytest_cmd = ["pytest"] + test_files

    # Run pytest with the selected tests
    subprocess.run(pytest_cmd)

if __name__ == "__main__":
    # Get the list of test names from command-line arguments
    selected_tests = sys.argv[1:]

    if not selected_tests:
        print("Usage: python run_selected_tests.py test_name1 test_name2 ...")
        sys.exit(1)

    # Run the selected tests
    run_selected_tests(selected_tests)

