@echo off
:: oc.cmd — CMD shim for oc.ps1
:: Forwards all arguments to oc.ps1 by absolute path.
:: Usage: oc.cmd [profile] [opencode-args...]
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0oc.ps1" %*
exit /b %ERRORLEVEL%
