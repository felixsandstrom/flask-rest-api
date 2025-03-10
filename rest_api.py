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

# Oppdater en eksisterende vare (PUT)
@app.route('/varer/<int:vare_id>', methods=['PUT'])
def oppdater_vare(vare_id):
    vare = Vare.query.get(vare_id)
    if not vare:
        return jsonify({"melding": "Vare ikke funnet"}), 404

    data = request.get_json()
    if "navn" in data:
        vare.navn = data["navn"]
    if "pris" in data:
        vare.pris = data["pris"]

    db.session.commit()
    return jsonify({"id": vare.id, "navn": vare.navn, "pris": vare.pris})

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