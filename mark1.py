import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the data
data = {
    'resume_text': [
        "PROJECTS: Developed an e-commerce platform with seamless payment integration and user-friendly interface, Created a Chatbox with AI Integration, Created a working robot,Created a working robot with AI Integration, Online Shopping,",
        "SKILLS: Excellent communication, problem-solving, and leadership abilities. Proficient in Python, Java, SQL, c++, c language and Ruby",
        "EXPERIENCE: Worked as a software engineer intern at a leading tech company, contributing to the development of innovative products, Sales Manager, Assistant",
        "ACHIEVEMENTS: Received the 'Employee of the Year' award for outstanding performance and dedication.",
        "EDUCATION: Graduated with honors in Computer Science from a top-tier university. GPA: 3.9/4.0",
        "CERTIFICATIONS: Certified Scrum Master (CSM) and AWS Certified Solutions Architect.",
        "VOLUNTEER WORK: Organized coding workshops for underprivileged youth, fostering interest in technology.",
        "LANGUAGES: Fluent in English, Spanish, and Mandarin Chinese.",
        "INTERESTS: Passionate about artificial intelligence, blockchain technology, and machine learning applications.",
        # Additional positive qualities
        "POSITIVE QUALITIES: Exceptional problem solver, creative thinker, team player, adaptable to change.",
        "NEGATIVE TERMS: None of these are necessarily negative, but they include terms like 'challenges', 'struggles', 'overcome difficulties'.",
        # Add more diverse resume texts here
    ],
    'label': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]  # 1 represents a positive label for a great resume
}

# Create a DataFrame
df = pd.DataFrame(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['resume_text'], df['label'], test_size=0.2, random_state=42)

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Define a simple neural network model using TensorFlow
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_vect.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
X_train_dense = X_train_vect.toarray()
model.fit(X_train_dense, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
X_test_dense = X_test_vect.toarray()
accuracy = model.evaluate(X_test_dense, y_test)[1]

print("Accuracy:", accuracy)