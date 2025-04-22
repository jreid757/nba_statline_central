from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# Function to retrieve and format player career stats
def stat_retrieval(player_name):
    # Search for player by full name
    player = players.find_players_by_full_name(player_name)

    # If player is not found, return None
    if not player:
        return None

    # Get the player's unique ID and full name
    player_id = player[0]['id']
    player_full_name = player[0]['full_name']

    # Fetch player's career statistics from the NBA API
    career = playercareerstats.PlayerCareerStats(player_id=player_id)

    # Get the DataFrame containing career total stats
    player_avg_df = career.get_data_frames()[1]
    career_averages = player_avg_df.iloc[0]

    # Format the output string
    output = f"\nYou searched for {player_name}, great choice!\n"
    output += f"Here are the career totals for {player_full_name}:\n"
    output += f"\nCareer Totals for {player_full_name}:\n"
    output += f"Points (PTS): {career_averages['PTS']}\n"
    output += f"Assists (AST): {career_averages['AST']}\n"
    output += f"Rebounds (REB): {career_averages['REB']}\n"
    output += f"Steals (STL): {career_averages['STL']}\n"
    output += f"Blocks (BLK): {career_averages['BLK']}\n"

    return output

# Main program loop — runs until user types 'exit'
while True:
    user_input = input("Welcome to NBA Statline Central!\nEnter the first and last name of the NBA player whose career total stats you want to search for and press 'enter'.\nType 'exit' to quit the program.\n\n")

    if user_input.lower() == "exit":
        print("Thanks for using NBA Statline Central!")
        break

    # Fetch and display stats if player exists
    user_input_search = stat_retrieval(user_input)

    if user_input_search:
        print(user_input_search)
    else:
        print(f"No player found with the name '{user_input}'. Could be a misspell, try again!")
