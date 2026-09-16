# Vom Tagebuch zur digitalen Edition – mit KI

In dieser Übung arbeiten Sie in Gruppen mit dem Eintrag vom 27. Februar 1825 aus Goethes Tagebuch. Anders als in der Übung zum Humboldt-Brief entstehen Transkription und TEI/XML-Auszeichnung nun **mit Hilfe von KI-Werkzeugen Ihrer Wahl**. Daraus kann, ebenfalls KI-gestützt, eine kleine statische Website als digitale Edition mit ersten Kommentaren werden.

Anders als ein Brief ist ein Tagebucheintrag knapp und listenartig. Er setzt viel Wissen über Personen, Orte und Vorgänge voraus und ist auf der Seite zweispaltig angelegt. Genau hier liegen Chancen und Risiken der KI-Unterstützung.

Die folgenden Aufgaben sind **Vorschläge**. Sie können einzelne Schritte auswählen, die Reihenfolge ändern, Schwerpunkte setzen oder eigene Fragestellungen entwickeln. Zwei Arbeitsfelder bieten sich an:

- **Teil A:** KI-gestützte Transkription und Auszeichnung;
- **Teil B:** von der XML-Datei zu einer kleinen digitalen Edition.

Eigene Ideen sind ausdrücklich willkommen, etwa ein systematischer Vergleich mehrerer KI-Werkzeuge bei der Handschriftenerkennung, eine Prompt-Sammlung für Tagebuchtexte, ein Register mit Normdaten oder eine ganz andere Präsentationsform. Stimmen Sie Ihr Vorhaben kurz mit der Seminarleitung ab.

Was für alle Wege gilt: Die KI ist Werkzeug, nicht Herausgeberin. Sie bleiben für jede Lesung, jede Auszeichnung und jede Kommentaraussage verantwortlich, und Ihr Vorgehen sollte nachvollziehbar dokumentiert sein.

### Materialien

