# Vom Druck zur digitalen Edition: Apparat und Register

In dieser Übung arbeiten Sie in Gruppen mit Goethes Tagebucheinträgen vom Juli 1823. Die [XML-Datei](Tagebuch_Juli_1823.xml) wurde automatisch aus den Druckdaten der historisch-kritischen Ausgabe erzeugt. Sie bildet das Buch ab: Der Text steht oben, der textkritische Apparat gesammelt am Ende, verbunden über Verweise. Eine digitale Edition verzeichnet Korrekturen, Ergänzungen und Streichungen dagegen in der Regel dort, wo sie im Text stehen.

Die folgenden Aufgaben sind **Vorschläge**. Sie können einzelne Schritte auswählen, die Reihenfolge ändern oder eigene Fragestellungen entwickeln. Zwei Arbeitsfelder bieten sich an, beide **mit KI-Werkzeugen Ihrer Wahl**:

- **Teil A:** den Apparat in eine Inline-Kodierung nach den Richtlinien der TEI überführen;
- **Teil B:** Personen, Orte, Werke und Briefe identifizieren und mit Normdaten und Verzeichnissen verknüpfen.

Eigene Ideen sind ausdrücklich willkommen, etwa eine Visualisierung von Goethes Begegnungen in Marienbad, eine Auswertung der Wetterbeobachtungen, ein Vergleich verschiedener KI-Werkzeuge oder ein Werkzeug, das die Konvertierung automatisiert. Stimmen Sie Ihr Vorhaben kurz mit der Seminarleitung ab.

Was für alle Wege gilt: Die KI ist Werkzeug, nicht Herausgeberin. Sie bleiben für jede Kodierung und jede Identifizierung verantwortlich, und Ihr Vorgehen sollte nachvollziehbar dokumentiert sein.

### Materialien

