## Usage

```bash
# Run script
python LAS_Handler.py


# Compiled with Pyinstaller

# Windows
pyinstaller --onefile --windowed LAS_Handler.py
pyinstaller --onefile --windowed --add-data 'src;src' LAS_Handler.py
pyinstaller --add-data 'src;src' -i ".\src\las.ico" --onefile --windowed LAS_Handler.py
```

- Version: 1.0.0
- License: MIT
- Author: Mero2online
