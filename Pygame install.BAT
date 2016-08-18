@echo off
set upath="C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python35\Scripts"
cd %upath%
dir 
echo  "this should be the contents of the address bar:"
echo  %upath%
start explorer.exe %upath%
PAUSE
pip3 install pygame-1.9.2a0-cp35-none-win32.whl
PAUSE