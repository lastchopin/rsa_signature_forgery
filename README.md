# Universelle Fälschung von RSA-Signaturen in Python

Dieses Projekt demonstriert die universelle Fälschung von RSA-Signaturen mittels eines chosen-message Angriffs. Es beinhaltet die Generierung eines eigenen 3000-Bit RSA-Schlüssels sowie die Implementierung eines Angriffsszenarios, bei dem der Angreifer eine beliebige Nachricht fälschen kann und anschließend die gefälschte Signatur verifiziert wird.

## Inhaltsverzeichnis

- [Beschreibung](#beschreibung)
- [BSI Empfehlungen aus TR-02102 zur RSA Signatur](#bsi-empfehlungen-aus-tr-02102-zur-rsa-signatur)
- [Installation](#installation)
- [Benutzung](#benutzung)

## Beschreibung

Das Projekt umfasst die folgenden Hauptkomponenten:

1. **RSA-Schlüsselgenerierung**: Erzeugt einen RSA-Schlüssel mit 3000-Bit gemäß den spezifizierten Vorgaben.
2. **RSA-Signaturerzeugung und -Verifikation**: Implementiert die Funktionen zur Signaturerstellung und -verifikation mittels RSA.
3. **Universelle Fälschung von RSA-Signaturen**: Zeigt, wie ein Angreifer eine RSA-Signatur für eine beliebige Nachricht fälschen kann, ohne den privaten Schlüssel zu kennen.

## BSI Empfehlungen aus TR-02102 zur RSA Signatur
Gemäß der BSI Technischen Richtlinie TR-02102 für den Einsatz digitaler Signaturen sind folgende Empfehlungen relevant:

**RSA-Schlüssellänge**

Die Länge des Modulus n sollte mindestens 3000 Bit betragen, um eine ausreichende Sicherheit gegenüber aktuellen und zukünftigen Kryptoanalysemethoden zu gewährleisten.

**Hashfunktionen**

Für die Verwendung in RSA-Signaturen werden bestimmte Hashfunktionen empfohlen, um die Sicherheit und Robustheit der Signaturen zu erhöhen. Empfohlene Hashfunktionen gemäß BSI TR-02102 sind:

- **SHA-256**: Eine kryptographisch sichere Hashfunktion mit einer Ausgabelänge von 256 Bit. Sie bietet eine gute Balance zwischen Geschwindigkeit und Sicherheit.
- **SHA-384**: Eine Variante von SHA-2 mit einer Ausgabelänge von 384 Bit. Geeignet für Anwendungen, die eine höhere Sicherheitsreserve erfordern.
- **SHA-512**: Eine weitere Variante von SHA-2 mit einer Ausgabelänge von 512 Bit. Bietet eine maximale Sicherheitsreserve, ist jedoch langsamer als SHA-256 und SHA-384.

Diese Hashfunktionen sollten für die Erzeugung von Hashwerten verwendet werden, die dann für die RSA-Signatur verwendet werden.

## Installation

1. **Klonen Sie das Repository**:
   ```bash
   git clone https://github.com/your_username/rsa_signature_forgery.git
   ```
2. **Wechseln Sie in das Verzeichnis**:
   ```bash
   cd rsa_signature_forgery
   ```
3. **Benötigte Pakete installieren:**:
   ```bash
   pip install pycryptodome
   ```

## Benutzung 

Das Projekt besteht aus mehreren Python-Skripten:

- `rsa_key_generation.py`: Erzeugt die RSA-Schlüssel.
- `rsa_signature_forgery.py`: Demonstriert die universelle Fälschung von RSA-Signaturen.

## RSA-Schlüsselgenerierung

Erzeugen Sie einen 3000-Bit RSA-Schlüssel:
```bash
python rsa_key_generation.py
```

## Universelle Fälschung von RSA-Signaturen

Fälschen Sie eine RSA-Signatur für eine beliebige Nachricht und verifizieren Sie sie:
```bash
python rsa_signature_forgery.py
```

## Hinweis

Dieses Projekt dient ausschließlich zu Bildungszwecken und zur Demonstration eines Angriffs auf RSA-Signaturen. Es sollte nicht in einer produktiven Umgebung eingesetzt werden.
