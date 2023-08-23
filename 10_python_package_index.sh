
# use pip to install package:
pip3 install requests

# upgrade pip:
pip3 install --upgrade pip

# list installed packages:
pip3 list

# install specific version
pip3 install requests==2.9.0
# install latest compatible version:
pip3 install requests==2.9.*
pip3 install requests~=2.9.0
pip3 install requests==2.*

pip3 uninstall requests


# virtual environments:
python3 -m venv env

## windows:
$env\bin\activate.bat

## mac/linux:
source env/bin/activate

## deactivate virtual environment:
deactivate

# pipenv:
pip3 install pipenv

pipenv install requests
pipenv --venv
# activate the virual environment:
pipenv shell
# deactivate:
exit




