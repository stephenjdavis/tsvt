import re


def validate_url(url):
    """
    Validates the format of a URL.

    Parameters:
    - url (str): The URL to be validated.

    Returns:
    - bool: True if the URL is valid, False otherwise.
    """
    # Use a simple regular expression to check if the URL has a valid format
    url_pattern = re.compile(r'^https?://(?:www\.)?\S+$')
    return bool(re.match(url_pattern, url))


def validate_email(email):
    """
    Validates the format of an email address.

    Parameters:
    - email (str): The email address to be validated.

    Returns:
    - bool: True if the email address is valid, False otherwise.
    """
    # Use a regular expression for basic email format validation
    email_pattern = re.compile(r'^\S+@\S+\.\S+$')
    return bool(re.match(email_pattern, email))


# Example usage:
if __name__ == '__main__':
    # Replace 'https://example.com' with the actual URL for validation
    example_url = 'https://example.com'

    # Replace 'user@example.com' with the actual email address for validation
    example_email = 'user@example.com'

    # Call the utility functions for validation
    is_valid_url = validate_url(example_url)
    is_valid_email = validate_email(example_email)

    # Print validation results
    print(f"URL Validation: {is_valid_url}")
    print(f"Email Validation: {is_valid_email}")
