import random

# Store leaderboard
leaderboard = {}

# Large question bank
question_bank = [
    {"question": "Which planet has the largest number of known moons?",
     "options": ["Mercury", "Uranus", "Jupiter", "Neptune"], "answer": "Jupiter"},
    {"question": "Which planet is the hottest due to its thick carbon dioxide atmosphere?",
     "options": ["Mercury", "Mars", "Venus", "Neptune"], "answer": "Venus"},
    {"question": "Which planet is known as the 'Red Planet'?",
     "options": ["Mercury", "Mars", "Venus", "Neptune"], "answer": "Mars"},
    {"question": "Which planet has the fastest rotation (about 10 hours)?",
     "options": ["Jupiter", "Mars", "Venus", "Earth"], "answer": "Jupiter"},
    {"question": "Which planet is tilted on its side, causing extreme seasons?",
     "options": ["Jupiter", "Uranus", "Venus", "Neptune"], "answer": "Uranus"},
    {"question": "Which is the smallest planet in the solar system?",
     "options": ["Mercury", "Mars", "Earth", "Venus"], "answer": "Mercury"},
    {"question": "Which planet is farthest from the Sun?",
     "options": ["Saturn", "Uranus", "Neptune", "Jupiter"], "answer": "Neptune"},
    {"question": "Which planet has a day longer than its year?",
     "options": ["Mercury", "Mars", "Venus", "Neptune"], "answer": "Venus"},
    {"question": "Which planet has the Great Red Spot?",
     "options": ["Jupiter", "Mars", "Saturn", "Neptune"], "answer": "Jupiter"},
    {"question": "Which planet has the densest atmosphere in our solar system?",
     "options": ["Earth", "Venus", "Saturn", "Neptune"], "answer": "Venus"},
    {"question": "Which planet has the largest volcano, Olympus Mons?",
     "options": ["Mars", "Earth", "Mercury", "Jupiter"], "answer": "Mars"},
    {"question": "Which planet has rings made mostly of ice particles?",
     "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": "Saturn"},
    {"question": "Which planet rotates in the opposite direction to most planets?",
     "options": ["Venus", "Mars", "Earth", "Saturn"], "answer": "Venus"},
    {"question": "Which planet is often called Earth's twin due to its size and mass?",
     "options": ["Venus", "Mars", "Mercury", "Neptune"], "answer": "Venus"},
    {"question": "Which planet is the closest to the Sun?",
     "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
    {"question": "Which planet is known for its blue color due to methane in its atmosphere?",
     "options": ["Neptune", "Mars", "Venus", "Jupiter"], "answer": "Neptune"},
    {"question": "Which planet has the highest mountain in the solar system?",
     "options": ["Mars", "Earth", "Venus", "Mercury"], "answer": "Mars"},
    {"question": "Which planet is the windiest, with speeds over 1,000 mph?",
     "options": ["Neptune", "Jupiter", "Saturn", "Venus"], "answer": "Neptune"},
    {"question": "Which planet has the most elliptical orbit?",
     "options": ["Mercury", "Mars", "Pluto", "Neptune"], "answer": "Mercury"},
    {"question": "Which planet has the shortest year (orbital period)?",
     "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"}
]

# Copy of questions that will be reduced as game goes on
unused_questions = question_bank.copy()

def ask_question(q_number, q_data):
    """Ask a single question and return True if correct."""
    letters = ["A", "B", "C", "D"]

    print(f"\n{q_number}. {q_data['question']}")
    for letter, option in zip(letters, q_data["options"]):
        print(f"{letter}. {option}")

    while True:
        choice = input("Enter the letter or the full answer: ").strip()

        # If answer is a letter
        if choice.upper() in letters:
            selected_answer = q_data["options"][letters.index(choice.upper())]
            break
        # If answer is full text
        elif choice.lower() in [opt.lower() for opt in q_data["options"]]:
            selected_answer = choice
            break
        else:
            print("Invalid input. Please enter A, B, C, D, or the full answer.")

    return selected_answer.lower() == q_data["answer"].lower()

def play_quiz():
    """Play the quiz game without repeating questions until all are used."""
    global unused_questions
    score = 0

    if len(unused_questions) < 5:
        print("\n🔄 All questions have been used. Resetting question bank.")
        unused_questions = question_bank.copy()

    selected_questions = random.sample(unused_questions, 5)

    for q in selected_questions:
        if ask_question(selected_questions.index(q) + 1, q):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {q['answer']}")
        unused_questions.remove(q)  # remove question so it won't repeat

    print(f"\nYour final score: {score}/5")
    name = input("Enter your name: ").strip()

    leaderboard[name] = score
    display_leaderboard()

def display_leaderboard():
    """Display leaderboard sorted by score."""
    print("\n🏆 Leaderboard 🏆")
    sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for rank, (player, score) in enumerate(sorted_board, start=1):
        print(f"{rank}. {player} - {score} points")

def main():
    """Main game loop."""
    print("=== Welcome to the Solar System Quiz Game ===")
    while True:
        play_quiz()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()

'''

