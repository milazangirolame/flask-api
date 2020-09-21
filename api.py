from flask import Flask

app = Flask(__name__)

@app.route('/api/index')
def get_api_index():
    return 'index'

@app.route('/')
def get_home():
    return 'index'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
