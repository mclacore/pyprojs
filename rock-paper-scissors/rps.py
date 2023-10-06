from flask import Flask, render_template, request
import random
import os
import psycopg2

db_params = {
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'database': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD')
}

app = Flask(__name__)

# Create the game history table
@app.before_first_request
def create_game_history_table():
    conn = psycopg2.connect(**db_params)
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
    return options[random.randint(0,2)]

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

    # Insert game history into the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    query = "INSERT INTO game_history (player_choice, computer_choice, winner) VALUES (%s, %s, %s)"
    data = (player_choice, computer_choice, winner)
    cursor.execute(query, data)

    conn.commit()
    cursor.close()
    conn.close()

    return winner

@app.route('/', methods=['GET', 'POST'])
def index():
    create_game_history_table()  # Make sure the table exists

    if request.method == 'POST':
        if request.form.get('play_again') == 'Play Again':
            return render_template("index.html")
    return render_template("index.html")

@app.route('/rps/<choice>')
def rps(choice):
    player_choice = choice.lower()    
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)
    
    return render_template("rps.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)

@app.route('/history')
def history():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    query = "SELECT * FROM game_history"
    cursor.execute(query)
    game_history = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("history.html", game_history=game_history)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)