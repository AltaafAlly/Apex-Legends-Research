import requests
from bs4 import BeautifulSoup
import csv

def scrape_usernames(base_url, num_pages):
    usernames = []
    
    for page in range(1, num_pages + 1):
        url = f'{base_url}/{page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Adjust the selector based on the actual HTML structure of the leaderboard page
        player_elements = soup.find_all('a', {'style': 'color:white;', 'target': '_alsLeaderboard'})
        
        for player in player_elements:
            username = player.get_text().strip()
            usernames.append(username)
    
    return usernames

def save_to_csv(usernames, filename='usernames_for_Xbox_players.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username'])
        for username in usernames:
            writer.writerow([username])
            print('username added')

# Base URL for the leaderboard
base_url = 'https://apexlegendsstatus.com/leaderboard/Global/career_kills/X1'

# Number of pages to scrape
num_pages = 40  # Adjust as needed

usernames = scrape_usernames(base_url, num_pages)
save_to_csv(usernames)

print(f'Saved {len(usernames)} usernames to usernames.csv')
