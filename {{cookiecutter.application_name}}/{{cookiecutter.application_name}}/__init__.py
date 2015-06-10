import os
from {{cookiecutter.application_name}}.factory import create_app
app = create_app(os.environ['SETTINGS'])
