"""
CP1404 Practical
Wimbleton
Estimate: 40 minutes
Actual: 50 minutes
"""

FILEPATH = "C:/Users/kfurn/Documents/UNI/2022/CP1404/Pracs/CP1404Pracs/prac_05/wimbledon.csv"

def main():
    """call functions to get, process and display relevant data"""
    data = get_data(FILEPATH)
    winner_to_wins, countries = process_data(data)
    display_data(winner_to_wins, countries)

def get_data(FILEPATH):
    """opens and cleans data from csv file"""
    data = []
    with open(FILEPATH, "r", encoding='cp1252') as in_file:
        for line in in_file:
            line = line.strip().split(',')
            data.append(line)
        data.pop(0)
        return data

def process_data(data):
    """iterates through all winners to determine their number of
    wins and their unique winning countries"""
    winner_to_wins = {}
    countries = []
    for item in data:
        if item[2] in winner_to_wins:
            winner_to_wins[item[2]] += 1
        else:
            winner_to_wins[item[2]] = 1
            if item[1] not in countries:
                countries.append(item[1])
    return winner_to_wins, countries

def display_data(winner_to_wins, countries):
    """Display and format results of data processing"""
    countries = ', '.join(map(str, sorted(countries)))
    print("Wimbledon Champions:")
    for winner in winner_to_wins.items():
        print(f"{winner[0]} {winner[1]}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(countries)

main()
