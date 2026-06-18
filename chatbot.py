"""
Basic Rule-Based Chatbot
-------------------------
A simple command-line chatbot that responds to user input using keyword
matching. No external libraries or API keys required.

Run with: python chatbot.py
"""

import random
import re

BOT_NAME = "Botty"

# Each entry: (list of regex patterns to match, list of possible responses)
RULES = [
    (r"\b(hi|hello|hey)\b", [
        "Hello there!", "Hi! How can I help you today?", "Hey! What's up?"
    ]),
    (r"\bhow are you\b", [
        "I'm just a program, but I'm doing great! How about you?",
        "Running smoothly, thanks for asking!"
    ]),
    (r"\b(your name|who are you)\b", [
        f"I'm {BOT_NAME}, your friendly chatbot.",
        f"You can call me {BOT_NAME}."
    ]),
    (r"\b(bye|goodbye|exit|quit)\b", [
        "Goodbye! Have a great day!", "See you later!", "Bye!"
    ]),
    (r"\b(thanks|thank you)\b", [
        "You're welcome!", "Anytime!", "No problem at all!"
    ]),
    (r"\bweather\b", [
        "I can't check live weather yet, but I hope it's sunny where you are!",
    ]),
    (r"\b(help|what can you do)\b", [
        "I can chat about simple things — try greeting me, asking my name, "
        "or saying thanks!"
    ]),
]

EXIT_PATTERN = re.compile(r"\b(bye|goodbye|exit|quit)\b", re.IGNORECASE)
DEFAULT_RESPONSES = [
    "Interesting — tell me more.",
    "I'm not quite sure I understand. Could you rephrase that?",
    "Hmm, I don't have a response for that yet.",
    "Let's talk about something else!",
]


def get_response(user_input: str) -> str:
    """Return a response based on matching the user's input against rules."""
    text = user_input.lower()
    for pattern, responses in RULES:
        if re.search(pattern, text):
            return random.choice(responses)
    return random.choice(DEFAULT_RESPONSES)


def main():
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}. Type 'quit' anytime to exit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = get_response(user_input)
        print(f"{BOT_NAME}: {response}")

        if EXIT_PATTERN.search(user_input.lower()):
            break


if __name__ == "__main__":
    main()
