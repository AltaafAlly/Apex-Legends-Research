import requests
from bs4 import BeautifulSoup
import csv

def scrape_steam_usernames(url, num_pages):
    usernames = []
    
    for page in range(1, num_pages + 1):
        response = requests.get(f'{url}&p={page}')
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all review cards (adjust the selector based on the actual HTML structure)
        review_cards = soup.find_all('div', class_='apphub_CardContentAuthorName')
        
        for review in review_cards:
            username_element = review.find('a', href=True)
            if username_element:
                username = username_element.get_text().strip()
                usernames.append(username)
    
    return usernames

def save_to_csv(usernames, filename='steam_usernames.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username'])
        for username in usernames:
            writer.writerow([username])

# URL of the Steam Apex Legends reviews page
base_url = 'https://steamcommunity.com/app/1172470/reviews/?browsefilter=toprated&snr=1_5_100010_'

# Number of pages to scrape
num_pages = 1  # Adjust as needed

usernames = scrape_steam_usernames(base_url, num_pages)
save_to_csv(usernames)

print(f'Saved {len(usernames)} usernames to steam_usernames.csv')
