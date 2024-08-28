# # import csv
# # import requests
# # import time

# # # API details
# # API_KEY = "22d0d035f3ebf343a5684221dc355c7f"
# # API_ENDPOINT = "https://api.mozambiquehe.re/nametouid"

# # # Function to get UID from username using the API
# # def get_uid_from_username(username, platform="PC"):
# #     try:
# #         response = requests.get(
# #             API_ENDPOINT,
# #             params={
# #                 "auth": API_KEY,
# #                 "player": username,
# #                 "platform": platform  # Default is PC, can be changed to X1 (Xbox) or PS4
# #             },
# #             timeout=10  # Timeout after 10 seconds
# #         )
# #         if response.status_code == 200:
# #             data = response.json()
# #             return data.get("uid")  # Adjust this according to the actual response format
# #         else:
# #             print(f"Failed to get UID for {username}: {response.status_code}, {response.text}")
# #             return None
# #     except requests.exceptions.Timeout:
# #         print(f"Request for {username} timed out.")
# #         return None
# #     except requests.exceptions.RequestException as e:
# #         print(f"Request exception for {username}: {e}")
# #         return None

# # # Function to read usernames from a CSV file with UTF-8 encoding, skipping the first line
# # def read_usernames_from_csv(file_path):
# #     usernames = []
# #     with open(file_path, mode='r', newline='', encoding='utf-8') as file:
# #         reader = csv.reader(file)
# #         next(reader)  # Skip the header
# #         for row in reader:
# #             usernames.append(row[0])  # Assuming usernames are in the first column
# #     return usernames

# # # Main script
# # def main():
# #     input_file = "Data_Retrieval/CSV_files/Usernames/usernames_for_PC_players.csv"  # Replace with the path to your input CSV file
# #     output_file = "Data_Retrieval/CSV_files/Usernames/usernames_with_uids_for_PC.csv"  # Output file to save usernames and UIDs

# #     usernames = read_usernames_from_csv(input_file)

# #     with open(output_file, mode='w', newline='', encoding='utf-8') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["Username", "UID"])  # Write header

# #         for index, username in enumerate(usernames):
# #             print(f"Processing {index + 1}/{len(usernames)}: {username}")  # Debugging info
# #             uid = get_uid_from_username(username)
# #             writer.writerow([username, uid])  # Write the username and UID to the CSV file immediately
# #             time.sleep(5)  # Add a delay to avoid hitting API rate limits

# #     print(f"UIDs saved to {output_file}")

# # if __name__ == "__main__":
# #     main()


# import csv
# import requests
# from bs4 import BeautifulSoup
# import time

# # API details
# API_KEY = "22d0d035f3ebf343a5684221dc355c7f"
# API_ENDPOINT = "https://api.mozambiquehe.re/nametouid"

# # Function to get Origin username from the player's profile page
# def get_origin_username(username):
#     profile_url = f"https://apexlegendsstatus.com/profile/PC/{username}"
#     try:
#         response = requests.get(profile_url)
#         if response.status_code == 200:
#             time.sleep(10)
#             soup = BeautifulSoup(response.content, 'html.parser')
#             # Print relevant HTML section for debugging
#             relevant_section = soup.find_all('p')  # Get all <p> tags
#             for section in relevant_section:
#                 print(section.prettify())  # Print each <p> tag content
#                 if section.find('img', {'src': '/lib/img/origin.svg'}):
#                     # Extract text after finding the img tag
#                     full_text = section.get_text()
#                     origin_username = full_text.split(';')[-1].replace("&nbsp;", "").strip()
#                     return origin_username
#             print(f"No Origin username found for {username}.")
#             return None
#         else:
#             print(f"Failed to retrieve profile for {username}: {response.status_code}")
#             return None
#     except Exception as e:
#         print(f"Error while fetching Origin username from {username}: {e}")
#         return None

