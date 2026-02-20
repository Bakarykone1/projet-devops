from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Récupération des variables d'environnement
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'password')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def hello():
    return jsonify({"message": "Bonjour, l'Ingénieur ! Ton API Flask fonctionne."})

@app.route('/db')
def test_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "Succès", "db_version": db_version})
    except Exception as e:
        return jsonify({"status": "Erreur", "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
