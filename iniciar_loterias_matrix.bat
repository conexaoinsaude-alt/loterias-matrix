@echo off
title LOTERIAS MATRIX PLATFORM

cd /d "%~dp0"

echo ============================================
echo          LOTERIAS MATRIX PLATFORM
echo ============================================
echo.

echo Iniciando a plataforma...
echo.

python app.py

echo.
echo ============================================
echo A plataforma foi encerrada.
echo Pressione qualquer tecla para sair.
echo ============================================

pause > nul