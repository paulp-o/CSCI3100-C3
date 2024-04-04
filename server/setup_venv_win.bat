@echo off

SET VENV_DIR=venv
SET REQUIREMENTS_FILE=requirements.txt

REM Check if python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python.
    exit /b 1
)

REM Create virtual environment
IF NOT EXIST %VENV_DIR% (
    python -m venv %VENV_DIR%
)

REM Activate the virtual environment
CALL %VENV_DIR%\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
IF EXIST %REQUIREMENTS_FILE% (
    pip install -r %REQUIREMENTS_FILE%
) ELSE (
    echo No requirements.txt found. Skipping dependency installation.
)

echo Setup complete. Use '%VENV_DIR%\Scripts\activate' to activate the virtual environment.
