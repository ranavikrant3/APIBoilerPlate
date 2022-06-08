from src.server.helpers import generic_errors
import re
import sys


def get_instance(path):
    """
    :statuscode 400: Bad Request - Raise if the browser sends something to the application the application or server cannot handle.
    :statuscode 403: Forbidden - Raise if the user doesn’t have the permission for the requested resource but was authenticated.
    :statuscode 404: Not Found - Raise if a resource does not exist and never existed.
    :statuscode 500: Internal Server Error - Raise if an internal server error occurred. This is a good fallback if an unknown error occurred in the dispatcher.
    :statuscode 401: Unauthorized - Raise if the user is not authorized to access a resource.
    """
    match = re.compile('/(v\d+)/.*').match(path)
    if match:
        try:
            module = 'src.server.controllers' + match.group(1)

            __import__('src.server.helpers.generic_errors', fromlist=[''])
            return getattr(sys.modules[module], 'errors')
        except (KeyError, AttributeError):
            return generic_errors
    return generic_errors