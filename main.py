from app.server import create_app
from waitress import serve
from flask_cors import CORS

app = create_app()
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "https://wemen-frontend-7idcrv8r3-nanyamax.vercel.app"}})


if __name__ == '__main__':
    app.run( host="0.0.0.0", port=3000)
