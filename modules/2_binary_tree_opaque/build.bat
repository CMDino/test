@echo off
cls

if not defined MAIN_DIR (set MAIN_DIR=C:\Users\bonaffino\Desktop\repo)
set EXE_NAME=binary_tree

rem /////////////////////////////////

mingw32-make.exe clean && mingw32-make.exe

pause
echo.
echo.
echo.