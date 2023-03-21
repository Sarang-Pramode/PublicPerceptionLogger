from flask import Flask, request, render_template

app = Flask(__name__)

visits = 0

@app.before_request
def count_visits():
    global visits
    if request.host == 'www.soteriia.com':
        visits += 1

@app.route('/')
def index():
    return render_template('index.html', visits=visits)

if __name__ == '__main__':
    app.run(debug=True)
