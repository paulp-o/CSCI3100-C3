@echo off

REM The directory where the virtual environment will be created, inside the server directory
SET VENV_DIR=server\venv

REM The requirements file inside the server directory
SET REQUIREMENTS_FILE=server\requirements.txt

REM Check if python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python.
    exit /b 1
)

REM Create virtual environment
IF NOT EXIST "%VENV_DIR%" (
    python -m venv "%VENV_DIR%"
)

REM Activate the virtual environment
CALL "%VENV_DIR%\Scripts\activate.bat"

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
IF EXIST "%REQUIREMENTS_FILE%" (
    pip install -r "%REQUIREMENTS_FILE%"
) ELSE (
    echo No requirements.txt found. Skipping dependency installation.
)

echo Setup complete. Use "%VENV_DIR%\Scripts\activate.bat" to activate the virtual environment.
