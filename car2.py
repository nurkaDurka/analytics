import streamlit as st
import pandas as pd

# Dataset from kaggle.com "Car Pricing Regression Dataset"
data = pd.read_csv('car_price.csv')

st.title("Car Pricing Regression Statistics")

# Make
st.subheader("Statistics by Make(count)")
make_counts = data['Make'].value_counts()
st.bar_chart(make_counts)

# Model
st.subheader("Statistics by Model(count)")
model_counts = data['Model'].value_counts()
st.bar_chart(model_counts)

# Year
st.subheader("Statistics by Year(count)")
year_counts = data['Year'].value_counts()
st.bar_chart(year_counts)

# Price
st.header("Statistics by Price(the cheapest and the most expensive)")
st.subheader("The cheapest car")
car_min = data.sort_values(by=['Price'], ascending=True).head()
st.write(car_min)

st.subheader("The most expensive car")
car_max = data.sort_values(by=['Price'], ascending=False).head()
st.write(car_max)

# Mileage
st.header("Statistics by Mileage")
st.subheader("The lowest mileage")
mileage_min = data.sort_values(by=['Mileage'], ascending=True).head()
st.write(mileage_min)

st.subheader("The longest mileage")
mileage_max = data.sort_values(by=['Mileage'], ascending=False).head()
st.write(mileage_max)

# Fuel Type
st.subheader("Statistics by Fuel Type(count)")
st.write("Count of Fuel(Diesel):", len(data[data["Fuel Type"] == "Diesel"].value_counts()))
st.write("Count of Fuel(Petrol):", len(data[data["Fuel Type"] == "Petrol"].value_counts()))
st.write("Count of Fuel(Electric):", len(data[data["Fuel Type"] == "Electric"].value_counts()))

# Transmission
st.subheader("Statistics by Transmission(count)")
st.write("Count of Transmission(Manual):", len(data[data["Transmission"] == "Manual"].value_counts()))
st.write("Count of Transmission(Automatic):", len(data[data["Transmission"] == "Automatic"].value_counts()))

# Generalized statistics
st.title("Generalized statistics")
st.subheader("Change in average prices of cars by year")
mean_price_by_year = data.groupby('Year')['Price'].mean()
st.line_chart(mean_price_by_year)

st.subheader("Average mileages of cars by make since 2015")
mean_mileage_by_make = data[data['Year'] > 2015].groupby('Make')['Mileage'].mean()
st.line_chart(mean_mileage_by_make)

st.subheader("Average engine size of cars")
mean_engine_size_by_make = data.groupby('Make')['Engine Size'].mean()
st.bar_chart(mean_engine_size_by_make)
