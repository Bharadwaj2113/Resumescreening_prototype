from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('resume_screening.html')

@app.route('/screen_resume', methods=['POST'])
def screen_resume():
    # Your processing code here
    return "Processing the uploaded resume..."

if __name__ == '__main__':
    app.run(debug=True)
