from flask import Flask, render_template, request
import random
import os
import psycopg2
from datetime import datetime

db_params = {
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
}

app = Flask(__name__)

def create_database():
    conn = psycopg2.connect(**db_params)
    
    conn.pytocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT 1 from pg_database WHERE datname='gamehistory'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("CREATE DATABASE gamehistory")
    cursor.close()
    conn.close()
    
create_database()

@app.before_first_request
def create_game_history_table():
    conn = psycopg2.connect(database='gamehistory', **db_params)
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS game_history (
        id SERIAL PRIMARY KEY,
        player_choice VARCHAR(10),
        computer_choice VARCHAR(10),
        winner VARCHAR(10),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def get_computer_move():
    options = ["rock", "paper", "scissors"]
    return options[random.randint(0, 2)]

def get_winner(player_choice, computer_choice):
    winner = "computer"

    if player_choice == computer_choice:
        winner = "tie"
    if player_choice == "rock" and computer_choice == "scissors":
        winner = "you"
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "you"
    if player_choice == "paper" and computer_choice == "rock":
        winner = "you"

    return winner

@app.route('/', methods=['GET', 'POST'])
def index():
    create_game_history_table()

    if request.method == 'POST':
        if request.form.get('play_again') == 'Play Again':
            return render_template("index.html")
    return render_template("index.html")


@app.route('/rps/<choice>')
def rps(choice):
    player_choice = choice.lower()
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)

    # Write the game outcome to the PostgreSQL database
    save_game_to_database(player_choice, computer_choice, winner)

    return render_template("rps.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)

@app.route('/history')
def history():
    # Retrieve game history from the PostgreSQL database
    game_history = retrieve_game_history_from_database()
    return render_template("history.html", game_history=game_history)

def save_game_to_database(player_choice, computer_choice, winner):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    query = """
    INSERT INTO game_history (player_choice, computer_choice, winner, created_at)
    VALUES (%s, %s, %s, %s)
    """
    current_time = datetime.now()
    cursor.execute(query, (player_choice, computer_choice, winner, current_time))
    conn.commit()
    cursor.close()
    conn.close()

def retrieve_game_history_from_database():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    query = """
    SELECT * FROM game_history
    """
    cursor.execute(query)
    game_history = cursor.fetchall()
    cursor.close()
    conn.close()
    return game_history

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
