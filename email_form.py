from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Communication</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Email Communication</h1>
        <form id="emailForm" method="post">
            <label for="recipient">Recipient:</label>
            <input type="email" id="recipient" name="recipient" required>
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="6" required></textarea>
            <button type="submit">Send Email</button>
        </form>
        <div id="result">{{ result }}</div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def email_form():
    result = ""
    if request.method == 'POST':
        # Get form data
        recipient = request.form['recipient']
        subject = request.form['subject']
        message = request.form['message']
        
        # Here you would implement the logic to send an email
        # For example, using smtplib or a third-party service like SendGrid
        # Since we cannot send emails from this environment, we'll just simulate it
        result = f"Email sent to {recipient} with subject '{subject}' and message '{message}'"
    
    # Render the form with the result
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)