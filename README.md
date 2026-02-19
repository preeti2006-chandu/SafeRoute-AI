# SafeRoute AI 🚦

AI-based Safe Route Recommendation system using:
- Flask (Backend API)
- OpenStreetMap + Leaflet (Frontend)
- ML model to predict route safety based on:
  - Crime rate
  - Lighting
  - Crowd level

## Features
- Shows route on map
- Predicts risk level (Low / Medium / High)
- Uses OpenStreetMap (no Google API cost)

## How to Run
```bash
pip install -r requirements.txt
python app.py