- [Tagebuch_Juli_1823.xml](Tagebuch_Juli_1823.xml): Ausgangsdatei; Erläuterungen dazu in der [README-Datei](README.md#die-datei)
- PDF-Dateien der Druckausgabe, Band 9 (werden in der Sitzung bereitgestellt)
- [Hilfsmittel des Goethe- und Schiller-Archivs](README.md#hilfsmittel-des-goethe--und-schiller-archivs)
- zum Vergleich: [Eintrag vom 27.2.1825 in der Kodierung der PROPYLÄEN](../Aufgaben_und_Daten_Tagebuch_Februar_1825/referenz_propylaeen/18250227_GT20058_tei.xml)
- [TEI Guidelines, Kapitel 11: Representation of Primary Sources](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html)

### Vorschlag zur Arbeitsweise

- Arbeiten Sie in einer Kopie der Datei im Ordner [ergebnisse](ergebnisse/), beispielsweise `gruppe_01.xml`.
- Führen Sie ein kurzes Protokoll, beispielsweise `gruppe_01_protokoll.md`, mit den verwendeten Werkzeugen und Modellen, Ihren Prompts und Ihren Entscheidungen: Was haben Sie übernommen, korrigiert oder verworfen, und warum?

---

## Teil A: Vom Apparat zur Inline-Kodierung

### 1. Die Datei erkunden

Ein Einstieg könnte sein, sich zunächst ohne KI einen Überblick zu verschaffen:

- Wie hängen ein `ptr` im Text und der zugehörige `app` am Dateiende zusammen (`ptr/@target`, `app/@n`, `app/@ana`)?
- Auf welche Textstelle bezieht sich ein Apparateintrag? Der Verweis steht hinter dem Wort; wo beginnt die betroffene Stelle?
- Was zeigt der Vergleich einiger Stellen mit Text und Apparat in der Druckausgabe? Ist bei der Konvertierung etwas verloren gegangen oder verschoben worden?

### 2. Die Siglen des Apparats klären

Die Apparateinträge verwenden die Zeichen und Abkürzungen der Druckausgabe; ihre Bedeutung wird dort erläutert. Hilfreich kann eine Tabelle sein, die Muster, Bedeutung und mögliche TEI-Kodierung zusammenführt, zum Beispiel:

| Muster im Apparat | Beispiel aus der Datei | Bedeutung laut Druckausgabe | TEI-Kodierung (Vorschlag) |
| --- | --- | --- | --- |
| `a > b` | `Kriegrath > Kriegsrath G` | | |
| `a → b` | `St → Roftoff` | | |
| `… erg` / `… erg G` | `Hofr. erg` | | |
| `vor … get: …` / `nach … get: …` | `vor Inspector get: Dr.` | | |
| `… bis … Jo` / `G` | `Dienstag bis was Jo` | | |
| Zusatz zu Schreibmaterial | `Sprühre > Sprühregen G mit Bleistift` | | |
| Angabe zur Position | `mit Einweisungszeichen in der linken Spalte` | | |
| Unleserliches | `<gap reason="illegible" …/>`, `<unclear>` | | |

Die Tabelle ist ein Ausgangspunkt und nicht vollständig.

### 3. Kodierungsregeln entwickeln

Für die Inline-Kodierung kommen unter anderem diese TEI-Elemente und -Attribute in Frage:

- `del`, `add`, `subst` für Streichungen, Ergänzungen und Ersetzungen;
- `add/@place` für die Position einer Ergänzung (etwa `above`, `margin`);
- `@hand` für die Hand, die eine Änderung vorgenommen hat, und `handShift` für einen Schreiberwechsel;
- `handNote` im `teiHeader` zur Beschreibung der Hände, gegebenenfalls mit `@medium`;
- `unclear` und `gap` für unsichere und unleserliche Stellen.

Fragen, die sich dabei stellen können:

- Wird bei `Kriegrath > Kriegsrath` das ganze Wort als Ersetzung kodiert oder nur der ergänzte Buchstabe?
- Was bedeutet `hand="#44155"` an den Einträgen, und wie verhält es sich zu den Siglen `Jo` und `G`? (so:fie könnte helfen.)
- Was geschieht mit Apparatnotizen, die sich nicht sinnvoll in Elemente überführen lassen?
- Wie gehen die PROPYLÄEN im [Vergleichseintrag von 1825](../Aufgaben_und_Daten_Tagebuch_Februar_1825/referenz_propylaeen/18250227_GT20058_tei.xml) vor (`subst`, `del rendition="#ow"`, `add place="across"`)?

Ihre Regeln lassen sich im `teiHeader` unter `encodingDesc/editorialDecl` festhalten.

#### Beispiel: eine mögliche Lösung

```xml
<!-- vorher -->
Besuchte mich Hofr. Rehbein und Inspector<ptr target="#220_84,14"/>
<!-- Apparat: <rdg><note type="editor">vor</note> Inspector <note type="editor">get:</note> Dr.</rdg> -->

<!-- nachher -->
Besuchte mich Hofr. Rehbein und <del>Dr.</del> Inspector
```

Ob diese Lösung dem Befund entspricht, lässt sich an der Druckausgabe prüfen.

### 4. Den Apparat mit KI überführen

Es empfiehlt sich, mit einem kleinen Ausschnitt zu beginnen, etwa den Einträgen vom 1. bis 5. Juli, und der KI Siglentabelle, Regeln und ein oder zwei gelöste Beispiele mitzugeben.

Mögliche Wege, die sich auch vergleichen lassen:

- **Direkte Umschreibung:** Die KI überführt den Ausschnitt selbst.
- **Skript:** Die KI schreibt ein Programm (etwa Python oder XSLT) für die regelmäßigen Muster; Sonderfälle bearbeiten Sie von Hand.
- **Eigener Ansatz:** etwa eine schrittweise Bearbeitung nach Apparattypen oder ein Prüfwerkzeug, das Ergebnisse gegenrechnet.

Fälle, die sich nicht lösen lassen, können stehen bleiben und mit einem XML-Kommentar gekennzeichnet werden.

### 5. Das Ergebnis prüfen

Mögliche Prüffragen:

- **Texttreue:** Entspricht der Text ohne `del`-Inhalte noch Zeichen für Zeichen der Ausgangsdatei? Ein Vergleichsskript kann helfen.
- **Vollständigkeit:** Sind alle Apparateinträge berücksichtigt? Wie viele `ptr` sind übrig?
- **Befund:** Stimmen Position und Reichweite der Kodierungen mit dem Apparat der Druckausgabe überein?
- **Gültigkeit:** Ist die Datei wohlgeformt und valide gegen das TEI-Schema?
- **KI-Fehler:** Wurde Text verändert, wurden Siglen falsch gedeutet oder Notizen erfunden?

---

## Teil B: Personen, Orte, Werke und Briefe identifizieren

### 6. Entitäten mit KI erkennen

Die KI kann in einigen Einträgen Personen, Orte und Werke erkennen und auszeichnen, etwa mit `persName`, `placeName` und `title` oder mit `rs type="person|place|work"`. Vorab lohnt es sich zu klären:

- Werden auch Umschreibungen wie „Serenissimo“ oder „I. K. H. der Großherzog“ ausgezeichnet?
- Wie werden Titel und Funktionsbezeichnungen behandelt („Hofr. Rehbein“, „Inspector Gradl“)?
- Wie werden Adjektive wie „Marienbader“ behandelt?

Beim Prüfen kann man darauf achten, ob die KI Personen übersehen, falsch zugeordnet oder Namen normalisiert hat.

### 7. Personen und Orte identifizieren

Für die Identifizierung eignen sich die [Hilfsmittel des Goethe- und Schiller-Archivs](https://www.klassik-stiftung.de/goethe-und-schiller-archiv/recherche/), insbesondere [so:fie](https://ores.klassik-stiftung.de/ords/f?p=900) und die [Biographischen Informationen zu den Briefen an Goethe](https://ores.klassik-stiftung.de/ords/f?p=403:600), außerdem die GND sowie Register und Kommentar der Druckausgabe.

Anregungen für das Vorgehen:

- KI-Vorschläge, etwa zu „Fürst Labanow Rostoff“ oder „Braun von Braunthal“, als Hypothesen behandeln und am Datensatz selbst prüfen.
- Kennungen als Schlüssel eintragen, etwa nach der Konvention der PROPYLÄEN (`key="sndb:person#…"`, `key="sndb:ort#…"`). Die vorhandenen Schlüssel wie `key="SNDB78519"` in den Metadaten bieten einen Ausgangspunkt.
- Unsichere Identifizierungen kennzeichnen, etwa mit `@cert="low"` oder einem Kommentar.
- Die Ergebnisse in einer Tabelle sammeln, etwa: Textstelle | Vorschlag der KI | geprüfte Identifizierung | Quelle/URL | Sicherheit.

### 8. Briefe identifizieren

Das Tagebuch verzeichnet abgehende und eingehende Briefe, etwa „Brief an Prof. Zelter dictirt“, „Kam ein Brief v. mei-…“ oder die Expeditionen zwischen `<!-- exped start-->` und `<!-- exped end-->`.

Mögliche Schritte:

- Erwähnungen von Briefen im Juli 1823 sammeln.
- Briefe **von** Goethe im Verzeichnis [Briefe von Goethe](https://ores.klassik-stiftung.de/ords/f?p=402) und in den [PROPYLÄEN](https://goethe-biographica.de/) suchen, mit Datum, Empfänger, Standort und Signatur.
- Briefe **an** Goethe suchen. Die [Regestausgabe Briefe an Goethe](https://ores.klassik-stiftung.de/ords/f?p=403) reicht derzeit nur bis 1822. Welche anderen Wege gibt es, etwa über die [Archivdatenbank](https://ores.klassik-stiftung.de/ords/f?p=401) oder die PROPYLÄEN?
- Festhalten, welche Briefe sich nicht eindeutig zuordnen lassen, und warum.

Für die Kodierung der Briefnotizen gibt es verschiedene Möglichkeiten, etwa `rs type="letter"` mit einem Verweis (`@ref`) auf den Datensatz, einen eigenen Abschnitt `div type="exped"` wie im [Vergleichseintrag](../Aufgaben_und_Daten_Tagebuch_Februar_1825/referenz_propylaeen/18250227_GT20058_tei.xml) oder `anchor`-Elemente des Typs „Briefausgangsnotiz“.

---

## Abschluss: Ergebnisse sichern und reflektieren

Zum Abschluss bietet sich ein kurzes Fazit im Protokoll an, gleich welchen Weg Sie gewählt haben. Mögliche Fragen:

- Was ließ sich zuverlässig mit KI bearbeiten, was nicht?
- Wo waren Druckausgabe und Datenbanken unverzichtbar?
- Welche Vorschläge der KI waren richtig, falsch oder nicht überprüfbar?
- Was bedeutet das für den Einsatz von KI bei der Retrodigitalisierung gedruckter Editionen?

---

### Hilfen

- [TEI Guidelines: Streichungen, Hinzufügungen, Ersetzungen](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHAD)
- [TEI Guidelines: Hände und Schreiberwechsel (`handNote`, `handShift`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDH)
- [TEI Guidelines: unsichere und unleserliche Stellen (`unclear`, `gap`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHOM)
- [TEI Guidelines: Namen und Referenzen (`rs`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-rs.html)
- [Recherche im Goethe- und Schiller-Archiv](https://www.klassik-stiftung.de/goethe-und-schiller-archiv/recherche/)
