from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('google_calendar.html')  # Render google_calendar.html

@app.route('/create_event', methods=['POST'])
def create_event():
    # Get form data
    event_title = request.form['eventTitle']
    interview_datetime = request.form['interviewDateTime']
    event_location = request.form['eventLocation']
    event_description = request.form['eventDescription']

    # Print form data (you can perform further processing here)
    print("Event Title:", event_title)
    print("Interview Date and Time:", interview_datetime)
    print("Location:", event_location)
    print("Description:", event_description)

    # Perform additional processing here, such as creating a calendar event

    # Return a response (you can customize this based on your requirements)
    return "Calendar event created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
