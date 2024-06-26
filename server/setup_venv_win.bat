@echo off

REM The directory where the virtual environment will be created, inside the server directory
SET VENV_DIR=venv

REM The requirements file inside the server directory
SET REQUIREMENTS_FILE=requirements.txt

REM Check if python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python.
    exit /b 1
)

REM check if the working directory name is server
FOR %%I IN (.) DO SET CURRENT_DIR_NAME=%%~nxI
IF NOT "%CURRENT_DIR_NAME%" == "server" (
    echo Please run this script from the server directory.
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
