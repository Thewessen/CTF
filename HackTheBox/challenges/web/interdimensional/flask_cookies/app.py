from flask import Flask, jsonify, session, request

app = Flask(__name__)
app.config.update({'SECRET_KEY': 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw'})

@app.route('/')
def index():
    a = request.args.get('a')
    session['a'] = a
    return jsonify(dict(session))

