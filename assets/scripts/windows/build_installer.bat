rem this file needs to be run in admin mode
mkdir %HOMEPATH%\installer
cd %HOMEPATH%\installer
if not exist "%ProgramFiles(x86)%\NSIS\" (
    curl -OL https://prdownloads.sourceforge.net/nsis/nsis-3.11-setup.exe?download
    nsis-3.11-setup.exe
    echo "Wait for the NSIS installer to finish, then type the enter key"
    pause
)
if not exist cpython-3.13.3+20250517-x86_64-pc-windows-msvc-install_only.tar.gz (
    curl -OL https://github.com/astral-sh/python-build-standalone/releases/download/20250517/cpython-3.13.3+20250517-x86_64-pc-windows-msvc-install_only.tar.gz
)
mkdir "%ProgramFiles(x86)%\Cayenue"
tar -xvzf cpython-3.13.3+20250517-x86_64-pc-windows-msvc-install_only.tar.gz -C "%ProgramFiles(x86)%\Cayenue"
cd "%ProgramFiles(x86)%\Cayenue"
python\python -m venv cayenue-env
cayenue-env\Scripts\pip install %HOMEPATH%\Cayenue torch==2.8.0 torchvision==0.23.0 openvino
cd %HOMEPATH%\installer
copy %HOMEPATH%\Cayenue\cayenue\resources\Cayenue.ico .
copy %HOMEPATH%\Cayenue\assets\scripts\windows\cayenue.nsi .
copy %HOMEPATH%\Cayenue\assets\scripts\windows\license.txt .
"%ProgramFiles(x86)%\NSIS\makensis" cayenue.nsi
rmdir /q /s "%ProgramFiles(x86)%\Cayenue"
cd %HOMEPATH%