from flask import Flask, request, jsonify
from PyPDF2 import PdfReader

app = Flask(_name_)

@app.route('/')  
def index():
    return app.send_static_file('resume_screening.html')

@app.route('/resume_screening.html', methods=['GET', 'POST'])  
def resume_screening():
    return app.send_static_file('resume_screening.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file part'})
    
    resume_file = request.files['resume']

    if resume_file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if resume_file:
        resume_text = extract_text(resume_file)
        # Calculate evaluation percentage based on keyword occurrences
        evaluation_percentage = calculate_evaluation(resume_text)
        return jsonify({'evaluation_percentage': evaluation_percentage})

def extract_text(file):
    if file.filename.endswith('.pdf'):
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    else:
        return 'Unsupported file format'

def calculate_evaluation(text):
    keywords = ['Project', 'Research', 'Languages known', 'Achievements', 'Skills']
    keyword_counts = {keyword: text.count(keyword) for keyword in keywords}
    
    # Assign weights for each keyword
    weights = {'Project': 0.2, 'Research': 0.2, 'Languages known': 0.2, 
               'Achievements': 0.2, 'Skills': 0.2}
    
    # Calculate evaluation percentage based on keyword counts and weights
    evaluation_percentage = sum(keyword_counts[keyword] >= (2 if keyword == 'Achievements' else 1) for keyword in keywords) * 20
    
    return evaluation_percentage

if _name_ == '_main_':
    app.run(debug=True)