@echo off
cd /d "%~dp0"
echo =========================================================================
echo  AI POWERED THREAT DETECTION SYSTEM - AUTOMATIC LAUNCHER
echo =========================================================================
echo.
echo [Step 1/2] Installing required Python packages...
python -m pip install -r requirements.txt
echo.
echo [Step 2/2] Starting the AI Threat Detection Server...
echo Open your browser and go to: http://127.0.0.1:5000
echo.
python main.py
pause
