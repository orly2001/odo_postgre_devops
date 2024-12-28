from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    odoo_url = os.getenv('ODOO_URL', '#')
    pgadmin_url = os.getenv('PGADMIN_URL', '#')
    return f"<h1>Bienvenue sur le site vitrine</h1><p><a href='{odoo_url}'>Odoo</a></p><p><a href='{pgadmin_url}'>pgAdmin</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