- [Digitalisate im Repo](README.md#digitalisate): S. 55 und S. 56
- [Lesehilfe](GT20058_Lesehilfe.txt) (am besten erst zur Kontrolle nutzen)
- [XML-Vorlage](GT20058_Template.xml)
- [Referenzdatei der PROPYLÄEN](README.md#referenzdatei-der-propyläen) (am besten erst nach der eigenen Bearbeitung öffnen)

### Vorschlag zur Arbeitsweise

- Arbeiten Sie im Ordner [ergebnisse](ergebnisse/), beispielsweise mit `gruppe_01.xml`.
- Führen Sie ein kurzes Protokoll, beispielsweise `gruppe_01_protokoll.md`, mit den verwendeten Werkzeugen und Modellen, Ihren Prompts und Ihren Entscheidungen: Was haben Sie übernommen, korrigiert oder verworfen, und warum?
- Prüfen Sie vor dem Hochladen der Digitalisate die Nutzungsbedingungen des Werkzeugs und beachten Sie die Rechteangaben in der [README-Datei](README.md#wissenschaftliche-referenz-und-nachnutzung).

---

## Teil A: KI-gestützte Transkription und Auszeichnung

### 1. Werkzeuge wählen

In Frage kommen etwa Chat-Assistenten mit Bildeingabe, spezialisierte Handschriftenerkennung (HTR) oder KI-Erweiterungen im Code-Editor. Es ist ausdrücklich erwünscht, dass Gruppen unterschiedliche Werkzeuge ausprobieren.

### 2. Die Handschrift mit KI transkribieren

Ein möglicher Ansatz: den Eintrag zunächst **ohne Lesehilfe** aus den Digitalisaten transkribieren lassen. Je genauer der Prompt, desto besser lässt sich das Ergebnis beurteilen. Mögliche Vorgaben:

- nur den Eintrag vom 27. Februar, zeilengetreu;
- historische Orthografie und Interpunktion beibehalten, Abkürzungen nicht auflösen, nichts ergänzen;
- Streichungen, Korrekturen, Unterstreichungen und lateinische Schrift kennzeichnen;
- die Notizen in der linken Spalte von S. 55 gesondert wiedergeben;
- unsichere Lesungen markieren statt raten.

Der Vergleich mit der [Lesehilfe](GT20058_Lesehilfe.txt) und dem Schriftbild zeigt, wo die KI abweicht. Eine mögliche Einteilung der Abweichungen:

- **Lesefehler:** falsch erkannte Buchstaben oder Wörter (etwa „Mattstett“ oder „ejd.“);
- **Normalisierungen:** modernisierte Schreibungen oder aufgelöste Abkürzungen;
- **Halluzinationen:** ergänzte, geglättete oder erfundene Textteile;
- **Layoutfehler:** vermischte Spalten, falsche Zeilenfolge, Text anderer Einträge;
- **Befundverluste:** übersehene Streichungen, Korrekturen oder Unterstreichungen.

Interessant kann auch der Vergleich zweier Prompts oder zweier Werkzeuge sein.

### 3. Metadaten ausfüllen

Die [XML-Vorlage](GT20058_Template.xml) lässt sich von der KI auf Grundlage der Quellenangaben in der [README-Datei](README.md) ausfüllen: Titel und Bearbeitungsverantwortung, Publikationsstatus, Aufbewahrungsort und Signatur, Datum und Ort des Eintrags.

Dabei lohnt ein genauer Blick: Hat die KI Angaben ergänzt, die in der README nicht stehen, etwa Links, Normdaten-IDs oder Angaben zum Schreiber? Und wie lässt sich im Header festhalten, dass KI-Werkzeuge beteiligt waren, etwa im `respStmt`?

### 4. Den Text mit KI auszeichnen

Die Auszeichnung kann schrittweise erfolgen. Als Grundlage bieten sich diese Bereiche an:

- **Textstruktur:** Datumszeile, Eintragstext, Seiten- und Zeilenwechsel (`dateline`, `p`, `pb`, `lb`, `<lb break="no"/>` bei Worttrennung);
- **Datum:** `date` mit `when="1825-02-27"`;
- **Eingriffe in den Text:** Streichungen (`del`), Hinzufügungen (`add`) und Ersetzungen (`subst`), etwa in der ersten Zeile („de…“) und in der gestrichenen Passage;
- **Linke Spalte:** die Expeditionsnotizen im Abschnitt `<div type="exped">`; auf welcher Seite stehen sie?

Je nach Interesse und Zeit auch:

- Abkürzungen (`abbr`);
- Personen und Orte (`persName`, `placeName` oder `rs`);
- Unterstreichungen und lateinische Schrift (`hi` mit `rend`);
- unsichere Lesungen (`unclear`).

Mögliche Prüffragen:

- Ist die Datei wohlgeformt und valide gegen das TEI-Schema?
- Hat die KI beim Auszeichnen den Text verändert?
- Entspricht die Auszeichnung dem Befund am Digitalisat, oder ist sie eine Vermutung der KI?
- Hat die KI Normdaten-Schlüssel (`key`, `ref`) erfunden?

Entscheidungen und offene Fragen lassen sich gut als XML-Kommentare festhalten, zum Beispiel:

```xml
<lb/>den Hofdienst. Venetianische <!-- KI: placeName; wir: eher Teil eines Werktitels? -->
<lb/>Sonette des Grafen Platen,
```

### 5. Ergebnisse vergleichen

Ein Vergleich über die Gruppen hinweg kann aufschlussreich sein. Mögliche Fragen:

- Welche Werkzeuge und Prompts führten zu welchen Ergebnissen?
- Beruht eine Abweichung auf einer anderen Lesung, einer anderen Kodierungsentscheidung, einem Fehler der KI oder einem eigenen Fehler?
- Wo gibt die KI Interpretation als Befund aus? Wer ist etwa mit „Mein Sohn“ oder „ihm“ gemeint, und woher „weiß“ die KI das?
- Welche Fehler waren leicht, welche schwer zu erkennen?

### 6. Die Edition der PROPYLÄEN hinzuziehen

Die [Referenzdatei](referenz_propylaeen/18250227_GT20058_tei.xml) bietet verschiedene Vergleichsmöglichkeiten, zum Beispiel:

- **Textstruktur und Korrekturen:** Wie sind Zeilen- und Seitenwechsel, Korrekturen und Expeditionsnotizen kodiert?
- **Befund und Erschließung:** Was ist Befund (z. B. `hi rendition="#u"`, `del rendition="#s"`, `g ref="#typoHyphen"`), was Erschließung (z. B. `rs` mit `key`)? Stimmen `type` und Schlüssel bei „Venetianische“ und „Hannöverischen“?
- **Thematische Gliederung:** Die `anchor`-Elemente gliedern den Eintrag in Abschnitte wie „Begegnungen“, „Lektüre“ oder „Werkentstehung“. Würden Sie anders abgrenzen oder benennen? Hat jedes Anfangs-`anchor` (`xml:id`) ein passendes End-`anchor` (`corresp`)? Wäre eine solche Gliederung eine Aufgabe für die KI?

Die Edition dient als wissenschaftliche Referenz. Eine abweichende Kodierung ist nicht automatisch falsch: Entscheidend sind Quellenbefund, Editionsziel und die zugrunde gelegten Regeln. Auch die Arbeitsdatei einer Edition kann Unstimmigkeiten enthalten.

---

## Teil B: Von der XML-Datei zur kleinen digitalen Edition

Aus der TEI/XML-Datei lässt sich eine kleine **statische Website** entwickeln, also HTML-, CSS- und gegebenenfalls JavaScript-Dateien, die ohne Server und Datenbank im Browser funktionieren. Code, Kommentare und Texte können Sie mit KI-Werkzeugen Ihrer Wahl erstellen.

Ein bewährter Grundsatz: Die XML-Datei bleibt die Datenquelle, und die Website wird aus ihr erzeugt. So lässt sich die Website nach jeder Korrektur neu erzeugen.

### 7. Editionsziel und Ansichten

Ein guter Ausgangspunkt ist die Frage, für wen die Edition gedacht ist und was sie zeigen soll. Eine erste Skizze auf Papier kann dabei helfen. Mögliche Bestandteile:

- Faksimile und Transkription nebeneinander;
- eine diplomatische Ansicht (zeilengetreu, mit Streichungen, Korrekturen und Abkürzungen);
- eine Leseansicht (fortlaufender Text ohne Gestrichenes);
- die Expeditionsnotizen als Randspalte oder eigener Block;
- ein kleines Register der Personen und Orte;
- Kommentare zu einzelnen Stellen;
- Angaben zur Quelle, zur Bearbeitung, zur Lizenz und zum KI-Einsatz.

Es muss nicht alles umgesetzt werden; zwei oder drei Bestandteile reichen für den Anfang.

### 8. Erste Kommentare

Ein Stellenkommentar erklärt, was heutigen Leserinnen und Lesern zum Verständnis fehlt. Mögliche Stellen:

- „Munda“ bzw. „mundirt“;
- „K. u Alterth.“;
- „Der junge Frommann“, „Dr. Eckermann“, „Mein Sohn“;
- die „Venetianischen Sonette“ des Grafen Platen;
- die *flora subterranea* des Grafen Sternberg;
- die „Expeditionen“ in der linken Spalte.

Die KI kann Kommentarentwürfe formulieren. Wichtig ist, jede Sachaussage an einer zitierfähigen Quelle zu prüfen, etwa an Normdaten (GND, so:fie), Nachschlagewerken oder Forschungsliteratur. Spannend für das Protokoll: Welche Angaben der KI waren falsch oder nicht belegbar?

Für die Kodierung gibt es verschiedene Möglichkeiten. Eine davon: das Lemma im Text mit einer ID versehen und aus dem Kommentar darauf verweisen. Für längere Abschnitte eignet sich, wie bei den PROPYLÄEN, ein Paar aus Anfangs- und End-`anchor`.

```xml
<!-- im Text -->
<lb/><abbr>Alterth.</abbr> <seg xml:id="k01">mundirt</seg>.

<!-- nach dem Eintrag, etwa in <back> -->
<note type="commentary" target="#k01" resp="#gruppe01">
  <!-- Erläuterung mit Beleg -->
  <bibl><!-- Quelle der Erläuterung --></bibl>
</note>
```

Personen und Orte lassen sich außerdem in Listen erfassen (`listPerson`/`person`, `listPlace`/`place`) und im Text mit `ref="#…"` verknüpfen.

### 9. Die Website erzeugen

Die KI kann ein Umwandlungsprogramm schreiben, das die XML-Datei in HTML überführt, etwa ein XSLT-Stylesheet, ein Python-Skript oder ein JavaScript, das die XML-Datei im Browser einliest. Hilfreich ist es, im Prompt Editionsziel und gewünschte Ansichten zu beschreiben und die XML-Datei mitzugeben.

Die Dateien können in einem eigenen Ordner liegen, beispielsweise `ergebnisse/gruppe_01_website/`. Anregungen, was die Website leisten könnte:

- den Text aus der XML-Datei erzeugen, statt ihn abzutippen oder von der KI neu formulieren zu lassen;
- Transkription und Faksimile zeigen;
- Kommentare an den zugehörigen Stellen erreichbar machen, etwa als Fußnote, Randnotiz oder Aufklapptext;
- in einem Abschnitt „Über diese Edition“ Quelle, Bearbeitende, Editionsregeln, KI-Werkzeuge, Lizenz und Bildnachweis nennen.

Ansehen lässt sich die Website auf verschiedenen Wegen:

- **Lokal im Browser:** `index.html` per Doppelklick öffnen. Liest ein JavaScript die XML-Datei erst beim Aufruf ein, blockieren manche Browser das bei lokal geöffneten Dateien. Dann hilft ein kleiner lokaler Server, etwa `python -m http.server` im Website-Ordner und anschließend `http://localhost:8000` im Browser, oder eine vorab erzeugte HTML-Datei (z. B. per XSLT oder Python).
- **Über Claude:** Die Seite kann als Artifact in Claude angezeigt und, falls gewünscht, mit der Gruppe geteilt werden.

### 10. Die Website prüfen

Ein kritischer Blick, gern im Austausch mit einer anderen Gruppe, kann sich etwa auf diese Punkte richten:

- **Vollständigkeit:** Erscheint alles, was in der XML-Datei ausgezeichnet ist? Was geht verloren, etwa Streichungen, Worttrennungen oder die Randspalte?
- **Texttreue:** Stimmt der angezeigte Text mit der XML-Datei überein?
- **Kommentare:** Sind die Aussagen belegt? Ist erkennbar, was Befund und was Erläuterung ist?
- **Transparenz:** Ist der KI-Einsatz nachvollziehbar dokumentiert?
- **Nutzbarkeit:** Funktioniert die Seite auf dem Smartphone, ohne Maus und mit Screenreader?
- **Nachnutzung:** Wie lässt sich die Edition zitieren? Sind die XML-Daten verlinkt?

---

## Abschluss: Ergebnisse sichern und vorstellen

Gleich welchen Weg Sie gewählt haben, bietet sich zum Schluss ein kurzes Fazit im Protokoll und eine kleine Vorstellung (etwa fünf Minuten) an. Mögliche Fragen:

- Was haben Sie gemacht, und für wen ist das Ergebnis gedacht?
- Wie sind Sie mit den KI-Werkzeugen vorgegangen?
- Wo hat die KI überzeugt, wo mussten Sie korrigieren, und wie hoch war der Prüfaufwand?
- Welche editorischen Entscheidungen würden Sie nicht an eine KI abgeben?

---

### Hilfen

- [TEI Guidelines: Metadaten im Header](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html)
- [TEI Guidelines: Streichungen, Hinzufügungen, Ersetzungen](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHAD)
- [TEI Guidelines: unsichere Lesungen (`unclear`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-unclear.html)
- [TEI Guidelines: Namen und Referenzen (`rs`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-rs.html)
- [TEI Guidelines: Anmerkungen (`note`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-note.html)
- [TEI Guidelines: Personen und Orte (`listPerson`, `listPlace`)](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html)
