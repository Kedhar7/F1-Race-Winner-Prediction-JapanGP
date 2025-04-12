import fastf1
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from quali_data_japan import load_2025_qualifying_data_japan

def main():
    fastf1.Cache.enable_cache('cache')
    
    session_2024 = fastf1.get_session(2024, 'Japanese Grand Prix', 'R')
    session_2024.load()
    
    laps = session_2024.laps[['Driver', 'LapTime']].copy()
    laps.dropna(subset=['LapTime'], inplace=True)
    laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()
    race_avg = laps.groupby('Driver')['LapTimeSeconds'].mean().reset_index()
    race_avg.rename(columns={'LapTimeSeconds': 'AvgLapTime2024'}, inplace=True)
    
    quali_2025 = load_2025_qualifying_data_japan()
    
    mapping = {
        'Lando Norris': 'NOR',
        'Max Verstappen': 'VER',
        'Lewis Hamilton': 'HAM',
        'Charles Leclerc': 'LEC',
        'Carlos Sainz': 'SAI',
        'Oscar Piastri': 'PIA',
        'George Russell': 'RUS',
        'Fernando Alonso': 'ALO',
        'Pierre Gasly': 'GAS',
        'Yuki Tsunoda': 'TSU'
    }
    quali_2025['DriverCode'] = quali_2025['Driver'].map(mapping)
    
    merged = quali_2025.merge(race_avg, left_on='DriverCode', right_on='Driver', how='left', suffixes=('_quali', '_race'))
    merged.dropna(subset=['AvgLapTime2024'], inplace=True)
    
    if merged.empty:
        print("No matching driver data found between 2024 Race and 2025 Qualifying.")
        return
    
    X = merged[['AvgLapTime2024', 'Time_sec']]
    y = merged['AvgLapTime2024']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print("Mean Absolute Error on test set: {:.3f} seconds".format(mae))
    
    merged['PredictedRaceLapTime'] = model.predict(X)
    merged.sort_values('PredictedRaceLapTime', inplace=True)
    merged['PredictedPosition'] = range(1, len(merged) + 1)
    merged['PredictedPosition'] = merged['PredictedPosition'].apply(lambda x: f'P{x}')
    
    print("\nPredicted Race Results for 2025 Japanese GP (following YouTube demo approach):")
    print(merged[['PredictedPosition', 'Driver_quali', 'Time_sec', 'AvgLapTime2024', 'PredictedRaceLapTime']])
    
    predicted_winner = merged.iloc[0]['Driver_quali']
    print("\nPredicted winner for the 2025 Japanese Grand Prix:", predicted_winner)

if __name__ == "__main__":
    main()
