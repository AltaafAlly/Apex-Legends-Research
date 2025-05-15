import requests
from bs4 import BeautifulSoup
import csv
import time
import os

# List of legends to scrape
legends = [
    'Bangalore', 'Fuse', 'Ash', 'Mad Maggie', 'Ballistic',
    'Pathfinder', 'Wraith', 'Octane', 'Revenant', 'Horizon', 'Valkyrie', 'Alter',
    'Bloodhound', 'Crypto', 'Seer', 'Vantage',
    'Gibraltar', 'Lifeline', 'Mirage', 'Loba', 'Newcastle', 'Conduit',
    'Caustic', 'Wattson', 'Rampart', 'Catalyst'
]

# Base URL for damage leaderboard
base_url = 'https://apexlegendsstatus.com/leaderboard/{}/damage/ANY/{}'

# Add a directory to save the CSV files
output_directory = 'damage_data'


# Create the directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to scrape damage data and save to CSV page-by-page
def scrape_damage_data(legend):
    csv_filename = os.path.join(output_directory, f"{legend}_damage.csv")
    
    # Open the CSV file once and keep appending to it as pages are scraped
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Damage"])  # Write the column header

        for page in range(1, 21):  # Loop over pages 1 to 20
            url = base_url.format(legend, page)
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f"Failed to retrieve data for {legend}, page {page}. Skipping...")
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all damage elements in the page
            damage_elements = soup.find_all('span', style='color: white; font-size: 20px;')
            
            if not damage_elements:
                print(f"No data found for {legend}, page {page}.")
            
            for damage_element in damage_elements:
                damage_count = damage_element.text.strip().replace(",", "")  # Remove commas
                writer.writerow([damage_count])  # Write the damage count directly to CSV
            
            print(f"Page {page} for {legend} scraped and saved successfully.")
            
            # Wait for 10 seconds before moving to the next page
            #time.sleep(1)

# Main loop to iterate over all legends for damage data
for legend in legends:
    print(f"Scraping damage data for {legend}...")
    scrape_damage_data(legend)
    
    # Wait for 30 seconds before moving to the next legend
    print(f"Finished scraping data for {legend}. Waiting 30 seconds before moving to the next legend...")
    time.sleep(30)

print("Scraping completed.")
