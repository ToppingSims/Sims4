@echo off
echo ================================================
echo   Laver Sims4 Backup .exe med ikon
echo ================================================
echo.

REM Tjek om Python virker
python --version >nul 2>&1
if errorlevel 1 (
    echo FEJL: Python blev ikke fundet
    echo Kør denne fil fra PowerShell eller Command Prompt i stedet.
    pause
    exit
)

echo Python fundet!
python --version
echo.

echo Installerer PyInstaller (hvis ikke allerede installeret)...
python -m pip install pyinstaller
echo.

echo Laver .exe fil med ikon...
python -m PyInstaller --onefile --windowed --icon="ToppingSimsBackup.ico" --add-data "ToppingSimsBackup.ico;." --name="Sims4Backup" sims4_backup.py
echo.

if exist "dist\Sims4Backup.exe" (
    echo ================================================
    echo   SUCCES! .exe fil er oprettet med ikon
    echo ================================================
    echo.
    echo Din færdige .exe fil ligger her:
    echo dist\Sims4Backup.exe
    echo.
    echo Flyt denne fil til hvor du vil have den.
    echo Ikonet er nu en del af .exe filen!
    echo.
) else (
    echo ================================================
    echo   FEJL: .exe fil blev ikke oprettet
    echo ================================================
    echo.
)

pause
