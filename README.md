# Weather Chatbot

A simple Flask-based chatbot that fetches real-time weather data using the OpenWeatherMap API. Enter a city name, and it returns the current weather information.

## Features

- Real-time weather updates  
- Accepts natural language city input  
- Displays temperature, humidity, and weather conditions  
- Built using Python, Flask, and OpenWeatherMap API

## Project Structure

```
weather-chatbot/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
└── templates/
    └── index.html       # User interface
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-chatbot.git
cd weather-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the API key

- Create a free account at [https://openweathermap.org/api](https://openweathermap.org/api)  
- Copy your API key  
- In `app.py`, replace:

```python
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
```

with your actual key

### 4. Run the chatbot

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Example Usage

**User Input:**  
`Pune`

**Response:**  
`The weather in Pune is 30°C with clear skies and 45% humidity.`

## Technologies Used

- Python 3  
- Flask  
- HTML/CSS  
- OpenWeatherMap API

## Future Enhancements

- Voice input integration  
- Multi-day forecasts  
- Auto-detect user location

## Author

Arpita Kotnis  
Founder of Lumizenz | ENTC @ COEP

## License

This project is licensed under the M
