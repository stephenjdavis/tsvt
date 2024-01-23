import requests
from cyberark_integration import get_cyberark_credential  # Example CyberArk integration function


def validate_data_sources(tableau_server_url):
    """
    Validates data sources on Tableau Server.

    Parameters:
    - tableau_server_url (str): The URL of the Tableau Server to validate data sources.

    Returns:
    - None: The validation is considered successful.
    - Exception: An exception is raised if validation fails.
    """
    try:
        # Retrieve CyberArk credential for Tableau Server API authentication
        cyberark_credential = get_cyberark_credential("tableau-server-api-credential")

        # Construct the API endpoint for getting data sources (adjust API version if needed)
        datasources_endpoint = f"{tableau_server_url}/api/3.8/sites/default/datasources"

        # Set up headers with CyberArk credential for API authentication
        headers = {
            'Content-Type': 'application/json',
            'X-Tableau-Auth': cyberark_credential  # Use the CyberArk credential for authentication
        }

        # Make a GET request to get data sources
        response = requests.get(datasources_endpoint, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            datasources_info = response.json()['datasources']

            # Add specific validation checks based on datasources_info
            # Example: Check data source names, connection details, etc.

            print("Data sources validation successful.")
        else:
            # Print details if validation fails
            print(f"Data sources validation failed. Status Code: {response.status_code}")
            print(response.text)

    except requests.RequestException as e:
        # Handle exceptions and print error details
        print(f"Error validating data sources: {e}")
        raise  # Re-raise the exception for test cases to catch


# Example usage:
if __name__ == '__main__':
    # Replace 'https://your-tableau-server' with the actual Tableau Server URL
    tableau_server_url = 'https://your-tableau-server'

    # Call the validation function
    validate_data_sources(tableau_server_url)