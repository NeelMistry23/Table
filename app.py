from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL DB config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # keep empty if no password set in XAMPP
    'database': 'table',
    'port':'3307'
}

@app.route("/api/offices")
def get_offices():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM offices")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/api/get_office_employees/<office_code>/")
def get_employees(office_code):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE office_code = %s", (officeCode,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/api/new_employee/<officeCode>/", methods=["POST"])
def new_employee(office_code):
    data = request.json
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employees (last_name, first_name, extension, email, office_code) VALUES (%s, %s, %s, %s, %s)",
            (data["last_name"], data["first_name"], data["extension"], data["email"], office_code)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
