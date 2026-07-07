# Live Weather App

A simple weather application built with Streamlit and the OpenWeatherMap API. It allows users to search for any city and view current weather information.

## Features

- Search weather by city
- Current temperature
- Feels like temperature
- Humidity
- Wind speed
- Weather condition and icon
- Error handling for invalid cities
- Secure API key using Streamlit Secrets

## Technologies Used

- Python
- Streamlit
- Requests
- OpenWeatherMap API

## Installation

```bash
git clone https://github.com/UpmanyuCodes/Live-Weather-App.git
cd Live-Weather-App
pip install streamlit requests
streamlit run app.py
```

Create `.streamlit/secrets.toml` and add:

```toml
API_KEY = "YOUR_API_KEY"
```

## Author

Upmanyu Singh
