
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
  - [Kontaktdetails](#kontaktdetails)

## Überblick

Bei diesem Projekt handelt es sich um eine moderne Interpretation des klassischen Snake-Spiels, realisiert durch die Verwendung von Python und der umfangreichen PyQt5-Bibliothek. Die Anwendung zielt darauf ab, den nostalgischen Charme des ursprünglichen Spiels zu bewahren, während sie gleichzeitig durch die Integration moderner Programmiermethoden und Benutzeroberflächen-Designs eine frische und ansprechende Spielerfahrung bietet. Das Spiel folgt den grundlegenden Regeln des traditionellen Snake-Spiels, erweitert diese jedoch um neue Elemente und Funktionen, die das Spielgeschehen bereichern und den Spieler vor neue Herausforderungen stellen.

Die Implementierung nutzt die leistungsstarken Komponenten von PyQt5, insbesondere `QGraphicsView` und `QGraphicsScene`, um ein dynamisches und interaktives Spielumfeld zu schaffen. Diese Werkzeuge ermöglichen es, komplexe Grafiken und Benutzeroberflächen mit hoher Effizienz und Flexibilität zu gestalten, was die Entwicklung eines visuell ansprechenden und reaktionsschnellen Spiels erleichtert.

## Features

- **Klassisches Snake-Gameplay**: Im Herzen des Spiels steht das zeitlose Spielprinzip von Snake. Spieler steuern eine sich kontinuierlich bewegende Schlange durch ein Spielfeld, mit dem Ziel, Punkte zu sammeln, indem sie Nahrung aufnehmen, welche zufällig auf dem Spielfeld erscheint. Jedes Mal, wenn die Schlange Nahrung konsumiert, wächst sie in der Länge. Dies erhöht die Schwierigkeit des Spiels, da die Gefahr, sich selbst oder die Wand zu treffen, mit der Länge der Schlange steigt.

- **Quadtree-Kollisionserkennung**: Eine der technischen Besonderheiten des Spiels ist die Verwendung einer Quadtree-Datenstruktur für eine effiziente Kollisionserkennung. Diese fortschrittliche Methode ermöglicht es, Kollisionen zwischen der Schlange, der Nahrung und den Wänden des Spielfelds schnell zu erkennen, indem der Raum in vier Quadranten unterteilt wird, die rekursiv in kleinere Abschnitte aufgeteilt werden können. Dies reduziert die Anzahl der notwendigen Vergleiche erheblich, was besonders bei einem größeren Spielfeld und einer längeren Schlange von Vorteil ist. Durch diese Optimierung wird sichergestellt, dass das Spiel auch unter komplexen Bedingungen flüssig und ohne Verzögerung läuft.

- **Autopilot-Modus**: Eine innovative Funktion des Spiels ist der Autopilot-Modus, der es der Schlange ermöglicht, autonom zu agieren. In diesem Modus nutzt das Spiel Algorithmen, um den Pfad der Schlange durch das Spielfeld zu bestimmen, wobei versucht wird, Nahrung zu konsumieren, ohne in Gefahr zu laufen, eine Kollision zu verursachen. Dieser Modus ist nicht nur eine interessante technische Demonstration der Möglichkeiten von Algorithmen zur Pfadfindung und Entscheidungsfindung, sondern bietet den Spielern auch die Möglichkeit, die Strategien der Schlange zu beobachten und daraus zu lernen.

- **Anpassbare Spielparameter**: Das Spiel bietet eine Vielzahl von Optionen zur Anpassung der Spielparameter, sodass Spieler das Erlebnis ihren Vorlieben anpassen können. Dazu gehören Einstellungen für die Geschwindigkeit der Schlange, die Größe des Spielfelds und möglicherweise die Häufigkeit, mit der Nahrung erscheint. Diese Flexibilität erlaubt es den Spielern, die Schwierigkeit und das Tempo des Spiels zu variieren, was für eine breite Palette von Spielerfahrungen sorgt, von entspannend bis intensiv herausfordernd.

- **A*-Algorithmus**: Der Autopilot-Modus der Schlange beruht auf der Verwendung des A*-Algorithmus zur Pfadfindung. Dieser Algorithmus ist ein leistungsstarker Wegfindungsalgorithmus, der es ermöglicht, den kürzesten Weg durch ein statisches Spielfeld zu berechnen. Durch die Verwendung dieses Algorithmus kann die Schlange autonom navigieren, während sie versucht, Nahrung aufzunehmen, und dabei Hindernissen ausweicht. Durch die Implementierung dieser künstlichen Intelligenz-Komponente wird das Spiel zu einer Herausforderung für Spieler, die versuchen, die Leistungen der Schlange zu übertreffen.

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

## Kontaktdetails

Für Fragen, Anregungen oder wenn du einfach nur in Kontakt treten möchtest, findest du hier einige Möglichkeiten, wie du das Team hinter dem Snake Game erreichen kannst:

- **E-Mail**: [siemenshendrik1@gmail.com](mailto:siemenshendrik1@gmail.com)
- **GitHub**: [https://github.com/SiemensHalske](https://github.com/SiemensHalske)

Ich freue mich, von dir zu hören, und ich hoffe, dass du Spaß hast, das Snake Game zu spielen.
