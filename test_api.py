import requests
import json

def test_calculate_macros():
    """Test the calculate_macros endpoint"""
    
    # Test data - sample ingredients
    test_data = {
        "ingredients": [
            "2 large eggs",
            "1 cup all-purpose flour", 
            "1/2 tsp baking powder",
            "1/4 cup milk",
            "1 tbsp butter"
        ],
        "title": "Simple Pancakes",
        "servings": 2
    }
    
    # API endpoint URL - replace with your Railway URL
    url = "https://recipe-nutrition-mvp-backend-production.up.railway.app/calculate_macros"  # Replace with your actual Railway URL
    
    try:
        # Send POST request
        response = requests.post(url, json=test_data)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure the Flask app is running.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_calculate_macros() 