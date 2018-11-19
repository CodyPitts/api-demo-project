This project uses Python 3, so make sure you have Python 3 and pip installed (you want the version of pip from Python 3, which might mean using the command ```pip3``` instead of ```pip```). I used homebrew to install Python 3 (which should come with pip), but there are multiple ways you can choose to manage this.

```
pip install virtualenv
pip install virtualenvwrapper
```

Virtualenv lets you create isolated Python environments for dependency/version management, and virtualenvwrapper extends virtualenv with additional functionality and more user-friendly commands.

Add the following to your .bash_profile:
```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

This sets where your virtualenvs live, sets which version of Python to use by default for your virtualenvs, and points to where the script from the virtualenvwrapper package is. For more details, check the [virtualenv](https://virtualenv.pypa.io/en/stable/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) documentation.

Now run ```mkvirtualenv <name-your-env>```, and you should see the name of your newly created virtualenv prepended to your command line. To activate a virtualenv, run ```workon <your-env-here>```. To deactivate it, simply run ```deactivate```.

With your virtualenv active, navigate to the directory with requirements.txt and run ```pip install -r requirements.txt``` to install the listed packages. At any time, you can run ```pip freeze``` to see the packages you have installed in your current environment.

The manage.py file allows you to run python commands within the context of your project. In the directory containing your manage.py file, run ```python manage.py migrate``` to synchronize your database, and then ```python manage.py createsuperuser``` to make yourself an account. You can run ```python manage.py runserver``` at any point to spin up a local version of your site.

To run the CSV importer, use the command ```python manage.py csv_import --path=[PATH/TO/FILE]```. I've added a test CSV for convenience in the datasource app.