from flask_admin import Admin
from src.server.config import routes
from flask_adminlte3 import AdminLTE3
import sys

admin = Admin()

def init_app(app):
   """
       Instanciate the Flask-Admin module

   @param app: flask application
   @return: Flask-Admin service
   """


   # Create admin
   global admin
   admin = Admin(
      app,
      template_mode='bootstrap4',
   )
   # AdminLTE3(app)


   for prefix in routes.ROUTES:
      if prefix == 'admin':
         session = 'admin'
         module = 'src.server.handlers.'
         for route in routes.ROUTES[session]:
            endpoint = route.get('endpoint')
            function = route.get('function')
            __import__(module + endpoint, fromlist=[''])

            view_function = getattr(sys.modules[module + endpoint], function)

            admin.add_view(view_function())



