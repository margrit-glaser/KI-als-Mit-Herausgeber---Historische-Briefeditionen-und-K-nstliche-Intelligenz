# Goethe, Tagebuch Juli 1823

Dieses Verzeichnis enthält die Daten für die Übung **„Vom Druck zur digitalen Edition: Apparat und Register“** im Seminar „KI als Mit-Herausgeber?“. Die Arbeitsaufträge finden Sie im Dokument [Ablauf und Aufgaben](Ablauf_und_Aufgaben.md).

## Die Einträge

Im Juli 1823 hält sich Goethe zur Kur in Marienbad auf. Die 31 Tageseinträge vom 1. bis 31. Juli verzeichnen Besuche, Begegnungen mit Kurgästen, Ausflüge, Wetterbeobachtungen, geologische Studien und abgehende Briefe. Die Einträge sind überwiegend von Schreiberhand; Goethe hat sie teilweise eigenhändig korrigiert und ergänzt.

## Die Datei

[Tagebuch_Juli_1823.xml](Tagebuch_Juli_1823.xml) ist ein Ausschnitt aus einer TEI/XML-Datei, die **automatisch aus den Druckdaten** der historisch-kritischen Ausgabe der Tagebücher (Band 9, 1823–1824) konvertiert wurde. Sie entspricht noch **nicht** den Konventionen der digitalen Edition der Tagebücher in den PROPYLÄEN.

Typische Merkmale der Konvertierung:

- **Kein Metadatenkopf:** Der `teiHeader` enthält nur Platzhalter („Title“, „Publication Information“).
- **Metadaten pro Eintrag** stehen in `<note type="metadaten">` mit Übernachtungsort (`placeName` mit so:fie-Schlüssel `SNDB…`) und Datum.
- **Zeilen** sind mit `lb` und einer ID gezählt, die Seite und Zeile der Druckvorlage wiedergibt, z. B. `GT09_1_84_22` = Seite 84, Zeile 22.
- **Textkritischer Apparat:** Korrekturen, Ergänzungen, Streichungen und Schreiberwechsel stehen nicht im Text, sondern am Ende der Datei in `<div type="apparat">`. Im Text verweist ein `<ptr target="#…"/>` auf den zugehörigen Eintrag `<app n="…">`. Die Apparateinträge verwenden die Siglen und Kurzformen der Druckausgabe (etwa `>`, `→`, `erg`, `get:`, `G`, `Jo`).
- **Expeditionen** (Notizen zu abgehender Post) sind nur durch Kommentare `<!-- exped start-->` und `<!-- exped end-->` markiert.
- **Arbeitskommentare** aus der Konvertierung (etwa `<!--a5-2-->` oder `<!-- Platzierung rdg/ptr prüfen -->`) sind stehen geblieben.

Der Ausschnitt enthält 31 Tageseinträge und 103 Apparateinträge. Einträge anderer Monate, Gästelisten und Büchervermehrungslisten wurden entfernt.

### Beispiel: Apparatverweis

```xml
<!-- im Text -->
<lb xml:id="GT09_1_84_22"/>suchten mich Präf. Steinhäuser von Pilsen.<ptr target="#223_84,22"/> Kriegsrath<ptr target="#224_84,22"/> Schulz

<!-- im Apparat am Dateiende -->
<app n="224_84,22" ana="GT09_1_84_22">
  <rdg>Kriegrath <note type="editor">&gt;</note> Kriegsrath <note type="editor">G</note></rdg>
</app>
```

## Digitalisate

Jeder Tageseintrag hat in den PROPYLÄEN eine eigene Seite, die über die ID des Eintrags aufgerufen werden kann. Die ID steht in der XML-Datei am Eintrag (`xml:id="GT09_0183"`); die Adresse lautet `https://goethe-biographica.de/id/GT09_0183`. Dort können Sie Korrekturen, Ergänzungen, Streichungen und Schreiberwechsel am Digitalisat prüfen.

