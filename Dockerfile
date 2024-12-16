# Python-Image als Basis
FROM python:3.11

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen-Datei (falls vorhanden) und installiere die Abhängigkeiten
COPY requirements.txt .

# Installiere Flask und andere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Projektcode (inkl. 'index.html' und 'helper.py') in den Container
COPY . .

# Stelle sicher, dass die HTML-Datei im richtigen Ordner 'templates' ist
RUN mkdir -p /app/templates

# Setze den Befehl, um die App zu starten
CMD ["python", "Main.py"]

# Exponiere den Port, auf dem die Flask-App läuft
EXPOSE 5000
