import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter the city : ")
search = st.button("Search")

if search:
    api_key = "8a102003c189ebd5a92a2aac607ae6cd"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()
    
    

    if data["cod"] == 200:
        city_name = data["name"]
        temperature = data["main"]["temp"]
        felt_tem = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["main"]

        st.subheader(city_name)
        st.metric("Temperature", f"{temperature} °C")
        st.metric("You may feel like : ",f"{felt_tem} °C")
        st.metric("Humidity : ",f"{humidity} %")
        st.metric("Wind speed : ",f"{wind_speed} m/s")
        st.metric("Conditions : ",condition)


    else:
        st.error("City not found")

    icon = data["weather"][0]["icon"]

    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    st.image(icon_url)

    

