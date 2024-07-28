import sqlite3
import matplotlib.pyplot as plt

# Define the database name
db_name = 'population_SM.db'

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS population (
    city TEXT,
    year INTEGER,
    population INTEGER
)
''')

# Data for 10 cities in Florida
cities_data = [
    ('Miami', 2023, 470914),
    ('Orlando', 2023, 307573),
    ('Tampa', 2023, 425257),
    ('Jacksonville', 2023, 929647),
    ('St. Petersburg', 2023, 263255),
    ('Hialeah', 2023, 234517),
    ('Tallahassee', 2023, 201658),
    ('Fort Lauderdale', 2023, 188191),
    ('Gainesville', 2023, 133857),
    ('Cape Coral', 2023, 204451)
]

# Insert data into the table
cursor.executemany('''
INSERT INTO population (city, year, population)
VALUES (?, ?, ?)
''', cities_data)


# Function to simulate population growth
def simulate_population_growth(city, initial_year, years=20, growth_rate=0.02):
    cursor.execute('SELECT population FROM population WHERE city = ? AND year = ?', (city, initial_year))
    initial_population = cursor.fetchone()[0]

    # Generate population for each year
    population_data = []
    for i in range(1, years + 1):
        new_year = initial_year + i
        new_population = int(initial_population * (1 + growth_rate) ** i)
        population_data.append((city, new_year, new_population))

    # Insert simulated data into the table
    cursor.executemany('''
    INSERT INTO population (city, year, population)
    VALUES (?, ?, ?)
    ''', population_data)


# Simulate and insert data for each city
cities = [city for city, _, _ in cities_data]
for city in cities:
    simulate_population_growth(city, 2023)

# Commit and close connection
conn.commit()
conn.close()


# Function to plot population growth
def plot_population_growth(city):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Fetch data for the specified city
    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (city,))
    data = cursor.fetchall()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth for {city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.xticks(years, rotation=45)
    plt.tight_layout()
    plt.show()


# Provide options to the user and plot the chosen city's data
def main():
    cities = [
        'Miami', 'Orlando', 'Tampa', 'Jacksonville',
        'St. Petersburg', 'Hialeah', 'Tallahassee',
        'Fort Lauderdale', 'Gainesville', 'Cape Coral'
    ]

    print("Available cities:")
    for idx, city in enumerate(cities, 1):
        print(f"{idx}. {city}")

    choice = int(input("Enter the number corresponding to the city you want to view: "))
    if 1 <= choice <= len(cities):
        chosen_city = cities[choice - 1]
        plot_population_growth(chosen_city)
    else:
        print("Invalid choice.")


# Run the main function
if __name__ == '__main__':
    main()
