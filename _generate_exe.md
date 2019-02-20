prepare the `version.txt` `user.ico`

run:
```
pyinstaller.exe --onefile --windowed cycle.py
pyinstaller.exe --windowed cycle.py
```


generate python UI from xxx.ui file
```
pyuic5.exe -x -o gui_cycle.py gui_cycle.ui
```
