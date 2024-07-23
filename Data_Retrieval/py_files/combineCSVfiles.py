import csv

def read_csv_column(file_path, column_name):
    values = set()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            value = row.get(column_name)
            if value:
                values.add(value)
    return values

def find_duplicates(file1, file2, column_name):
    values1 = read_csv_column(file1, column_name)
    values2 = read_csv_column(file2, column_name)

    duplicates = values1.intersection(values2)
    return duplicates

# Example usage
file1 = 'usernames_for_PS_players.csv'  # Replace with the path to your first CSV file
file2 = 'usernames_for_Xbox_players.csv'  # Replace with the path to your second CSV file
column_name = 'Username'  # Replace with the name of the column to check for duplicates

duplicates = find_duplicates(file1, file2, column_name)

if duplicates:
    print("Duplicate values found:")
    for value in duplicates:
        print(value)
else:
    print("No duplicate values found.")

