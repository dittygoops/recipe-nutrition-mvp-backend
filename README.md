# Recipe Nutrition MVP Backend

A Flask application that calculates nutritional macros for recipes using the Spoonacular API.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Spoonacular API key: `SPOONACULAR_API_KEY=your_actual_api_key_here`
   - You can get a free API key from [Spoonacular](https://spoonacular.com/food-api)

## Running the Application

Start the Flask server:
```bash
python server.py
```

The server will run on `http://localhost:5000`

## API Endpoints

### POST /calculate_macros

Calculate nutritional information for a list of ingredients.

**Request Body:**
```json
{
  "ingredients": [
    "2 large eggs",
    "1 cup all-purpose flour",
    "1/2 tsp baking powder"
  ],
  "title": "Simple Pancakes",
  "servings": 2
}
```

**Response:**
```json
{
  "success": true,
  "nutrition_data": {
    // Spoonacular API response with nutrition information
  }
}
```

### GET /health

Health check endpoint to verify the server is running.

## Testing

Run the test script to see the API in action:
```bash
python test_api.py
```

## Example Usage with curl

```bash
curl -X POST http://localhost:5000/calculate_macros \
  -H "Content-Type: application/json" \
  -d '{
    "ingredients": [
      "2 large eggs",
      "1 cup all-purpose flour",
      "1/2 tsp baking powder"
    ],
    "title": "Simple Pancakes",
    "servings": 2
  }'
```

## Railway Deployment

To deploy on Railway:

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Python app and use the `Procfile`
3. Add your environment variables in Railway dashboard:
   - `SPOONACULAR_API_KEY`: Your Spoonacular API key
4. Deploy!

## Notes

- The application sends a POST request to Spoonacular's `/recipes/analyze` endpoint
- Ingredients should be formatted as strings with amounts and units (e.g., "1 cup flour")
- The API key is included as a query parameter in the Spoonacular API request
- Error handling is included for network issues and API errors
- The app automatically uses the `PORT` environment variable provided by Railway 