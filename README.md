demo-cookie-cutter
==================

A template for flask applications using [cookiecutter](https://github.com/audreyr/cookiecutter). This cookie cutter template has been very heavily influenced by [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)

####Prerequisites

1. Python (2 or 3)


####How to use it

Install cookiecutter (in it's own virtualenv would be a smashing idea)
```
mkvirtualenv cookiecutter
pip install cookiecutter
```

then run:

```
cookiecutter https://github.com/openregister/demo-cookiecutter.git
```

You will be prompted for the name of your application. Don't use any kebab-case names and that would result in an invalid python module name. Use single words or snake case, e.g. schoolfinder or school_finder.

The cookiecutter will create a directory for your app with the name you answered and in there you will find a simple skeleton app with a base govuk template and stylesheets. The rest is up to you.


####What happens next

deactivate cookiecutter virtual env, cd into the newly create directory for the application.

Create a virtualenv for your *newly* created app
```
mkvirtualenv --python=/path/to/required/python/version [appname]
```

Install python requirements.
```
pip install -r requirements/dev.txt
```

Once that this all done you can:
```
source environment.sh
python manage.py server
```
and have a look at http://localhost:8000


#### License
MIT
