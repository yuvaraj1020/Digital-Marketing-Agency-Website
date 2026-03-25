from flask import Blueprint, jsonify
import random

public_bp = Blueprint('public_bp', __name__)

QUOTES = [
    "Great brands are built through bold ideas and powerful storytelling.",
    "Design is the silent ambassador of your brand.",
    "Marketing is no longer about the stuff that you make, but about the stories you tell.",
    "Innovation distinguishes between a leader and a follower.",
    "Creativity is intelligence having fun.",
    "Good marketing makes the company look smart. Great marketing makes the customer feel smart."
]

@public_bp.route('/api/quotes/random', methods=['GET'])
def get_random_quote():
    quote = random.choice(QUOTES)
    return jsonify({"quote": quote})
