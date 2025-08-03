import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("airlines_flights_data.csv")
st.title("Airlines Flights Data")
data.drop(["index"], axis=1, inplace=True)
st.write(data)
st.write("Length table:", len(data))

st.header("Airline selector")
# Option
airline_option = sorted(data['airline'].unique().tolist())
source_city_option = sorted(data['source_city'].unique().tolist())
departure_time_option = sorted(data['departure_time'].unique().tolist())
class_option = sorted(data['class'].unique().tolist())

min_duration, max_duration = int(data['duration'].min()), int(data['duration'].max())
min_price, max_price = int(data['price'].min()), int(data['price'].max())

# Selector
airline_selector = st.multiselect("Select airline:", airline_option, default=airline_option)
source_city_selector = st.multiselect("Select source city:", source_city_option, default=source_city_option)
departure_time_selector = st.multiselect("Select departure time:", departure_time_option, default=departure_time_option)
class_selector = st.multiselect("Select class:", class_option, default=class_option)

duration_selector = st.slider("Select duration:", min_duration, max_duration, (min_duration, max_duration))
price_selector = st.slider("Select price", min_price, max_price, (min_price, max_price))

filtered_data = data.copy()

if airline_selector:
    filtered_data = filtered_data[filtered_data['airline'].isin(airline_selector)]

if source_city_selector:
    filtered_data = filtered_data[filtered_data['source_city'].isin(source_city_selector)]

if departure_time_selector:
    filtered_data = filtered_data[filtered_data['departure_time'].isin(departure_time_selector)]

if class_selector:
    filtered_data = filtered_data[filtered_data['class'].isin(class_selector)]

filtered_data = filtered_data[(filtered_data['duration'] >= duration_selector[0]) & (filtered_data['duration'] <= duration_selector[1])]
filtered_data = filtered_data[(filtered_data['price'] >= price_selector[0]) & (filtered_data['price'] <= price_selector[1])]

# Result
st.subheader("Filtered data")
st.write(filtered_data)
st.write(f"Number of matching airlines: {len(filtered_data)}")

st.header("Group data")
st.subheader("Count of classes")
st.write(data['class'].value_counts())
st.bar_chart(data['class'].value_counts())

st.subheader("Earnings of airlines")
earnings_of_airline = data.groupby('airline')['price'].sum().sort_values(ascending=False)
earnings_of_airline_df = earnings_of_airline.reset_index(name="earnings")
st.write(earnings_of_airline_df)
st.bar_chart(earnings_of_airline_df.set_index('airline'))

st.subheader("Отчет по количеству рейсов по авиакомпаниям")
st.write(data["airline"].value_counts())
st.bar_chart(data["airline"].value_counts())

st.subheader("Средняя цена билета по классам")
avg_price_by_class = data.groupby('class')['price'].mean()
st.write(avg_price_by_class)
plt.figure(figsize=(4, 3))
plt.pie(avg_price_by_class, labels=avg_price_by_class.index)
plt.axis("equal")
st.pyplot(plt)

st.subheader("Количество остановок по авиакомпаниям")
avg_stops_by_airline = data.groupby('airline')['stops'].count().sort_values(ascending=False)
st.write(avg_stops_by_airline)
st.bar_chart(avg_stops_by_airline)

st.subheader("Сравнение цен по авиакомпаниям")
avg_price_by_airline = data.groupby("airline")['price'].mean().sort_values(ascending=False)
st.write(avg_price_by_airline)
st.bar_chart(avg_price_by_airline)