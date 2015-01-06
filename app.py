import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
import webapp2

# Must set this env var *before* importing any part of Django.
os.environ['DJANGO_SETTINGS_MODULE'] = 'algby.settings'


# import django.core.handlers.wsgi
# app = django.core.handlers.wsgi.WSGIHandler()


# #########################################################

# # Google App Hosting imports.
# from google.appengine.ext.webapp import util


# # Import the part of Django that we use here.
# import django.core.handlers.wsgi

# def main():
  # # Create a Django application for WSGI.
  # application = django.core.handlers.wsgi.WSGIHandler()

  # # Run the WSGI CGI handler with that application.
  # util.run_wsgi_app(application)

# if __name__ == '__main__':
  # main()


# #########################################################


from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