Einträge Juli 1823: [1.](https://goethe-biographica.de/id/GT09_0183) · [2.](https://goethe-biographica.de/id/GT09_0184) · [3.](https://goethe-biographica.de/id/GT09_0185) · [4.](https://goethe-biographica.de/id/GT09_0186) · [5.](https://goethe-biographica.de/id/GT09_0187) · [6.](https://goethe-biographica.de/id/GT09_0188) · [7.](https://goethe-biographica.de/id/GT09_0189) · [8.](https://goethe-biographica.de/id/GT09_0190) · [9.](https://goethe-biographica.de/id/GT09_0191) · [10.](https://goethe-biographica.de/id/GT09_0192) · [11.](https://goethe-biographica.de/id/GT09_0193) · [12.](https://goethe-biographica.de/id/GT09_0194) · [13.](https://goethe-biographica.de/id/GT09_0195) · [14.](https://goethe-biographica.de/id/GT09_0196) · [15.](https://goethe-biographica.de/id/GT09_0197) · [16.](https://goethe-biographica.de/id/GT09_0198) · [17.](https://goethe-biographica.de/id/GT09_0199) · [18.](https://goethe-biographica.de/id/GT09_0200) · [19.](https://goethe-biographica.de/id/GT09_0201) · [20.](https://goethe-biographica.de/id/GT09_0202) · [21.](https://goethe-biographica.de/id/GT09_0203) · [22.](https://goethe-biographica.de/id/GT09_0204) · [23.](https://goethe-biographica.de/id/GT09_0205) · [24.](https://goethe-biographica.de/id/GT09_0206) · [25.](https://goethe-biographica.de/id/GT09_0207) · [26.](https://goethe-biographica.de/id/GT09_0208) · [27.](https://goethe-biographica.de/id/GT09_0209) · [28.](https://goethe-biographica.de/id/GT09_0210) · [29.](https://goethe-biographica.de/id/GT09_0211) · [30.](https://goethe-biographica.de/id/GT09_0212) · [31.](https://goethe-biographica.de/id/GT09_0213)

Eine Übersicht bieten die [Digitalisate des Tagebuchs 1823](https://goethe-biographica.de/recherche/tagebuecher/1823-1824/digitalisate-einzeltagebuecher/tagebuch-1823.html). Beachten Sie die dort angegebenen Nutzungsbedingungen.

## Druckausgabe

Als Hilfsmittel stehen Ihnen die beiden PDF-Dateien der Druckausgabe (Band 9) zur Verfügung. Sie werden in der Sitzung bereitgestellt und sind nicht Teil dieses Repositorys. Dort finden Sie den gedruckten Text, den Apparat, die Erläuterung der Siglen und Zeichen sowie den Kommentar.

## Hilfsmittel des Goethe- und Schiller-Archivs

Übersicht: [Recherche im Goethe- und Schiller-Archiv](https://www.klassik-stiftung.de/goethe-und-schiller-archiv/recherche/)

| Hilfsmittel | Nutzen für die Übung |
| --- | --- |
| [so:fie – Sammlungen online](https://ores.klassik-stiftung.de/ords/f?p=900) | Personen, Körperschaften und Orte mit Normdaten der Klassik Stiftung |
| [Briefe von Goethe](https://ores.klassik-stiftung.de/ords/f?p=402) | Verzeichnis der überlieferten Briefe Goethes mit Standorten der Handschriften |
| [Briefe an Goethe](https://ores.klassik-stiftung.de/ords/f?p=403) | Regestausgabe der Briefe an Goethe (derzeit bis 1822) |
| [Briefe an Goethe: Biographische Informationen](https://ores.klassik-stiftung.de/ords/f?p=403:600) | Kurzbiographien zu rund 16.400 Personen |
| [Archivdatenbank](https://ores.klassik-stiftung.de/ords/f?p=401) | Recherche in den Beständen des Goethe- und Schiller-Archivs |
| [PROPYLÄEN](https://goethe-biographica.de/) | Briefe, Tagebücher und Begegnungen Goethes, kommentiert und erschlossen |
| [Goethe-Gedichte](https://ores.klassik-stiftung.de/ords/f?p=405) | Handschriftenverzeichnis der Gedichte Goethes |

Für Personen und Orte außerhalb dieser Datenbanken können Sie die [GND](https://explore.gnd.network/) nutzen.

## Nachnutzung

Die Daten stammen aus dem Projekt *PROPYLÄEN. Forschungsplattform zu Goethes Biographica* (Klassik Stiftung Weimar / Goethe- und Schiller-Archiv, Sächsische Akademie der Wissenschaften zu Leipzig, Akademie der Wissenschaften und der Literatur Mainz). Die XML-Datei ist ein unveröffentlichter Arbeitsstand. Sie wird ausschließlich für die Lehre im Seminar bereitgestellt.
