@echo off
title OpenAI API Key Checker
color 0B

echo Installing required packages...
pip install -r requirements.txt > nul 2>&1

cls
echo Starting API Key Checker...
echo.
python check_keys.py

echo.
echo Press any key to exit...
pause > nul
