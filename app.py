from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'SecDevOps Pipeline is Running!'

if __name__ == '__main__':
    # Running on all interfaces so Docker can expose it
    app.run(debug=True, host='0.0.0.0', port=5000)
    