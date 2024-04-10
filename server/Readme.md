# How to setup Python environment for this project

## 1) run venv setup script

### Windows:

- run setup_venv_win.bat file by double-clicking or `setup_venv_win.bat` in cmd

### Mac:

- run `chmod +x setup_venv.sh; ./setup_venv.sh` in terminal IN 'server' DIRECTORY, NOT THE ROOT DIRECTORY!

_Important: If there are new dependencies added to the project, run the setup_venv script again to install the new dependencies._

## 2) Choose Python interpreter on VSCode

- Press `Ctrl/Command + Shift + P` and type `Python: Select Interpreter` and choose 'enter interpreter path' and select the python interpreter from the venv folder
- windows: `./venv/Scripts/python.exe`
- mac: `./venv/bin/python`

# How to setup and run Django environment for this project

## 1) create migrations and migrate

- run `python manage.py makemigrations` and `python manage.py migrate` in terminal

## 2) run Django server

- run `python manage.py runserver` in terminal
