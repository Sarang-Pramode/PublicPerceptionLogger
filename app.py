from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM clicks;')
    count = cur.fetchone()[0]
    cur.close()
    return render_template('index.html', visits=count)

@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    cur = conn.cursor()
    cur.execute('INSERT INTO clicks (timestamp) VALUES (NOW());')
    conn.commit()
    cur.close()
    return redirect(url_for('redirect_to_soteriia'))

@app.route('/redirect-to-soteriia')
def redirect_to_soteriia():
    return redirect('http://www.soteriia.com')

if __name__ == '__main__':
    app.run(debug=True)
