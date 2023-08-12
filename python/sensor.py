from matplotlib import pyplot as plt
import numpy as np
import csv
from datetime import datetime, timedelta

def calculate_heat_index(temperature, humidity):
    # Convert Celsius temperature to Fahrenheit
    T = (temperature * 9/5) + 32
    RH = humidity

    # Calculate the heat index
    heat_index = ((-42.379) + 2.04901523*T + 10.14333127*RH - 0.22475541*T*RH - 0.00683783*T*T - 0.05481717*RH*RH + 0.00122874*T*T*RH + 0.00085282*T*RH*RH - 0.00000199*T*T*RH*RH)
    heat_index = (heat_index - 32) * (5/9)

    if heat_index < temperature:
        return temperature
    else:
        return heat_index

def simulate_sensor_data(num_samples, initial_temp, temp_variance, initial_humidity, humidity_variance):
    # Generate random noise for temperature and humidity
    temp_noise = np.random.normal(0, temp_variance, num_samples)
    humidity_noise = np.random.normal(0, humidity_variance, num_samples)

    # Initialize lists to store timestamp, temperature, humidity, and heat index data
    timestamp_data = []
    temperature_data = []
    humidity_data = []
    heat_index_data = []

    # Set initial values
    temperature = initial_temp
    humidity = initial_humidity

    # Set initial timestamp to midnight (00:00)
    current_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0, 0)

    # Simulate the sensor data
    for i in range(num_samples):
        # Calculate the new temperature and humidity values with noise
        new_temperature = temperature + temp_noise[i]
        new_humidity = humidity + humidity_noise[i]

        # Ensure that the temperature and humidity values do not go negative
        if new_temperature < initial_temp:
            new_temperature = initial_temp
        if new_humidity < initial_humidity:
            new_humidity = initial_humidity

        # Calculate the heat index for the new temperature and humidity
        heat_index = calculate_heat_index(new_temperature, new_humidity)

        # Add timestamp, temperature, humidity, and heat index to the lists
        timestamp_data.append(current_time.strftime('%H:%M'))
        temperature_data.append(new_temperature)
        humidity_data.append(new_humidity)
        heat_index_data.append(heat_index)

        # Update temperature and humidity for the next data point
        temperature = new_temperature
        humidity = new_humidity

        # Increment the time by 1 minute for the next data point
        current_time += timedelta(minutes=1)

        # Stop the simulation if it reaches 23:59
        if current_time.hour == 24 and current_time.minute == 0:
            break

    return timestamp_data, temperature_data, humidity_data, heat_index_data

def read_csv_data(csv_file):
    timestamp_data = []
    temperature_data = []
    humidity_data = []
    
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            timestamp, temperature, humidity = row
            timestamp_data.append(timestamp)
            temperature_data.append(float(temperature))
            humidity_data.append(float(humidity))
    
    return timestamp_data, temperature_data, humidity_data

def plot_data(timestamp_data, temperature_data, humidity_data):
    time = range(len(timestamp_data))
    plt.plot(time, temperature_data, label='Temperature (Celsius)')
    plt.plot(time, humidity_data, label='Humidity (%)')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Sensor Value')
    plt.legend()
    plt.grid(True)
    plt.title('Simulated Temperature and Humidity Sensor Data')
    plt.show()

def main():
    num_samples = 1440  # Simulate data for 24 hours (1 minute intervals)
    initial_temp = 5.0
    temp_variance = 0.4
    initial_humidity = 21.0
    humidity_variance = 0.2
    
    timestamp_data, temperature_data, humidity_data, heat_index_data = simulate_sensor_data(num_samples, initial_temp, temp_variance, initial_humidity, humidity_variance)
    
    # Save the data to a CSV file
    with open("sensor_data.csv", "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Timestamp", "Temperature (Celsius)", "Humidity (%)", "Heat Index"])
        for timestamp, temperature, humidity, heat_index in zip(timestamp_data, temperature_data, humidity_data, heat_index_data):
            csvwriter.writerow([timestamp, temperature, humidity, heat_index])

    print("Data saved to sensor_data.csv")

if __name__ == "__main__":
    main()
