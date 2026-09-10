# Von der Handschrift zur TEI/XML-Edition

## Dienstag, 10:30-12:00 Uhr eigene Lektüre und Kodierung

In dieser 90-minütigen Übung bearbeiten Sie in Zweiergruppen einen gemeinsamen Ausschnitt aus Alexander von Humboldts Brief an Karl Ludwig Willdenow vom 20. April und 5. Juni 1799. Sie erschließen die Handschrift, erstellen eine eigene TEI/XML-Datei und vergleichen Ihre Entscheidungen mit denen anderer Gruppen sowie mit der wissenschaftlichen Edition.

Ziel ist eine nachvollziehbar begründete Kodierung eines kurzen Ausschnitts. KI werden wir heute noch nicht einsetzen!

## Materialien und Textumfang

- [Digitalisate im Repo](README.md#digitalisate)
- [Handschrift im Browser der SBB-PK](http://resolver.staatsbibliothek-berlin.de/SBB0001A88D00000000)
- [Lesehilfe](H0001200_Lesehilfe_Ausschnitt.txt) (Ausschnitt)
- [Rohtranskription](H0001200_Lesehilfe_Rohtranskription.txt) (Volltext)
- [XML-Vorlage](H0001200_Template.xml), die für die Übung bereitgestellt werden

Arbeiten Sie während der Lektüre stets mit dem Digitalisat. Die Lesehilfe unterstützt die Entzifferung; handschriftliche Zusätze, Streichungen und räumliche Anordnungen müssen Sie selbst am Bild erkennen.

## 1. Die Handschrift lesen

Vergleichen Sie die Lesehilfe mit dem Schriftbild. Achten Sie auf wiederkehrende Buchstabenformen, Abkürzungen, Worttrennungen und Eingriffe in den Text. Entziffern Sie die für die eigenständige Lektüre vereinbarten Stellen und notieren Sie unsichere Lesungen.

Behalten Sie die historische Orthografie und Interpunktion bei. Lösen Sie Abkürzungen zunächst nicht auf und ergänzen Sie fehlende Wörter oder Satzzeichen nicht stillschweigend. Halten Sie fest, wo eine Entscheidung am Digitalisat überprüft werden muss.

## 2. Die XML-Datei anlegen und Metadaten ausfüllen

Speichern Sie die bereitgestellte Vorlage unter einem eigenen Dateinamen im GitHub-Ordner [ergebnisse](ergebnisse\), beispielsweise `gruppe_01.xml`. Nutzen Sie dafür die [XML-Vorlage](H0001200_Template.xml) mit den Basis-Elementen innerhalb der TEI-Grundstruktur aus `<teiHeader>` und `<text><body>`.

Tragen Sie die benötigten Metadaten ein. Nutzen Sie dafür auch die Quellenangaben in der [README-Datei](README.md):

- Titel Ihrer Bearbeitung und eigene Bearbeitungsverantwortung;
- Publikationsstatus der Seminarfassung;
- Aufbewahrungsort und Signatur der Handschrift;
- Absender, Empfänger, Schreiborte und Daten des Briefes.

## 3. Den Text auszeichnen

Fügen Sie den vereinbarten Textausschnitt in den Textbereich ein. Bearbeiten Sie zunächst drei Bereiche:

1. **Textstruktur:** Absatz, Blattseite und Zeilenwechsel (`p`, `pb`, `lb`).
2. **Abkürzungen:** Kennzeichnen Sie abgekürzte Formen mit `abbr`. Auflösungen sind in diesem Arbeitsschritt nicht verlangt.
3. **Ortsnamen:** Zeichnen Sie Ortsnamen mit `placeName` aus und bewahren Sie ihre historische Schreibweise. Eine Normdatenrecherche ist nicht Teil der Übung.

Prüfen Sie anschließend handschriftliche Zusätze (`add`), soweit sie im ausgewählten Ausschnitt vorkommen. Weitere Phänomene bearbeiten Sie nach verfügbarer Zeit. Unsichere Lesungen dürfen offenbleiben und sollen dokumentiert werden; für eine unsicher gelesene Textstelle kann `unclear` verwendet werden.

## 4. Die Ergebnisse der Gruppen vergleichen

Vergleichen Sie zwei oder drei ausgewählte Stellen und erläutern Sie Ihre Entscheidungen:

- Was lässt sich am Schriftbild beobachten, und was ist bereits Interpretation?
- Beruht eine Abweichung auf einer anderen Lesung, einer anderen Kodierungsentscheidung oder einem Fehler?
- Welche Information erhält die jeweilige Auszeichnung, welche bleibt unberücksichtigt?

Dokumentieren Sie begründete Entscheidungen und/oder offene Fragen. Nutzen Sie dafür die Kommentarfunktion in XML. 

**Beispiel**

```xml

<lb> … bestimmt sind, muß ich Dich über mich selbst u mein Schiksal orientiren. Die-
<lb>ses Schiksal <!-- sollten wir hier "Schicksal" schreiben? --> ist nun in diesem Jahr wunderbar genug gewesen

```

## 5. Die wissenschaftliche Edition hinzuziehen

Öffnen Sie nun die [XML-Datei der edition humboldt digital, Version 12] ([hier im Repo](referenz_ehd/H000120.xml) oder auf der [Live-Instanz der Edition](https://edition-humboldt.de/v12/H0001200.xml), und suchen Sie die gemeinsam untersuchten Stellen auf. Vergleichen Sie Lesungen und Auszeichnungen mit Ihren Ergebnissen. Ziehen Sie bei Bedarf die [Editionsrichtlinien](https://edition-humboldt.de/richtlinien/) hinzu.

Die Edition dient als wissenschaftliche Referenz. Eine abweichende Kodierung ist nicht automatisch falsch: Entscheidend sind Quellenbefund, Editionsziel und die zugrunde gelegten Regeln. 

## 6. Ergebnisse sichern

Bewahren Sie Ihre XML-Datei und Ihr kurzes Entscheidungsprotokoll auf, beispielsweise als `gruppe_01.xml` und `gruppe_01_notizen.md`. Diese Dateien bilden den Ausgangspunkt für die zweite Sitzung zum Einsatz von KI.

## TEI-Hilfen

- [TEI Guidelines: Metadaten im Header](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html)
- [TEI Guidelines: unsichere Lesungen (`unclear`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-unclear.html)
