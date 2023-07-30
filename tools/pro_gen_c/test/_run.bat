@echo off
cls

if not defined MAIN_DIR (set MAIN_DIR=C:\Users\bonaffino\Desktop\repo)
set EXE_NAME=test

rem /////////////////////////////////

if exist "%MAIN_DIR%\build\bin\%EXE_NAME%.exe" (
  "%MAIN_DIR%\build\bin\%EXE_NAME%.exe"
  echo.
  echo.
  echo ****************************
  echo ****************************
  echo *** C application ended. ***
  echo ****************************
  echo ****************************
  echo.
  echo.
) else (
  echo Executable not found.
)

pause
echo.
echo.
echo.
