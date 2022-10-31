"""
CP1404 Practical
Wimbleton
Wimbleton data reading, analysis and display
Estimate: 40 minutes
Actual: 50 minutes
"""

FILEPATH = "wimbledon.csv"


def main():
    """call functions to get, process and display relevant """
    records = get_data(FILEPATH)
    winner_to_count, countries = process_data(records)
    display_data(winner_to_count, countries)


def get_data(FILEPATH):
    """opens and cleans data from csv file"""
    records = []
    with open(FILEPATH, "r", encoding='cp1252') as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip().split(',')
            records.append(line)
        return records


def process_data(records):
    """Creates dictionary of winners and list of countries from data"""
    winner_to_count = {}
    countries = []
    for item in records:
        if item[2] in winner_to_count:
            winner_to_count[item[2]] += 1
        else:
            winner_to_count[item[2]] = 1
            if item[1] not in countries:
                countries.append(item[1])
    return winner_to_count, countries


def display_data(winner_to_count, countries):
    """Display and format results of data processing"""
    countries = ', '.join(map(str, sorted(countries)))
    print("Wimbledon Champions:")
    for winner in winner_to_count.items():
        print(f"{winner[0]} {winner[1]}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(countries)


main()