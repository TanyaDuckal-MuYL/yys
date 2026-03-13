@echo off
pip install pywin32
pip install pynput
pip install pyside6
pip install pyautogui
pip install pyinstaller
pyinstaller -F widget.py linklist.py yys_work.py --hidden-import PySide6.QtSvg --paths  c:\users\22953\appdata\local\programs\python\python38\lib\site-packages\shiboken6.abi3.dll -w --exclude PyQt5
pause