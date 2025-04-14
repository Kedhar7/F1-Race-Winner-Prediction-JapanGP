import pandas as pd

def parse_time_to_seconds(time_str):

    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            return None
        minutes = float(parts[1])
        seconds = float(parts[2])
        return minutes * 60 + seconds
    except Exception as e:
        print("Error parsing time:", time_str, e)
        return None

def load_2025_qualifying_data_japan():

    data = [
        {"Pos": 1,  "No": 1,  "Driver": "Max Verstappen",    "Car": "Red Bull Racing Honda RBPT",          "Time": "00:01:26.9830000", "Laps": 17},
        {"Pos": 2,  "No": 4,  "Driver": "Lando Norris",      "Car": "McLaren Mercedes",                     "Time": "00:01:26.9950000", "Laps": 15},
        {"Pos": 3,  "No": 81, "Driver": "Oscar Piastri",     "Car": "McLaren Mercedes",                     "Time": "00:01:27.0270000", "Laps": 18},
        {"Pos": 4,  "No": 16, "Driver": "Charles Leclerc",   "Car": "Ferrari",                              "Time": "00:01:27.2990000", "Laps": 21},
        {"Pos": 5,  "No": 63, "Driver": "George Russell",    "Car": "Mercedes",                             "Time": "00:01:27.3180000", "Laps": 17},
        {"Pos": 6,  "No": 12, "Driver": "Kimi Antonelli",    "Car": "Mercedes",                             "Time": "00:01:27.5550000", "Laps": 18},
        {"Pos": 7,  "No": 6,  "Driver": "Isack Hadjar",      "Car": "Racing Bulls Honda RBPT",              "Time": "00:01:27.5690000", "Laps": 18},
        {"Pos": 8,  "No": 44, "Driver": "Lewis Hamilton",    "Car": "Ferrari",                              "Time": "00:01:27.6100000", "Laps": 23},
        {"Pos": 9,  "No": 23, "Driver": "Alexander Albon",   "Car": "Williams Mercedes",                    "Time": "00:01:27.6150000", "Laps": 20},
        {"Pos": 10, "No": 87, "Driver": "Oliver Bearman",    "Car": "Haas Ferrari",                         "Time": "00:01:27.8670000", "Laps": 21},
        {"Pos": 11, "No": 10, "Driver": "Pierre Gasly",      "Car": "Alpine Renault",                       "Time": "00:01:27.8220000", "Laps": 12},
        {"Pos": 12, "No": 55, "Driver": "Carlos Sainz",      "Car": "Williams Mercedes",                    "Time": "00:01:27.8360000", "Laps": 15},
        {"Pos": 13, "No": 14, "Driver": "Fernando Alonso",   "Car": "Aston Martin Aramco Mercedes",         "Time": "00:01:27.8970000", "Laps": 12},
        {"Pos": 14, "No": 30, "Driver": "Liam Lawson",       "Car": "Racing Bulls Honda RBPT",              "Time": "00:01:27.9060000", "Laps": 12},
        {"Pos": 15, "No": 22, "Driver": "Yuki Tsunoda",      "Car": "Red Bull Racing Honda RBPT",           "Time": "00:01:28.0000000", "Laps": 12}
    ]
    df = pd.DataFrame(data)
    df['Time_sec'] = df['Time'].apply(parse_time_to_seconds)
    return df

if __name__ == '__main__':
    df = load_2025_qualifying_data_japan()
    print("Stored 2025 Japanese GP Qualifying (Starting Grid) Data:")
    print(df)
