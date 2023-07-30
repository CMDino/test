@echo off
cls

if not defined MAIN_DIR (set MAIN_DIR=C:\Users\bonaffino\Desktop\repo)
set EXE_NAME=bit_test

rem /////////////////////////////////

mingw32-make.exe clean && mingw32-make.exe

pause
echo.
echo.
echo.
