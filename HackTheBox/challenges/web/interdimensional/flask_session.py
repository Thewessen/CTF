#!/usr/bin/env python3

from flask import Flask, session

def main():
    app = Flask(__name__)
    app.secret_key = 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw'

    session.set('ingredient', 'xmcnryleff')
    session.set('measurements', '9+6')


    print(dir(session))

if __name__ == '__main__':
    main()
