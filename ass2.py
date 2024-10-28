import streamlit as st

# Define quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Bangalore"],
        "answer": "New Delhi"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["0°C", "50°C", "100°C", "150°C"],
        "answer": "100°C"
    }
]

# Streamlit application
def main():
    st.title("Online Quiz Application")
    st.write("Welcome to the quiz! Please enter your details to start.")

    # User details input
    name = st.text_input("Enter your name:")
    roll_number = st.text_input("Enter your roll number:")
    class_name = st.text_input("Enter your class:")

    if st.button("Start Quiz"):
        if name and roll_number and class_name:
            st.session_state.started = True
            st.session_state.score = 0
            st.session_state.current_question = 0
            st.session_state.answered = [False] * len(questions)  # Track answered questions
        else:
            st.error("Please fill in all fields to start the quiz.")

    # Quiz section
    if st.session_state.get("started"):
        current_question = st.session_state.current_question
        question = questions[current_question]
        st.subheader(question["question"])
        selected_option = st.radio("Select an option:", question["options"], key="options")

        # Submit Answer Button
        if st.button("Submit Answer"):
            if selected_option == question["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect! The correct answer is: {question['answer']}")

            st.session_state.answered[current_question] = True  # Mark this question as answered

        # Show the next question button only after the user answers the current question
        if st.session_state.answered[current_question]:
            if st.button("Next Question"):
                if current_question < len(questions) - 1:
                    st.session_state.current_question += 1
                else:
                    st.session_state.started = False
                    st.session_state.current_question = 0
                    st.write(f"Your final score is: {st.session_state.score}/{len(questions)}")
                    st.balloons()  # Celebration balloons for completion

if __name__ == "__main__":
    # Initialize session state
    if 'started' not in st.session_state:
        st.session_state.started = False
    main()
