import re   #regular Expressions

def is_valid_email(email:str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    def is_valid_email(email: str):
    if '@' in email:
        divide_string = email.split('@')
        if len(divide_string) == 2 and "." in divide_string[1]: # not optimal since it only returns True if there is no subdomain
            return True
        else:
            return False
    else:
        return False
