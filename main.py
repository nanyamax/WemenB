from app.server import create_app
from waitress import serve

app = create_app()
print("Started")

@app.route('/')
@app.route('/index')
def home():
    return 'This is home'

if __name__ == '__main__':
    serve(app)
