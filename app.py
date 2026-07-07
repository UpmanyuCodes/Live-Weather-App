import streamlit as st
import requests
import time

def get_weather(city):
    api_key = st.secrets["api_key"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    return data

st.title("Weather App")

with st.form("weather_form"):

    city = st.text_input("Enter the city")

    search = st.form_submit_button("Search")

if search:
    if city.strip() == "":
        st.warning("Please enter the city")
    else:
        with st.spinner("Fetching weather..."):
            time.sleep(2)
            data = get_weather(city)
        
            if data["cod"] == 200:
                city_name = data["name"]

                temperature = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]

                    wind_speed = data["wind"]["speed"]

                condition = data["weather"][0]["main"]

                icon = data["weather"][0]["icon"]

                icon_url = f"https://openweathermap.org/img/wn/{icon}@4x.png"

                st.subheader(city_name)

                st.image(icon_url, width=120)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Temperature", f"{temperature} °C")
                    st.metric("Humidity", f"{humidity}%")

                with col2:
                    st.metric("Feels Like", f"{feels_like} °C")
                    st.metric("Wind Speed", f"{wind_speed} m/s")

                st.subheader(f" {condition}")

            else:
                st.error("City not found!")