## Preview
![preview](https://i.imgur.com/5TvKpye.png)

## Format File Supported
- XLS
- XLSX
- CSV

## OS Supported
- Windows
- Linux

## Build From Source
### Python Package Dependencies:
- PyInstaller
- PyQt5
- pandas
- sys
- os
- openpyxl

### Steps:
1. Install all dependencies using `pip3 install -r requirements.txt`
2. Convert .ui to .py `pyuic gui.ui -o gui.py`
3. Build using `pyinstaller --onefile main.py`
