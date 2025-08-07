from flask import Flask, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')

@app.route('/calculate_macros', methods=['POST'])
def calculate_macros():
    """
    Calculate nutritional macros for a list of ingredients using Spoonacular API
    """
    try:
        # Get ingredients from request body
        data = request.get_json()
        
        if not data or 'ingredients' not in data:
            return jsonify({'error': 'Ingredients list is required'}), 400
        
        ingredients = data['ingredients']
        
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            return jsonify({'error': 'Ingredients must be a non-empty list'}), 400
        
        # Prepare the request to Spoonacular API
        api_url = f"https://api.spoonacular.com/recipes/analyze?apiKey={SPOONACULAR_API_KEY}&includeNutrition=true"
        
        payload = {
            "ingredients": ingredients
        }
        
        # Optional: include title and servings if provided
        if 'title' in data:
            payload['title'] = data['title']
        if 'servings' in data:
            payload['servings'] = data['servings']
        
        # Send POST request to Spoonacular API
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(api_url, json=payload, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            nutrition_data = response.json()
            return jsonify({
                'success': True,
                'nutrition_data': nutrition_data
            })
        else:
            return jsonify({
                'error': f'Spoonacular API error: {response.status_code}',
                'details': response.text
            }), response.status_code
            
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Network error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Flask app is running'})

if __name__ == '__main__':
    # Get port from environment variable (for Railway) or default to 5000
    port = int(os.getenv('PORT', 5000))
    # Only use Flask's development server for local development
    app.run(debug=False, host='0.0.0.0', port=port)
