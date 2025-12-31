from flask import Flask, render_template, request
import requests
import os
import random
from datetime import datetime
from dotenv import load_dotenv
import numpy as np
from sklearn.ensemble import RandomForestRegressor

load_dotenv()
app = Flask(__name__)

# Simplified forecaster for Vercel
def predict_trend():
    return random.randint(60, 95)

@app.route('/')
def trending_topics():
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        return "API key missing! Set NEWS_API_KEY in Vercel environment variables"
    
    # In production, you'd fetch real data here
    news = []
    for i in range(5):
        score = predict_trend()
        news.append({
            'id': i,
            'title': f"Breaking News #{i+1}",
            'source': random.choice(['CNN', 'NBC News', 'ABC News']),
            'image': 'https://via.placeholder.com/300x200?text=USA+News',
            'description': 'This is a simulated news story for demonstration',
            'time_ago': f"{random.randint(1, 60)}m ago",
            'trend_score': score,
            'trend_category': "High Potential" if score >= 80 else "Medium Potential" if score >= 60 else "Low Potential",
            'forecast': "High probability to trend nationally within 12 hours" if score >= 80 else "Likely to gain traction in regional markets within 24 hours"
        })
    
    return render_template('trending.html', 
                          news=news,
                          current_date=datetime.now().strftime('%A, %B %d, %Y'))

if __name__ == '__main__':
    app.run()
