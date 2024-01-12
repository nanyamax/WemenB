from app.server import create_app
from waitress import serve
from flask_cors import CORS

app = create_app()
CORS(app, origins=['*'])


@app.route('/')
@app.route('/index')
def home():
    return 'This is home'

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
