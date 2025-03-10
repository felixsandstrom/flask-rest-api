import pyautogui
import time

# Wait for the user to switch to VS Code manually
time.sleep(3)

# Step 1: Open a new Terminal in VS Code (Ctrl+Shift+`)
pyautogui.hotkey('ctrl', 'shift', '`')
time.sleep(2)  # Pause to allow terminal to open

# Step 2: Create Virtual Environment
pyautogui.write('python -m venv venv', interval=0.1)
pyautogui.press('enter')
time.sleep(5)  # Pause for venv creation

# Step 3: Activate Virtual Environment (Windows PowerShell)
pyautogui.write('.\\venv\\Scripts\\Activate', interval=0.1)
pyautogui.press('enter')
time.sleep(2)

# Step 4: Install Dependencies
pyautogui.write('pip install flask flask-sqlalchemy', interval=0.1)
pyautogui.press('enter')
time.sleep(10)  # Pause for installation

# Step 5: Open the file using Ctrl+P
pyautogui.hotkey('ctrl', 'p')  
time.sleep(1)

# Step 6: Type the filename and open it
filename = "restful_api.py"
pyautogui.write(filename, interval=0.3)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)  # Allow file to open

# Step 7: Code to be typed
code = '''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurer database (Bruker SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///varer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Modell
class Vare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    navn = db.Column(db.String(100), nullable=False) 
    pris = db.Column(db.Float, nullable=False) 

# Opprett database
with app.app_context():
    db.create_all()

# Hent alle varer (GET)
@app.route('/varer', methods=['GET'])
def hent_alle_varer():
    varer = Vare.query.all()
    return jsonify([{"id": vare.id, "navn": vare.navn, "pris": vare.pris} for vare in varer])

# Legg til en ny vare (POST)
@app.route('/varer', methods=['POST'])
def legg_til_vare():
    data = request.get_json()
    ny_vare = Vare(navn=data["navn"], pris=data["pris"])
    db.session.add(ny_vare)
    db.session.commit()
    return jsonify({"id": ny_vare.id, "navn": ny_vare.navn, "pris": ny_vare.pris}), 201

# Slett en vare (DELETE)
@app.route('/varer/<int:vare_id>', methods=['DELETE'])
def slett_vare(vare_id):
    vare = Vare.query.get(vare_id)
    if not vare:
        return jsonify({"melding": "Vare ikke funnet"}), 404
    
    db.session.delete(vare)
    db.session.commit()
    return jsonify({"melding": "Vare slettet"}), 200

if __name__ == '__main__':
    app.run(debug=True)
'''

# Step 8: Type the code with natural pauses
for line in code.split('\n'):
    pyautogui.write(line, interval=0.15)
    pyautogui.press('enter')
    time.sleep(0.5)  # Short pause after each line
