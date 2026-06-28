@echo off
REM opencode config export launcher (Windows)
REM Double-click this file to create a snapshot in snapshots\

cd /d "%~dp0"
echo Running opencode export...
echo.

python export.py
set RC=%errorlevel%

REM 9009 = "command not found" on Windows. Try the py launcher as a fallback.
if %RC%==9009 (
    echo Python not found as "python", trying "py" launcher...
    echo.
    py export.py
    set RC=%errorlevel%
)

if %RC%==9009 (
    echo.
    echo ERROR: Python is not installed or not on PATH.
    echo Install from https://python.org and rerun this file.
)

echo.
pause
