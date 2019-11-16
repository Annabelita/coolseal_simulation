# Voraussetzungen

* Python 3.6 oder höher
* Pycharm IDEA
* pip install pygame --upgrade (In der Konsole oder bei Windows im Anaconda prompt)
* pip install numpy --upgrade (In der Konsole oder bei Windows im Anaconda prompt)
* Weitere notwendige Packages: matplotlib, reportlab

# Projektinstallation

* Projekt aus Gitlab pullen (Über die Konsole oder direkt in Pycharm)

# Benutzung

* Pycharm starten
* Zum Ausführen der Simulation muss __main.py__ (im src Ordner) ausgeführt werden.
* Um verschiedene Simulationen/Optionen auszuprobieren können in __settings.py__ unter dem Punkt __Simulation Options__ verschiedene Parameter gesetzt werden (Beschreibung in settings.py vorhanden)
* Während die Simulation arbeitet wird die Datei __log.txt__ mit logs gefüllt.
* Nach Abschluss der Simulation wird eine PDF mit einer Zusammenfassung aller wichtigen logs und einem plot generiert.
* Zum Beenden der Simulation kann der Knopf __Escape (ESC)__ gedrückt werden oder das Fenster oben rechts geschlossen werden.
* Zum Pausieren der Simulation kann der Knopf __Space/Spacebar/Leertaste__ gedrückt werden, erneutes Drücken entfernt die Pause.
* Um Häuser während der Simulation zu erstellen, muss ein Feld ausgewählt werden (Maus zum Feld navigieren) und die linke Maustaste gedrückt werden (1 Mal).

# Änderung der Simulationsumgebung

* Um das Areal der Simulation zu ändern muss die __area.txt__ Datei verändert werden.
* Das Gebiet ist auf 34x26 Felder begrent (Angepasst an eine Fenstergröße von 1024x768 pixel).
* Das sichtbare Gebiet ist auf 32x24 Felder begrenzt, wobei am Rand jeweils Häuser/Startpositionen platziert sind um die Agenten im sichtbaren Gebiet zu halten.
* Ein __H__ repräsentiert ein Haus (Blockade für Agenten).
* Ein __A__ repräsentiert eine Startposition für Agenten (pro Startposition werden ANT_AMOUNT (siehe settings.py) viele Agenten erzeugt).
* Ein __E__ repräsentiert eine schwarze Straße.
* __Alle anderen Symbole erzeugen kein valides Areal.__


# Log Dateien

* Voraussetzungen: Die Simulation darf nicht manuell abgebrochen werden, da es ansonsten zur Fehlern (Endlosschleifen) bei der Auswertung kommen kann
* Nach Beenden der zuvor definierten Simulationsdurchläufe, wird automatisch die log.txt Datei ausgewertet.
* Die automatische Auswertung wird als PDF Datei im Ordner src/Results gespeichert.
* Jede valide log.txt endet mit einer Zeile in der "ENDE" steht. 

# Videos
* Es stehen mehrere Videos für die verschiedenen Algorithmen im Ordner __videos__ zur Verfügung.

### log.txt
Dokumentiert ...
* ... Startparameter: Explorations-Algorithmus, Anzahl der Agenten
* ... prozentualen Anteil der bereits gefärbten Fläche / pro 10 Zeitschritte
* ... wenn eine Agent stirbt & Anzahl der verbleibenden Agenten
* ... nach Simulations-Ende: Fläche komplett gefärbt (ja/nein). Dauer in Sekunden. 

### Automatische Ausertung (PDF)
Dokumentiert ...
* ... Aggregation der maximalen Schrittanzahl & prozentuale Färbungsfläche pro Simulation
* ... Ausgabe der maximalen Färbungsfläche und benötigter Schritte des besten Pfads
* ... durchschnittliche Schrittanzahl & prozentuale Färbungsfläche aller Simulationen
* ... einen Plot inklusive dem besten Pfad (Definition nach unserem Paper)
* 


# Ordnerstruktur
* alle log.txt Dateien für verschiedene, beispielhafte Konfiguration liegen im Order src/Analysis/logFiles
* alle aus den log.txt Daten erzeuten Plots liegen im Ordner src/Analysis/Plots
* alle ausgewerteten PDFs liegen im Order src/Results
* __Beim jedem Start der Simulation wird die log.txt und log.pdf überschrieben. Sollen die Auswertungen gespeichert werden, müssen diese
beiden Datei vor dem erneuten Starten umbenannt werden!__
* Die Dateinamen wurden nach folgenden Schema erstellt: ExplorationsAlgorithmus-AnzahlAgenten-Startposition(en) 
* Startpositionen: _or = oben rechts, ul = unten links, ol = oben links, or = oben rechts_
* Beispiel: SimpleWalk-1-or = Algorithmus SimpleWalk, 1 Agent, Startposition or
