# app.py - pagrindine Flask aplikacijos logika
# Siame faile aprasyti marsrutai (routes)

# Reikalingos bibliotekos (importai)
from flask import Flask, render_template
# Sukuriame Flask aplikacijos objekta
app = Flask(__name__)

# Marsrutas: pagrindinis puslapis
# URL: /
# Metodas: GET
# Atvaizduoja index.html sablona
@app.route("/") # Dekoratorius
def index():
    return render_template("index.html")

# Marsrutas: kontaktu puslapis (forma)
# Metodai: GET ir POST
@app.route("/kontaktai") # Dekoratorius
def kontaktai():
    return render_template("kontaktai.html")

# Aplikacijos paleidimas
# Paleidimo metu kai debug = true - automatinis plikacijos perkrovimas pakeitus koda = klaidu rodymas

if __name__ == "__main__":
    app.run(debug=True)