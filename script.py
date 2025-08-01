import streamlit as st
import pandas as pd

# Dataset from kaggle.com "Car Pricing Regression Dataset"
data = pd.read_csv('car_price.csv')

st.title("Car Pricing Regression Dataset")

# Option
car_option = sorted(data['Make'].unique().tolist())
model_option = sorted(data['Model'].unique().tolist())
fuel_option = sorted(data['Fuel Type'].unique().tolist())
transmission_option = sorted(data['Transmission'].unique().tolist())

min_mileage, max_mileage = int(data['Mileage'].min()), int(data['Mileage'].max()) # The total distance the car has been driven
min_year, max_year = int(data['Year'].min()), int(data['Year'].max()) # The year the car was manufactured or released
min_price, max_price = int(data['Price'].min()), int(data['Price'].max()) # The selling price of the vehicle

# Text
st.markdown("""
    Description: 
    - Make - the manufacturer or brand of the vehicle (e.g., Toyota, BMW, Ford).
    - Model - the variant or trim level of the vehicle, labeled as 'a', 'b', 'c', 'd', or 'e'
    - Year - the year the car was manufactured or released.
    - Engine Size - the engine capacity in liters (L)
    - Mileage - the total distance the car has been driven
    - Fuel Type - the type of gearbox system used in the vehicle
    - Transmission - The type of gearbox system used in the vehicle
    - Price - the selling price of the vehicle
""")

# Filter
selected_car = st.multiselect("Select car:", car_option, default=car_option)
selected_model = st.multiselect("Select model:", model_option, default=model_option)
selected_fuel = st.multiselect("Select fuel:", fuel_option, default=fuel_option)
selected_transmission = st.multiselect("Select transmission:", transmission_option, default=transmission_option)

selected_mileage = st.slider("Select mileage:", min_mileage, max_mileage, (min_mileage, max_mileage))
selected_year = st.slider("Select year:", min_year, max_year, (min_year, max_year))
selected_price = st.slider("Select price:", min_price, max_price, (min_price, max_price))

filtered_data = data.copy()

# Choice
if selected_car:
    filtered_data = filtered_data[filtered_data['Make'].isin(selected_car)]

if selected_model:
    filtered_data = filtered_data[filtered_data['Model'].isin(selected_model)]

if selected_fuel:
    filtered_data = filtered_data[filtered_data['Fuel Type'].isin(selected_fuel)]

if selected_transmission:
    filtered_data = filtered_data[filtered_data['Transmission'].isin(selected_transmission)]

filtered_data = filtered_data[(filtered_data['Mileage'] >= selected_mileage[0]) & (filtered_data['Mileage'] <= selected_mileage[1])]
filtered_data = filtered_data[(filtered_data['Year'] >= selected_year[0]) & (filtered_data['Year'] <= selected_year[1])]
filtered_data = filtered_data[(filtered_data['Price'] >= selected_price[0]) & (filtered_data['Price'] <= selected_price[1])]

st.write("Filtered Data:")
st.write(filtered_data)
st.write(f"Number of matching cars: {len(filtered_data)}")