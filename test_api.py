import requests
import json
from datetime import datetime

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
    url = "https://web-production-15cb5.up.railway.app/calculate_macros"  # Replace with your actual Railway URL
    
    # Prepare output content
    output_content = []
    output_content.append(f"Test Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output_content.append("=" * 50)
    output_content.append(f"Testing endpoint: {url}")
    output_content.append(f"Test data: {json.dumps(test_data, indent=2)}")
    output_content.append("")
    
    try:
        # Send POST request
        response = requests.post(url, json=test_data)
        
        output_content.append(f"Status Code: {response.status_code}")
        output_content.append(f"Response: {json.dumps(response.json(), indent=2)}")
        
    except requests.exceptions.ConnectionError:
        output_content.append("Error: Could not connect to the server. Make sure the Flask app is running.")
    except Exception as e:
        output_content.append(f"Error: {e}")
    
    # Write output to file
    with open('testoutput', 'w') as f:
        f.write('\n'.join(output_content))
    
    print("Test completed. Results written to 'testoutput' file.")

if __name__ == "__main__":
    test_calculate_macros() 