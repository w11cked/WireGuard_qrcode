@echo off

REM Dynamisch den Ordner setzen, in dem die Batch-Datei liegt
cd /d "%~dp0"

REM Virtuelle Umgebung aktivieren
call .venv\Scripts\activate



REM Bot starten
python main.py

pause
