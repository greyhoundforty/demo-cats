import os
import requests
from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def get_random_cat_image():
    """Fetch a random cat image URL from a free API"""
    try:
        # Primary: The Cat API - more reliable, no API key required for basic usage
        response = requests.get('https://api.thecatapi.com/v1/images/search', timeout=10)
        response.raise_for_status()
        data = response.json()
        if data and len(data) > 0:
            return data[0].get('url', '')
    except requests.RequestException as e:
        app.logger.error(f"Error fetching from The Cat API: {e}")
    
    try:
        # Fallback 1: CATAAS (Cat as a Service)
        response = requests.get('https://cataas.com/cat?json', timeout=10)
        response.raise_for_status()
        data = response.json()
        cat_id = data.get('_id', '')
        if cat_id:
            return f'https://cataas.com/cat/{cat_id}'
    except requests.RequestException as e:
        app.logger.error(f"Error fetching from CATAAS: {e}")
    
    # Final fallback to placeholder service
    app.logger.warning("All cat APIs failed, using placeholder")
    return 'https://placekitten.com/800/600'

@app.route('/')
def index():
    """Main page displaying a random cat image"""
    cat_image_url = get_random_cat_image()
    return render_template('index.html', cat_image_url=cat_image_url)

@app.route('/api/cat')
def api_cat():
    """API endpoint to get a new random cat image"""
    cat_image_url = get_random_cat_image()
    return jsonify({'image_url': cat_image_url})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)