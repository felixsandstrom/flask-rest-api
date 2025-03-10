# Flask REST API – Backend

Dette prosjektet demonstrerer hvordan man bygger en **REST API med Flask** og en **SQLite-database**.  
API-et gjør det mulig å lagre, hente og administrere data via HTTP-endepunkter.

## 📂 Prosjektstruktur
```
flask-rest-api/
│── rest_api.py
│── requirements.txt
│── README.md       # Dokumentasjon
```

## 🛠️ Hvordan kjøre backend (Flask)
Følg disse stegene for å kjøre backend-løsningen på din lokale maskin.

### 1️⃣ Klone repositoryet
```bash
git clone https://github.com/felixsandstrom/flask-rest-api.git
cd flask-rest-api
```

### 2️⃣ Opprett et virtuelt miljø og installer avhengigheter
```bash
python -m venv venv
source venv/bin/activate  # På Windows bruk: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Start Flask-serveren
```bash
python app.py
```
API-et kjører nå på `http://127.0.0.1:5000/`

## 🔥 API Endepunkter
| Metode  | Endepunkt       | Beskrivelse               |
|---------|---------------|---------------------------|
| `GET`   | `/items`      | Henter alle elementer     |
| `POST`  | `/items`      | Legger til et nytt element |
| `PUT`   | `/items/<id>` | Oppdaterer et element     |
| `DELETE`| `/items/<id>` | Sletter et element        |

## 📌 YouTube-video
🎬 **Del 1: Flask API med SQLite** – [Se video](https://www.youtube.com/YOUR_VIDEO_LINK)

## 📂 Kode fra videoen
🔗 **[GitHub Repository (Backend)](https://github.com/felixsandstrom/flask-rest-api/tree/main)**

## 📧 Kontakt
🌍 **Nettside:** [www.felixwebutvikling.no](https://www.felixwebutvikling.no/)  
📧 **E-post:** [info@felixwebutvikling.no](mailto:info@felixwebutvikling.no)  
