import requests


def get_api_token(tableau_server_url, username, password):
    """
    Retrieves a Tableau Server API token using username and password.

    Parameters:
    - tableau_server_url (str): The URL of the Tableau Server.
    - username (str): The username for API authentication.
    - password (str): The password for API authentication.

    Returns:
    - str: The API token for further API requests.
    """
    try:
        # Construct the API endpoint for token creation (adjust API version if needed)
        token_endpoint = f"{tableau_server_url}/api/3.8/auth/signin"

        # Set up payload with username and password
        payload = {
            'credentials': {
                'name': username,
                'password': password,
                'site': {
                    'contentUrl': ''
                }
            }
        }

        # Make a POST request to get the API token
        response = requests.post(token_endpoint, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            api_token = response.json()['credentials']['token']
            return api_token
        else:
            # Print details if token retrieval fails
            print(f"Token retrieval failed. Status Code: {response.status_code}")
            print(response.text)

    except requests.RequestException as e:
        # Handle exceptions and print error details
        print(f"Error retrieving API token: {e}")
        raise  # Re-raise the exception for test cases to catch


# Example usage:
if __name__ == '__main__':
    # Replace 'https://your-tableau-server' with the actual Tableau Server URL
    tableau_server_url = 'https://your-tableau-server'

    # Replace 'your-username' and 'your-password' with actual credentials for token retrieval
    username = 'your-username'
    password = 'your-password'

    # Call the utility function to get the API token
    api_token = get_api_token(tableau_server_url, username, password)
    print(f"API Token: {api_token}")
