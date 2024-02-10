
# Snake Game

Ein klassisches Snake-Spiel, implementiert in Python mit der PyQt-Bibliothek. Erlebe das nostalgische Gefühl, Snake zu spielen, mit zusätzlichen modernen Verbesserungen, einschließlich eines Autopilot-Modus.

## Inhaltsverzeichnis

- [Snake Game](#snake-game)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Überblick](#überblick)
  - [Features](#features)
  - [Installation](#installation)
    - [Voraussetzungen](#voraussetzungen)
    - [Installationsanweisungen](#installationsanweisungen)
  - [Spielstart](#spielstart)
  - [Spielanleitung](#spielanleitung)
  - [Technische Besonderheiten](#technische-besonderheiten)
  - [Entwickler-Tipps](#entwickler-tipps)
  - [Mitwirken](#mitwirken)

## Überblick

Dieses Spiel ist eine moderne Umsetzung des klassischen Snake-Spiels mit erweiterten Funktionen und einer verbesserten Benutzeroberfläche, entwickelt mit Python und der PyQt5-Bibliothek. Es bietet nicht nur die Möglichkeit, das nostalgische Spiel in einer modernen Umgebung zu genießen, sondern integriert auch innovative Spielmechaniken und technische Lösungen.

## Features

- **Klassisches Snake-Gameplay**: Navigiere die Schlange durch das Spielfeld, um Nahrung zu konsumieren und wachse in der Länge.
- **Quadtree-Kollisionserkennung**: Ein fortschrittliches System zur Erkennung von Kollisionen, das die Spielperformance verbessert und eine flüssige Spielerfahrung gewährleistet.
- **Autopilot-Modus**: Ein spezieller Modus, der es der Schlange ermöglicht, autonom zu navigieren und Nahrung zu konsumieren.
- **Anpassbare Spielparameter**: Spieler können verschiedene Einstellungen wie die Geschwindigkeit der Schlange und die Spielgröße anpassen.

## Installation

### Voraussetzungen

- Python 3.6 oder höher
- PyQt5

### Installationsanweisungen

1. Klone das Repository oder lade den Quellcode herunter.
2. Installiere die erforderlichen Pakete mit `pip install -r requirements.txt`.
3. Starte das Spiel mit `python main.py`.

## Spielstart

Um das Spiel zu starten, führe das Skript `main.py` aus dem Hauptverzeichnis aus. Das Spiel wird sofort gestartet, und du kannst direkt mit dem Spielen beginnen.

## Spielanleitung

- **Bewegung**: Nutze die Pfeiltasten auf deiner Tastatur, um die Richtung der Schlange zu steuern.
- **Ziel**: Versuche, so viel Nahrung wie möglich zu konsumieren, um die Länge der Schlange zu erhöhen. Vermeide die Kollision mit der Schlange selbst oder den Wänden.

## Technische Besonderheiten

- **Quadtree-Datenstruktur**: Diese Datenstruktur wird für die effiziente Kollisionserkennung zwischen der Schlange und der Nahrung sowie zwischen der Schlange und den Wänden verwendet.

## Entwickler-Tipps

- Experimentiere mit den Einstellungen, um verschiedene Spielmodi zu entdecken.
- Der Quellcode ist offen für Anpassungen. Fühle dich frei, eigene Features hinzuzufügen oder das Spielverhalten anzupassen.

## Mitwirken

Interessierte Entwickler sind herzlich eingeladen, zum Projekt beizutragen. Ob es sich um Fehlerbehebungen, neue Features oder Verbesserungen handelt, jeder Beitrag ist willkommen.
