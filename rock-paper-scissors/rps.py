from flask import Flask, render_template, request
import random
import os
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Azure Storage Account endpoint
storage_account_url = os.environ['STORAGE_ENDPOINT']

# Authenticate using managed identity
credential = DefaultAzureCredential()

# Create a blob service client
blob_service_client = BlobServiceClient(account_url=storage_account_url, credential=credential)

def create_blob_container():
    # Check if the container exists
    containers = blob_service_client.list_containers()
    for container in containers:
        if container.name == 'game-history':
            return 'game-history'

    # Create a blob container if it doesn't exist
    blob_service_client.create_container('game-history', public_access='blob')
    return 'game-history'

container_name = create_blob_container()

def save_game_to_blob(player_choice, computer_choice, winner):
    # Create a blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='game_history.log')

    # Retrieve existing log or create a new one
    try:
        existing_log = blob_client.download_blob().content_as_text()
    except:
        existing_log = ""

    # Append the game result to the existing log
    log_data = f"{datetime.now()} - Player Choice: {player_choice}, Computer Choice: {computer_choice}, Winner: {winner}\n"
    updated_log = existing_log + log_data

    # Upload the updated log to the blob
    blob_client.upload_blob(updated_log, overwrite=True)

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
    if request.method == 'POST':
        if request.form.get('play_again') == 'Play Again':
            return render_template("index.html")
    return render_template("index.html")


@app.route('/rps/<choice>')
def rps(choice):
    player_choice = choice.lower()
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)

    # Write the game outcome to the Azure Storage Account Blob
    save_game_to_blob(player_choice, computer_choice, winner)

    return render_template("rps.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)

@app.route('/history')
def history():
    # Retrieve game history from the Azure Storage Account Blob
    game_history = retrieve_game_history_from_blob()
    return render_template("history.html", game_history=game_history)

def retrieve_game_history_from_blob():
    # Create a blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='game_history.log')

    # Download and return the game history log
    try:
        game_history = blob_client.download_blob().content_as_text()
    except:
        game_history = "No game history available."
    
    # Process the game history log
    game_history_lines = game_history.split('\n')
    parsed_game_history = []
    for line in game_history_lines:
        if line.strip():  # Skip empty lines
            parts = line.split(' - ')
            if len(parts) == 2:
                timestamp_str, game_data = parts
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
                game_data_parts = game_data.split(', ')
                if len(game_data_parts) == 3:
                    player_choice = game_data_parts[0].split(': ')[1]
                    computer_choice = game_data_parts[1].split(': ')[1]
                    winner = game_data_parts[2].split(': ')[1]
                    parsed_game_history.append((timestamp, player_choice, computer_choice, winner))
    
    return parsed_game_history

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)