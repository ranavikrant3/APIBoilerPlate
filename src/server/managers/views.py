import sys
from flask.blueprints import Blueprint
from src.server.config import routes
from src.server.views import restful


def init_app(app):

    # https://exploreflask.com/en/latest/blueprints.html
    """
    Add a Flask route.

    :param str endpoint: The endpoint name.
    :param str rule: The endpoint url.
    :param view_func: The endpoint func
    :param str method: The http method.
    """

    for prefix in routes.ROUTES:

        if prefix != 'admin':
            version = prefix
            blueprint = Blueprint(version, __name__)

            module = 'src.server.controllers.%s.' % version

            for route in routes.ROUTES[version]:
                endpoint = route.get('endpoint')
                function = route.get('function')
                method = route.get('method')
                rule = route.get('rule')
                opts = route.get('opts', {})
                __import__(module + endpoint, fromlist=[''])
                view_function = restful.restful(**opts)(getattr(sys.modules[module + endpoint], function))

                blueprint.add_url_rule(
                    rule,
                    endpoint=endpoint + ' ' + function,
                    view_func=view_function,
                    methods=method,
                    strict_slashes=False
                )
            app.register_blueprint(blueprint, url_prefix='/v1')

