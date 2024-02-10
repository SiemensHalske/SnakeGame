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
      - [Manuelle Installation](#manuelle-installation)
      - [Installation mit dem Installer](#installation-mit-dem-installer)
    - [Fehlerbehebung](#fehlerbehebung)
  - [Spielstart](#spielstart)
  - [Spielanleitung](#spielanleitung)
    - [Steuerung](#steuerung)
    - [Zusätzliche Steuerungsoptionen](#zusätzliche-steuerungsoptionen)
    - [Spielziel](#spielziel)
    - [Tipps](#tipps)
  - [Technische Besonderheiten](#technische-besonderheiten)
    - [Quadtree-Datenstruktur](#quadtree-datenstruktur)
    - [Autopilot und A\*-Algorithmus](#autopilot-und-a-algorithmus)
      - [Funktionsweise des Autopiloten](#funktionsweise-des-autopiloten)
      - [Technische Dokumentation](#technische-dokumentation)
    - [Abschließende Gedanken](#abschließende-gedanken)
  - [Entwickler-Tipps](#entwickler-tipps)
    - [Experimentiere mit den Einstellungen](#experimentiere-mit-den-einstellungen)
    - [Eigene Features hinzufügen](#eigene-features-hinzufügen)
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

- **A\*-Algorithmus**: Der Autopilot-Modus der Schlange beruht auf der Verwendung des A\*-Algorithmus zur Pfadfindung. Dieser Algorithmus ist ein leistungsstarker Wegfindungsalgorithmus, der es ermöglicht, den kürzesten Weg durch ein statisches Spielfeld zu berechnen. Durch die Verwendung dieses Algorithmus kann die Schlange autonom navigieren, während sie versucht, Nahrung aufzunehmen, und dabei Hindernissen ausweicht. Durch die Implementierung dieser künstlichen Intelligenz-Komponente wird das Spiel zu einer Herausforderung für Spieler, die versuchen, die Leistungen der Schlange zu übertreffen.

## Installation

Die Installation des Snake-Spiels ist einfach und unkompliziert. Du hast die Wahl zwischen einer manuellen Installation, bei der du die Kontrolle über jeden Schritt hast, und einer automatischen Installation mit einem Installer, der den Prozess für dich vereinfacht.

### Voraussetzungen

Bevor du mit der Installation beginnst, stelle sicher, dass die folgenden Voraussetzungen auf deinem System erfüllt sind:

- Python 3.6 oder höher: Das Spiel ist in Python geschrieben und benötigt mindestens Version 3.6, um ordnungsgemäß zu funktionieren.
- PyQt5: Diese Bibliothek wird für die grafische Benutzeroberfläche des Spiels verwendet. Sie muss in deiner Python-Umgebung installiert sein.

### Installationsanweisungen

#### Manuelle Installation

1. **Repository klonen oder Quellcode herunterladen**: Beginne damit, das GitHub-Repository zu klonen oder den Quellcode als ZIP-Datei herunterzuladen und auf deinem Computer zu entpacken.
2. **Abhängigkeiten installieren**: Öffne eine Kommandozeile oder ein Terminal in dem Verzeichnis, in das du den Quellcode extrahiert hast. Führe dann `pip install -r requirements.txt` aus, um alle erforderlichen Pakete zu installieren.
3. **Spiel starten**: Nach der Installation der Abhängigkeiten kannst du das Spiel starten, indem du `python main.py` im Terminal oder der Kommandozeile ausführst. Das Spiel sollte sich daraufhin öffnen und spielbereit sein.

#### Installation mit dem Installer

Wenn du einen benutzerfreundlicheren Weg bevorzugst oder das Spiel an jemanden weitergeben möchtest, der weniger vertraut mit der Kommandozeile ist, kannst du den Installer verwenden. Dieser Installer bündelt das Spiel und alle notwendigen Abhängigkeiten in einem einfach zu bedienenden Installationsprogramm.

1. **Installer herunterladen**: Lade den Installer von der bereitgestellten Quelle herunter. Dies könnte eine Webseite, ein GitHub-Release oder ein ähnlicher Ablageort sein.
2. **Installationsprozess durchführen**: Führe die heruntergeladene Installationsdatei aus und folge den Anweisungen auf dem Bildschirm. Der Installer kümmert sich um die Installation von Python und PyQt5, falls diese noch nicht auf deinem System vorhanden sind, und richtet das Spiel für dich ein.
3. **Spiel starten**: Nach Abschluss der Installation kannst du das Spiel über das Startmenü oder eine Verknüpfung auf dem Desktop starten. Keine Notwendigkeit, Kommandozeilenbefehle zu verwenden oder manuell Abhängigkeiten zu installieren.

### Fehlerbehebung

Solltest du auf Probleme während der Installation oder beim Start des Spiels stoßen, überprüfe zuerst, ob alle Voraussetzungen korrekt installiert sind. Für weitere Unterstützung kannst du die Dokumentation konsultieren oder ein Issue im GitHub-Repository des Spiels erstellen.

## Spielstart

Das Starten des Snake-Spiels kann je nach Installationsmethode variieren. Wenn du das Spiel manuell installiert hast, indem du den Quellcode heruntergeladen und die Abhängigkeiten installiert hast, kannst du das Spiel starten, indem du `main.py` im Hauptverzeichnis des Spiels ausführst. Dies kann über ein Terminal oder eine Kommandozeile geschehen, indem du zum Verzeichnis des Spiels navigierst und `python main.py` eingibst.

Für Benutzer, die das Spiel über den Installer installiert haben, wird in der Regel eine Verknüpfung auf dem Desktop oder im Startmenü erstellt, über die das Spiel mit einem einfachen Klick gestartet werden kann. Dies eliminiert die Notwendigkeit, Kommandozeilenbefehle zu verwenden.

## Spielanleitung

### Steuerung

Das Spiel bietet mehrere Optionen zur Steuerung der Schlange, um unterschiedlichen Vorlieben gerecht zu werden:

- **Pfeiltasten**: Die klassische Methode, bei der du die Pfeiltasten auf deiner Tastatur verwendest, um die Richtung der Schlange zu ändern.
- **WASD**: Alternativ kannst du die W, A, S, D Tasten für die Bewegung nach oben, links, unten bzw. rechts nutzen.
- **Ziffernblock**: Für Spieler, die den Ziffernblock bevorzugen, funktionieren die Tasten 4, 8, 5, 6 ebenfalls zur Steuerung.

### Zusätzliche Steuerungsoptionen

- **Leertaste**: Drücke die Leertaste, um das Spiel zu pausieren und fortzusetzen.
- **Q**: Aktiviere den Autopilot-Modus mit der Q-Taste. In diesem Modus übernimmt das Spiel die Kontrolle über die Schlange und navigiert autonom durch das Spielfeld.

### Spielziel

Das Hauptziel des Spiels ist es, so lange wie möglich zu überleben und dabei so viel Nahrung wie möglich zu konsumieren. Jedes Mal, wenn die Schlange Nahrung aufnimmt, wächst sie in der Länge. Dies erhöht die Herausforderung, da der Raum für die Bewegung begrenzt wird und die Wahrscheinlichkeit von Kollisionen steigt. Vermeide es, mit den Wänden des Spielfelds oder dem eigenen Schwanz der Schlange zu kollidieren, um das Spiel fortzusetzen.

### Tipps

- **Raumnutzung**: Versuche, den verfügbaren Raum effizient zu nutzen, indem du Spiralmuster oder ähnliche Strategien anwendest, um Kollisionen zu vermeiden.
- **Autopilot-Modus**: Nutze den Autopilot-Modus, um die Strategie des Spiels zu beobachten und deine eigenen Fähigkeiten zu verbessern. Beachte jedoch, dass der Autopilot nicht unfehlbar ist und das Spiel letztendlich eine Herausforderung bleiben soll.

Viel Spaß beim Spielen und dem Erreichen neuer Highscores!

## Technische Besonderheiten

Das Snake-Spiel weist mehrere technische Besonderheiten auf, die es von traditionellen Implementierungen abheben. Diese Innovationen verbessern nicht nur die Spielerfahrung, sondern bieten auch Einblicke in fortgeschrittene Programmierungskonzepte.

### Quadtree-Datenstruktur

Eine der Kernkomponenten des Spiels ist die Verwendung einer Quadtree-Datenstruktur für die effiziente Kollisionserkennung. Quadtrees sind eine Art Baumstruktur, in der jeder Knoten genau vier Kinder hat. Diese Struktur ist ideal für Spiele und Grafikanwendungen, da sie eine schnelle und effiziente Raumaufteilung und Objektlokalisierung ermöglicht. Im Kontext des Snake-Spiels wird der Quadtree genutzt, um das Spielfeld in kleinere Segmente aufzuteilen, was die Überprüfung von Kollisionen zwischen der Schlange, der Nahrung und den Wänden erheblich beschleunigt. Dadurch wird die Leistung optimiert, indem die Anzahl der notwendigen Kollisionsüberprüfungen reduziert wird, besonders wichtig, da die Schlange wächst und das Spiel komplexer wird.

### Autopilot und A\*-Algorithmus

Ein weiteres herausragendes Merkmal des Spiels ist der Autopilot-Modus, der durch die Implementierung des A*-Suchalgorithmus ermöglicht wird. Der A*-Algorithmus ist eine weit verbreitete und effiziente Technik in der Computerwissenschaft für das Finden des kürzesten Pfades durch Graphen. Im Spiel wird er verwendet, um der Schlange automatisch zu ermöglichen, den optimalen Weg zur Nahrung zu finden, ohne sich selbst zu treffen oder in die Wände zu laufen.

#### Funktionsweise des Autopiloten

- **Pfadfindung**: Der Autopilot verwendet den A\*-Algorithmus, um den kürzesten und sichersten Pfad zur nächsten Nahrung zu berechnen. Der Algorithmus berücksichtigt die aktuelle Position der Schlange, die Position der Nahrung und potenzielle Hindernisse, um einen effizienten Weg zu finden.
- **Dynamische Anpassung**: Da sich die Position der Schlange und der Nahrung ständig ändert, muss der Algorithmus dynamisch angepasst werden. Der Autopilot reevaluiert den Pfad kontinuierlich, um auf Veränderungen im Spielzustand zu reagieren.
- **Sicherheitsmechanismen**: Um Selbstkollisionen zu vermeiden, integriert der Autopilot zusätzliche Sicherheitsmechanismen, die es der Schlange ermöglichen, gefährliche Manöver zu erkennen und alternative Routen zu wählen.

#### Technische Dokumentation

Für eine tiefergehende Erklärung des A\*-Algorithmus und seiner Anwendung im Autopilot-Modus des Spiels wird auf ein separates technisches Dokument verwiesen. Dieses Dokument bietet detaillierte Einblicke in die algorithmischen Entscheidungen, die Implementierungsdetails und die Herausforderungen bei der Entwicklung des Autopilot-Modus.

### Abschließende Gedanken

Die Integration von Quadtrees für Kollisionserkennung und die Verwendung des A*-Algorithmus für den Autopilot-Modus sind Beispiele für die technischen Innovationen, die dieses Snake-Spiel auszeichnen. Diese Funktionen verbessern nicht nur die Spielqualität und Leistung, sondern bieten auch wertvolle Lernmöglichkeiten für Entwickler, die sich mit fortschrittlichen Programmierungskonzepten und Algorithmen auseinandersetzen möchten.

Es ist wichtig zu erwähnen, dass der A*-Algorithmus momentan nur testweise implementiert ist und noch nicht vollständig funktioniert. Diese vorläufige Implementierung dient als Grundlage für zukünftige Verbesserungen und Optimierungen. Entwickler, die an der Weiterentwicklung des Spiels interessiert sind, können diese Implementierung als Ausgangspunkt nutzen, um tiefergehende Kenntnisse in der Pfadfindung und algorithmischen Problemstellung zu erlangen. Die Weiterentwicklung und Feinabstimmung des A*-Algorithmus bietet eine ausgezeichnete Gelegenheit, praktische Erfahrungen mit dieser leistungsstarken Suchtechnik zu sammeln und gleichzeitig die Spielmechanik und -dynamik zu verbessern.

## Entwickler-Tipps

### Experimentiere mit den Einstellungen

1. **Ändern der Spielgeschwindigkeit**:
   Die Geschwindigkeit der Schlange ist ein wesentlicher Aspekt, der das Spielgefühl signifikant beeinflussen kann. Eine höhere Geschwindigkeit macht das Spiel herausfordernder, während eine niedrigere Geschwindigkeit es einfacher macht, aber möglicherweise weniger spannend. Die `adjustSpeed` Methode passt die Spielgeschwindigkeit dynamisch an, basierend auf der Länge der Schlange. Dies sorgt für eine stetige Steigerung der Schwierigkeit, da die Schlange wächst und das Spiel fortschreitet.

   ```python
   # Beispiel: Anpassen der Spielgeschwindigkeit basierend auf der Schlange-Länge
   def adjustSpeed(self):
       snake_length = len(self.snake_positions)
       base_interval = 100
       speed_increase = 0.25

       new_interval = max(20, int(base_interval - (snake_length - 1) * speed_increase))
       self.timer.setInterval(new_interval)
   ```

   Dieser Codeabschnitt zeigt, wie die adjustSpeed Methode die Spielgeschwindigkeit basierend auf der Länge der Schlange anpasst. Die Geschwindigkeit erhöht sich, indem das Timer-Intervall verringert wird, je länger die Schlange wird. Die Verwendung dieser Methode in deinem Spiel ermöglicht es, dass das Spiel mit zunehmender Länge der Schlange schwieriger und anspruchsvoller wird, wodurch ein dynamischeres und herausfordernderes Spielerlebnis entsteht.

   Die adjustSpeed Methode ist ein ausgezeichnetes Beispiel dafür, wie du das Spielverhalten anpassen kannst, um verschiedene Spielmodi und Schwierigkeitsgrade zu entdecken. Experimentiere mit den Werten für base_interval und speed_increase, um das optimale Gleichgewicht zwischen Spielbarkeit und Herausforderung zu finden.

2. **Anpassen der Größe des Spielfelds**:
   Ein größeres oder kleineres Spielfeld kann die Strategie und Spielbarkeit erheblich beeinflussen. Ein größeres Feld bietet mehr Raum, erhöht aber auch die Zeit, die benötigt wird, um Nahrung zu finden.

   ```python
   window = SnakeGame(
           screen_width=800,
           screen_height=800
       )
   ```

### Eigene Features hinzufügen

1. **Einführung neuer Nahrungsarten**: Du könntest verschiedene Arten von Nahrung einführen, die unterschiedliche Effekte auf die Schlange haben, wie z.B. eine temporäre Geschwindigkeitserhöhung oder eine Verkürzung der Schlange.

   ```python
   # Beispiel: Hinzufügen einer neuen Nahrungsart
   class SpecialFood(Food):
       def __init__(self, ...):
           super().__init__(...)
           self.effect = "speed_boost"  # Möglicher Effekt: Geschwindigkeitserhöhung

       def apply_effect(self, snake):
           if self.effect == "speed_boost":
               snake.speed += 5  # Temporäre Geschwindigkeitserhöhung
   ```

2. **Implementierung von Leveln oder Modi**: Du könntest das Spiel um verschiedene Schwierigkeitsgrade oder Modi erweitern, wie z.B. einen Zeitmodus, in dem der Spieler so viele Punkte wie möglich in einer festgelegten Zeit sammeln muss.

   ```python
   # Beispiel: Einführung eines Zeitmodus
   class TimeMode(GameMode):
       def __init__(self, time_limit):
           self.time_limit = time_limit  # Zeitlimit in Sekunden
           # Initialisiere den Modus ...

       def update(self, ...):
           # Aktualisiere den Spielstatus basierend auf dem verbleibenden Zeit
   ```

## Mitwirken

Interessierte Entwickler sind herzlich eingeladen, zum Projekt beizutragen. Ob es sich um Fehlerbehebungen, neue Features oder Verbesserungen handelt, jeder Beitrag ist willkommen.

## Kontaktdetails

Für Fragen, Anregungen oder wenn du einfach nur in Kontakt treten möchtest, findest du hier einige Möglichkeiten, wie du das Team hinter dem Snake Game erreichen kannst:

- **E-Mail**: [siemenshendrik1@gmail.com](mailto:siemenshendrik1@gmail.com)
- **GitHub**: [https://github.com/SiemensHalske](https://github.com/SiemensHalske)

Ich freue mich, von dir zu hören, und ich hoffe, dass du Spaß hast, das Snake Game zu spielen.
