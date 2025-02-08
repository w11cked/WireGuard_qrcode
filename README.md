# WireGuard QR-Code Generator mit Logo und Batch-Skript

## 📚 Beschreibung

Dieses Projekt generiert **QR-Codes aus WireGuard-Konfigurationsdateien** (`.conf`). Zu jeder Datei wird ein QR-Code erzeugt, der den Dateinamen und ein benutzerdefiniertes **Logo** im finalen Bild enthält. Das Projekt unterstützt die Verarbeitung mehrerer Dateien und die **automatische Batch-Ausführung** unter Windows.

### 🔧 Features:
- Suche nach **allen `.conf`-Dateien** im Verzeichnis
- Auswahl: Entweder **eine bestimmte Datei** oder **alle auf einmal** verarbeiten
- Anpassbarer **grüner Bereich** mit Dateiname und Logo im QR-Code-Bild
- **Automatisches Starten** über eine `.bat`-Datei unter Windows

---

## 🔀 Projektstruktur

```
Projektverzeichnis
│
├── main.py               # Hauptskript zur QR-Code-Erstellung
├── requirements.txt      # Abhängigkeiten für das Projekt
├── get_qr_code.bat       # Batch-Datei zum Starten des Projekts (Windows)
├── README.md             # Projektdokumentation
├── example.conf          # Beispiel-WireGuard-Konfigurationsdatei
└── logo.png    # Das Logo, das im QR-Code eingebettet wird
```

---

## 🛠️ Installation

### 1️⃣ Python-Umgebung einrichten
Stelle sicher, dass **Python 3.8 oder höher** installiert ist.  
Erstelle eine virtuelle Umgebung und aktiviere sie:

```bash
python -m venv .venv
```

Aktiviere die virtuelle Umgebung:
- **Windows:**  
  ```bash
  .venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```bash
  source .venv/bin/activate
  ```

### 2️⃣ Abhängigkeiten installieren
Installiere die benötigten Pakete:

```bash
pip install -r requirements.txt
```

---

## 🏃 **Ausführung des Projekts**

### Möglichkeit 1: Manuelles Starten
Starte das Python-Skript manuell mit:

```bash
python main.py
```

### Möglichkeit 2: Nutzung der Batch-Datei (Windows)
Führe die **`get_qr_code.bat`** aus:

```bash
get_qr_code.bat
```

---

## 📄 **Beispielkonfigurationsdatei (`example.conf`)**

Eine WireGuard-Konfigurationsdatei enthält Details zur **Netzwerkkonfiguration**. Der Inhalt ist in **[Abschnitte]** wie `[Interface]` und `[Peer]` unterteilt.

### Beispielinhalt:
```
[Interface]
PrivateKey = wJ3b5nMK+fR...sample...key==
Address = 10.0.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = T29f9X7K...sample...peerkey==
Endpoint = 203.0.113.1:51820
AllowedIPs = 0.0.0.0/0
```

### Erklärung der Abschnitte:
- **[Interface]**: Beschreibt die lokale WireGuard-Schnittstelle.
  - `PrivateKey`: Der private Schlüssel für diese Verbindung.
  - `Address`: Die IP-Adresse dieses Geräts im VPN-Netzwerk.
  - `DNS`: DNS-Server für diese Verbindung.


- **[Peer]**: Beschreibt den entfernten Peer (Gegenstelle).
  - `PublicKey`: Der öffentliche Schlüssel des Peers.
  - `Endpoint`: Die Adresse und der Port der Gegenstelle.
  - `AllowedIPs`: Die IP-Adressen, die über diese Verbindung geroutet werden.

### **Sicherheitshinweis:**
- Die Konfigurationsdatei enthält sensible Informationen wie den privaten Schlüssel. Gehe daher sorgfältig mit den generierten QR-Codes um!

---

## 📦 **Inhalt der `requirements.txt`**

Die Datei wird mit `pip freeze > requirements.txt` generiert. Sie enthält die Abhängigkeiten des Projekts mit exakten Versionsnummern:

```
colorama==0.4.6
pillow==11.1.0
qrcode==8.0
```

---

## 📋 **Funktionen im Projekt**

1. **Suchen und auswählen:**  
   - Das Skript sucht nach `.conf`-Dateien und bietet die Auswahl:
     - Eine bestimmte Datei auswählen
     - Alle Dateien verarbeiten

2. **QR-Code-Erstellung:**  
   - Der QR-Code wird aus den Konfigurationsdaten erstellt.

3. **Visuelle Anpassung:**  
   - Das Bild enthält einen grünen Bereich, in dem der Dateiname in Weiß und das Logo angezeigt werden.

4. **Ausgabe:**  
   - Die QR-Codes werden im Verzeichnis als PNG-Dateien gespeichert.

---

## 📚 **Beispielausgabe**

Ein Beispielbild zeigt den QR-Code oben und den grünen Bereich darunter mit dem Dateinamen und Logo:

```
qr_code_example.png
```



## 🛡️ **Sicherheit**
Da die `.conf`-Dateien vertrauliche Informationen wie private Schlüssel enthalten, sollten die generierten QR-Codes nur an autorisierte Personen weitergegeben werden.

