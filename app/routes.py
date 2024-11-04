from flask import Blueprint, render_template, jsonify
from .ai.agents import start_dialog

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/start-dialog', methods=['POST'])
def start_dialog_route():
    messages = start_dialog()
    return jsonify(messages)