from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main webpage where users can input a number.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Running frontend on port 5000
