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
    """Play the quiz game."""
    score = 0
    selected_questions = random.sample(question_bank, 5)

    for i, q_data in enumerate(selected_questions, start=1):
        if ask_question(i, q_data):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {q_data['answer']}")

    print(f"\nYour final score: {score}/5")
    name = input("Enter your name: ").strip()

    leaderboard[name] = score
    display_leaderboard()


def display_leaderboard():
    """Display leaderboard sorted by score."""
    print("\n🏆 Leaderboard 🏆")
    sorted_board = sorted(leaderboard.items(),
                          key=lambda x: x[1], reverse=True)
    for rank, (player, score) in enumerate(sorted_board, start=1):
        print(f"{rank}. {player} - {score} points")


def main():
    """Main game loop."""
    print(" ")
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

"""
Quiz Game with Leaderboard
Author: Generated by AI (prompt-run)
Purpose: Terminal-based multiple-choice quiz game that:
 - Asks 5 questions (each with 4 options)
 - Tracks the score
 - Asks for player's name after the quiz
 - Stores name and score in a dictionary (leaderboard)
 - Displays leaderboard sorted in descending order of scores
 - Avoids repeating questions when player restarts the game in the same program run


'''  # import random
# import textwrap
# from typing import Dict, List, Tuple

# -------------------------
# Data structures & config
# -------------------------

# { "question": str, "options": List[str], "answer": int }
''' Question = Dict[str, object]

# Hard-coded question bank. Easy to extend or load from file in future.
QUESTION_BANK: List[Question] = [
    {
        "question": "What is the time complexity of binary search in a sorted list?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        # 1-based index for human readability (1 -> first option). Here 2 -> "O(log n)"
        "answer": 2,
    },
    {
        "question": "Which device converts AC to DC?",
        "options": ["Transformer", "Rectifier", "Inverter", "Oscillator"],
        "answer": 2,
    },
    {
        "question": "What does 'HTTP' stand for?",
        "options": [
            "HyperText Transfer Protocol",
            "Hyperlink Transfer Text Protocol",
            "High Transfer Text Protocol",
            "Hyper Transfer Text Process"
        ],
        "answer": 1,
    },
    {
        "question": "Which of the following is not a programming paradigm?",
        "options": ["Functional", "Procedural", "Object-oriented", "Editorial"],
        "answer": 4,
    },
    {
        "question": "Which semiconductor device is used to amplify signals?",
        "options": ["Diode", "Transistor", "Resistor", "Inductor"],
        "answer": 2,
    },
    {
        "question": "In a 3-phase motor, what happens if one phase is lost?",
        "options": [
            "The motor runs normally",
            "The motor may overheat and lose torque",
            "The motor speed doubles",
            "All lights in the building go off"
        ],
        "answer": 2,
    },
    {
        "question": "What is the SI unit of electric charge?",
        "options": ["Volt", "Ohm", "Coulomb", "Farad"],
        "answer": 3,
    },
    {
        "question": "Which data structure uses FIFO ordering?",
        "options": ["Stack", "Queue", "Tree", "Hash Table"],
        "answer": 2,
    },
    {
        "question": "Which layer of the OSI model provides routing between networks?",
        "options": ["Data Link", "Transport", "Network", "Application"],
        "answer": 3,
    },
    {
        "question": "What is an advantage of using magnetic levitation in transport?",
        "options": [
            "Increased friction",
            "Higher wear and tear",
            "Less mechanical contact — reduced friction",
            "Lower speed"
        ],
        "answer": 3,
    },
]

NUM_QUESTIONS_PER_GAME = 5


# -------------------------
# Quiz Manager Class
# -------------------------

class QuizManager:
    """
    Manages question selection and tracks which questions have been used in this program run.
    Ensures that questions are not repeated until all have been used.
    """

    def __init__(self, question_bank: List[Question]):
        if len(question_bank) < NUM_QUESTIONS_PER_GAME:
            raise ValueError(
                "Question bank must contain at least NUM_QUESTIONS_PER_GAME questions.")
        # immutable reference not enforced, but we copy
        self._master_bank = list(question_bank)
        self._available_indices = list(range(len(self._master_bank)))
        random.shuffle(self._available_indices)
        self._used_indices: List[int] = []

    def get_quiz_questions(self, count: int = NUM_QUESTIONS_PER_GAME) -> List[Question]:
        """
        Get `count` unique questions from the available pool, removing them from available.
        If available pool runs low, recycle used questions after exhausting the bank.
        """
        if count <= 0:
            return []

        if len(self._available_indices) < count:
            # Not enough fresh questions remain. Recycle used ones back into available.
            # This ensures continued play, while preventing immediate repeats until full cycle.
            print(
                "\n[Notice] Question pool is being refreshed to avoid repetition.\n")
            self._available_indices = self._used_indices.copy()
            random.shuffle(self._available_indices)
            self._used_indices = []

            # If still not enough (shouldn't happen if bank size >= count), raise error:
            if len(self._available_indices) < count:
                raise RuntimeError(
                    "Not enough questions available to generate a quiz.")

        selected_indices = [self._available_indices.pop()
                            for _ in range(count)]
        self._used_indices.extend(selected_indices)
        return [self._master_bank[i] for i in selected_indices]


# -------------------------
# Leaderboard functions
# -------------------------

def update_leaderboard(leaderboard: Dict[str, int], player_name: str, score: int) -> None:
    """
    Update the leaderboard dictionary with player's score.
    Behavior: keep the highest score for each player.
    """
    previous = leaderboard.get(player_name)
    if previous is None or score > previous:
        leaderboard[player_name] = score


def display_leaderboard(leaderboard: Dict[str, int]) -> None:
    """
    Print the leaderboard sorted in descending order of scores.
    """
    if not leaderboard:
        print("\nLeaderboard is currently empty.\n")
        return

    sorted_entries = sorted(leaderboard.items(),
                            key=lambda kv: kv[1], reverse=True)
    print("\n===== LEADERBOARD =====")
    print("{:3} | {:20} | {:5}".format("No.", "Player", "Score"))
    print("-" * 34)
    for i, (name, score) in enumerate(sorted_entries, start=1):
        print("{:3} | {:20} | {:5}".format(i, name, score))
    print("=" * 34 + "\n")


# -------------------------
# User interaction helpers
# -------------------------

def prompt_choice(prompt_text: str, valid_choices: List[str]) -> str:
    """
    Prompt the user until they provide an input in valid_choices (case-insensitive).
    Returns the normalized (lowercase) choice.
    """
    valid_lower = [c.lower() for c in valid_choices]
    while True:
        choice = input(prompt_text).strip().lower()
        if choice in valid_lower:
            return choice
        print(f"Invalid input. Choose from: {', '.join(valid_choices)}.")


def ask_question(q: Question, q_num: int, total: int) -> bool:
    """
    Ask a single question. Returns True if the user answered correctly.
    """
    print("\n" + "-" * 60)
    header = f"Question {q_num}/{total}"
    print(header)
    print("-" * len(header))
    print(textwrap.fill(q["question"], width=70))
    print()

    # Present options with letters A-D
    letters = ["A", "B", "C", "D"]
    for i, option in enumerate(q["options"], start=1):
        print(f"  {letters[i - 1]}. {option}")

    # Accept either letters or numbers (A/B/C/D or 1/2/3/4)
    user_input = prompt_choice(
        "Answer (A/B/C/D or 1-4): ", ["A", "B", "C", "D", "1", "2", "3", "4"])
    # Map input to 1-based integer index
    if user_input in ("a", "1"):
        selected = 1
    elif user_input in ("b", "2"):
        selected = 2
    elif user_input in ("c", "3"):
        selected = 3
    else:
        selected = 4

    # Evaluate
    correct = selected == q["answer"]
    if correct:
        print("Correct! ✅")
    else:
        correct_option = q["options"][q["answer"] - 1]
        print(f"Incorrect. The correct answer was: {correct_option}")
    return correct


# -------------------------
# Game play logic
# -------------------------

def play_quiz(quiz_manager: QuizManager, leaderboard: Dict[str, int]) -> None:
    """
    Runs one round of the quiz: ask NUM_QUESTIONS_PER_GAME questions, compute score,
    get player's name, update and display leaderboard.
    """
    questions = quiz_manager.get_quiz_questions(NUM_QUESTIONS_PER_GAME)
    score = 0
    total = len(questions)

    print("\nStarting quiz... Good luck!\n")
    for i, q in enumerate(questions, start=1):
        try:
            if ask_question(q, i, total):
                score += 1
        except Exception as e:
            # Defensive catch: we don't want one bad question to crash the quiz
            print(
                f"[Error] Problem asking question: {e}. Skipping this question.")
    print("\n" + "=" * 40)
    print(f"Quiz finished. You scored {score} out of {total}.")
    print("=" * 40)

    # Ask for player's name AFTER quiz, as required by brief
    name = input("Enter your name (for the leaderboard): ").strip()
    if not name:
        name = "Anonymous"

    # Update leaderboard with best score behaviour
    update_leaderboard(leaderboard, name, score)
    print(f"Thanks, {name}. Your score has been recorded.")

    # Display leaderboard
    display_leaderboard(leaderboard)


# -------------------------
# Main program loop
# -------------------------

def main():
    print("WELCOME to the Quiz Game!")
    print("You will be asked 5 multiple-choice questions each round.")
    print("Answer by typing A/B/C/D or 1/2/3/4, then press Enter.")
    print()

    quiz_manager = QuizManager(QUESTION_BANK)
    leaderboard: Dict[str, int] = {}

    while True:
        play_quiz(quiz_manager, leaderboard)
        choice = prompt_choice(
            "Would you like to play again? (Y/N/L to view leaderboard): ", ["Y", "N", "L"])
        if choice == "y":
            continue
        elif choice == "l":
            display_leaderboard(leaderboard)
            # After showing leaderboard, prompt continue / quit
            cont = prompt_choice("Play another round? (Y/N): ", ["Y", "N"])
            if cont == "y":
                continue
            else:
                print("Goodbye! Thanks for playing.")
                break
        else:
            print("Goodbye! Thanks for playing.")
            break


if __name__ == "__main__":
    main() '''
