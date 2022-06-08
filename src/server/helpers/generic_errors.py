from flask import jsonify
from werkzeug import exceptions

def bad_request(message=exceptions.BadRequest().description, exc=None):
    """
    Raise if the browser sends something to the application the application or server cannot handle.

    400 Bad Request
    """
    response = {'error': 'Bad Request', 'message': message}
    if exc:
        response['type'] = exc.__class__.__name__
    response = jsonify(response)
    response.status_code = 400
    return response


def forbidden(message=exceptions.Forbidden().description):
    """
    Raise if the user doesn’t have the permission for the requested resource but was authenticated.

    403 Forbidden

    @param message:
    @return:
    """
    response = jsonify({'error': 'Forbidden', 'message': message})
    response.status_code = 403
    return response


def not_found(message=exceptions.NotFound().description):
    """
    Raise if a resource does not exist and never existed.

    404 Not Found
    """
    response = jsonify({'error': 'Not Found 20', 'message': message})
    print(message)
    response.status_code = 404
    return response


def server_error(message):
    """
    Raise if an internal server error occurred. This is a good fallback if an unknown error occurred in the dispatcher.

    500 Internal Server Error
    """
    response = jsonify({'error': 'Server Error', 'message': message})
    response.status_code = 500
    return response


def unauthorized(error='Unauthorized', message=exceptions.Unauthorized().description):
    """
    Raise if the user is not authorized to access a resource.

    401 Unauthorized
    """
    response = jsonify({'error': error, 'message': message})
    response.status_code = 401
    return response