# # Function to get UID from Origin username using the API
# def get_uid_from_origin_username(origin_username, platform="PC"):
#     try:
#         response = requests.get(
#             API_ENDPOINT,
#             params={
#                 "auth": API_KEY,
#                 "player": origin_username,
#                 "platform": platform  # Default is PC
#             },
#             timeout=10  # Timeout after 10 seconds
#         )
#         if response.status_code == 200:
#             data = response.json()
#             return data.get("uid")  # Adjust this according to the actual response format
#         else:
#             print(f"Failed to get UID for {origin_username}: {response.status_code}, {response.text}")
#             return None
#     except requests.exceptions.Timeout:
#         print(f"Request for {origin_username} timed out.")
#         return None
#     except requests.exceptions.RequestException as e:
#         print(f"Request exception for {origin_username}: {e}")
#         return None

# # Function to read usernames and UIDs from the CSV file
# def read_usernames_and_uids(file_path):
#     data = []
#     with open(file_path, mode='r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header
#         for row in reader:
#             username, uid = row[0], row[1]
#             data.append((username, uid))
#     return data

# # Function to save usernames and UIDs to a CSV file
# def save_uids_to_csv(data, output_file):
#     with open(output_file, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Username", "UID"])  # Write header
#         for username, uid in data:
#             writer.writerow([username, uid])

# # Main script
# def main():
#     input_file = "Data_Retrieval/CSV_files/Usernames/usernames_with_uids_for_PC.csv"  # File with missing UIDs
#     output_file = "Data_Retrieval/CSV_files/Usernames/usernames_with_uids_filled.csv"  # Output file with filled UIDs

#     data = read_usernames_and_uids(input_file)

#     updated_data = []
#     for username, uid in data:
#         if not uid:  # Check if UID is missing
#             print(f"Retrieving Origin username for {username} from profile page...")
#             origin_username = get_origin_username(username)
#             if origin_username:
#                 print(f"Origin username found: {origin_username}. Retrieving UID...")
#                 uid = get_uid_from_origin_username(origin_username)
#             time.sleep(2)  # To avoid hitting rate limits
#         updated_data.append((username, uid))

#     save_uids_to_csv(updated_data, output_file)
#     print(f"UIDs saved to {output_file}")

# if __name__ == "__main__":
#     main()

import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape UIDs and usernames from a given URL
def extract_uids_from_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <a> tags with href containing '/profile/uid/PC/'
            uid_links = soup.find_all('a', href=True)
            
            uids = []
            for link in uid_links:
                href = link['href']
                # Check if the href attribute contains '/profile/uid/PC/'
                if '/profile/uid/PC/' in href:
                    # Extract the UID part from the href
                    uid = href.split('/profile/uid/PC/')[1]  # Get the part after '/profile/uid/PC/'
                    username = link.get_text().strip()  # Get the player's name
                    uids.append((username, uid))
                    print(f"Extracted UID: {uid}, Username: {username}")
            return uids
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to scrape UIDs from multiple pages and save to a CSV file
def scrape_uids_to_csv(base_url, pages, output_file):
    unique_uids = set()  # Use a set to avoid duplicates

    # Open the CSV file to write
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "UID"])  # Write the header

        for page in range(1, pages + 1):
            page_url = f"{base_url}/{page}"
            print(f"Scraping page: {page_url}")
            uids = extract_uids_from_page(page_url)
            if uids:
                for username, uid in uids:
                    if uid not in unique_uids:  # Check if UID is already added
                        writer.writerow([username, uid])
                        unique_uids.add(uid)
            else:
                print(f"No UIDs found on page {page}")

            time.sleep(10)  # Add a 10-second delay after each page fetch

    print(f"Scraping completed. UIDs saved to {output_file}")

# Base URL for leaderboard pages
base_leaderboard_url = 'https://apexlegendsstatus.com/leaderboard/Global/career_kills/PC'
total_pages = 40  # Number of pages to scrape

# Output CSV file path
output_csv_file = "Data_Retrieval/CSV_files/Usernames/usernames_with_uids_for_PC.csv"

# Scrape the UIDs and save them to the CSV file
scrape_uids_to_csv(base_leaderboard_url, total_pages, output_csv_file)








