import pytest
from tableau_server_validation.scripts.validate_data_sources import validate_data_sources

def test_successful_validation(monkeypatch, capsys):
    """
    Test case for successful validation of data sources on Tableau Server.
    """
    # Replace 'https://your-tableau-server' with the actual Tableau Server URL
    tableau_server_url = 'https://your-tableau-server'

    # Replace 'your-api-token' with a valid API token for testing
    api_token = 'your-api-token'

    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data

            def json(self):
                return self.json_data

        # Mock the GET request for data sources
        if args[0] == f"{tableau_server_url}/api/3.8/sites/default/datasources":
            return MockResponse(200, {'datasources': [{'example_key': 'example_value'}]})
        else:
            return MockResponse(404, None)

    # Use monkeypatch to mock the requests.get function
    monkeypatch.setattr("requests.get", mock_get)

    # Call the validation function
    validate_data_sources(tableau_server_url, api_token)

    # Capture the printed output and check for success message
    captured = capsys.readouterr()
    assert "Data sources validation successful." in captured.out

def test_invalid_server_url(monkeypatch, capsys):
    """
    Test case for validation failure with an invalid Tableau Server URL.
    """
    # Replace 'https://invalid-tableau-server' with an invalid Tableau Server URL
    tableau_server_url = 'https://invalid-tableau-server'

    # Replace 'your-api-token' with a valid API token for testing
    api_token = 'your-api-token'

    def mock_get(*args, **kwargs):
        # Mock the GET request for an invalid server URL
        return {'status_code': 404, 'json_data': None}

    # Use monkeypatch to mock the requests.get function
    monkeypatch.setattr("requests.get", mock_get)

    # Call the validation function
    validate_data_sources(tableau_server_url, api_token)

    # Capture the printed output and check for failure message
    captured = capsys.readouterr()
    assert "Data sources validation failed." in captured.out

# Additional test cases can be added as needed
