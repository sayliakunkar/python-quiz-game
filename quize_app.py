def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
            "answer": "a"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
            "answer": "b"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
            "answer": "c"
        },
        {
            "question": "What is the capital of Germany?",
            "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
            "answer": "c"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        print(f"\nQuestion {index + 1}: {q['question']}")

        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is: {score}/{len(questions)}")


run_quiz()