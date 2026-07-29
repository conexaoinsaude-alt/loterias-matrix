@echo off

title LOTERIAS MATRIX PLATFORM

cd /d "%~dp0"

echo.
echo ===========================================
echo      INICIANDO LOTERIAS MATRIX PLATFORM
echo ===========================================
echo.

start "" cmd /c "uvicorn backend.main:app --host 127.0.0.1 --port 8000"

echo Aguarde iniciando servidor...
timeout /t 5 /nobreak >nul

start "" http://127.0.0.1:5500

exit