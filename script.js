document.getElementById('resumeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var formData = new FormData(this); // Create a FormData object to store form data

    fetch('/process_resume', { // Replace '/process_resume' with the actual backend endpoint
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // Parse the JSON response from the backend
    .then(data => {
        // Display the result returned by the backend
        document.getElementById('result').innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('scheduleForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var formData = new FormData(this); // Create a FormData object to store form data

    fetch('/schedule_interview', { // Replace '/schedule_interview' with the actual backend endpoint
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // Parse the JSON response from the backend
    .then(data => {
        // Display the result returned by the backend
        document.getElementById('result').innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
