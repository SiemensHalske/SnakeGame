@echo off
SETLOCAL EnableDelayedExpansion

REM Erstelle die Hauptordner
mkdir "src"
mkdir "src\game"
mkdir "assets"
mkdir "assets\images"
mkdir "assets\sounds"
mkdir "versions"
mkdir "docs"
mkdir "tests"
mkdir "versions\v1.0"
mkdir "versions\v1.0\src"
mkdir "versions\v2.0"
mkdir "versions\v2.0\src"

REM Erstelle die __init__.py Dateien
echo # Dies ist eine init-Datei > "src\__init__.py"
echo # Dies ist eine init-Datei > "src\game\__init__.py"
echo # Dies ist eine init-Datei > "tests\__init__.py"

REM Erstelle die Hauptdateien
echo # Haupt-Skript, um das Spiel zu starten > "src\main.py"
echo # Spiel-Engine > "src\game\engine.py"
echo # Spielmodelle > "src\game\models.py"
echo # Testspiellogik > "tests\test_game_logic.py"

REM Erstelle eine leere requirements.txt Datei
type nul > "requirements.txt"

REM Erstelle README.md und LICENSE Dateien
echo README Inhalte > "docs\README.md"
echo GPL 3.0 Lizenztext > "docs\LICENSE"

echo Struktur und Dateien wurden erfolgreich erstellt.
