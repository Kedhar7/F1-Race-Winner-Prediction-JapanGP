# 🏎️ F1 2025 Japanese Grand Prix Prediction

A lightweight machine learning project that predicts the outcome of the 2025 Japanese Grand Prix using real Formula 1 data from the FastF1 API.


## 📌 Overview

This project combines historical race data and current season qualifying data to predict race performance. It uses a machine learning model to estimate lap times and determine the most likely finishing order.


## 🔧 What It Does

- Loads 2024 Japanese GP race data via FastF1  
- Combines with 2025 qualifying times  
- Trains a Gradient Boosting Regressor to predict race lap pace  
- Outputs a sorted prediction of race results and the winner  


## ✅ Results

- 🥇 Predicted Winner: Max Verstappen (✅ matched real result)  
- 🥈 Predicted P2: Lando Norris (✅ also matched real result)  
- 📉 Mean Absolute Error (MAE): 0.156 seconds  
- 📊 Several other top positions closely aligned with actual results  


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/f1-japan-2025-prediction.git
cd f1-japan-2025-prediction
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Cache Directory for FastF1

FastF1 uses a local cache to store session data.

```bash
mkdir cache
```

Also ensure your script includes:

```python
import fastf1
fastf1.Cache.enable_cache('cache')
```

### 5. Run the Prediction

```bash
python prediction_japan_2025.py
```


## 📁 Project Structure

| File                   | Description                            |
|------------------------|----------------------------------------|
| prediction_japan_2025.py | Main script for race prediction       |
| quali_data_japan.py      | 2025 qualifying data (manually entered) |
| requirements.txt         | Python package dependencies           |


## 🧠 Built With

- Python  
- FastF1  
- Pandas  
- NumPy  
- scikit-learn  


## 📈 Highlights

- ✅ Predicted Max Verstappen as race winner  
- ✅ Predicted Lando Norris in P2  
- 📉 MAE of just 0.156s, showing strong model reliability  
- 🏁 Predictions align closely with actual top finishers  


## 🔮 Future Enhancements

- Include FP1, FP2, FP3 practice session data  
- Expand to full 2025 season race predictions  
- Add a Streamlit UI for interactive prediction visualization


## 📜 License

MIT License
