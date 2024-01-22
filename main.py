from flask_cors import CORS
from waitress import serve
from app.server import create_app

app = create_app()

CORS(app)


@app.route('/')
@app.route('/index')
def home():
    return 'This is home'

if __name__ == '__main__':
    serve(app)
    
