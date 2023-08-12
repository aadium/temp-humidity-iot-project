from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import csv

# InfluxDB 2.0 connection settings
INFLUXDB_URL = "http://ec2-15-184-201-178.me-south-1.compute.amazonaws.com:8086"
INFLUXDB_TOKEN = "sg0OVg_vlc_TGjh_9LB_mq3RtaXZc6rzKtb9GEMK20zerWEe8YgDOVeuxq2AApk6ysLKlfA4vjv3KBgPWvQSnA=="
INFLUXDB_ORG = "AU"
INFLUXDB_BUCKET = "IoT_bucket"

# Path to the CSV data file on your local machine
CSV_FILE_PATH = "sensor_data.csv"

# Function to read data from the CSV file
def read_csv_data(csv_file):
    data_points = [] # The data points would store each retrived field
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            timestamp, temperature, humidity, heat_index = row
            # the data point for the current field is defined here
            data_point = {
                "time": timestamp,
                "temperature": float(temperature),
                "humidity": float(humidity),
                "heat_index": float(heat_index),
            }
            data_points.append(data_point) # This data point is appended into the data_points array
    return data_points

def upload_data_to_influxdb(data_points):
    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN) # The client object is defined here
    write_api = client.write_api(write_options=SYNCHRONOUS) # the write_api object to write the data into the InfluxDB 2.0 Database is defined here

    for data_point in data_points:
        # We define a point object that stores the data in the flux query syntax
        point = Point("environment_data") \
            .time(data_point["time"], WritePrecision.NS) \
            .field("temperature", data_point["temperature"]) \
            .field("humidity", data_point["humidity"]) \
            .field("heat_index", data_point["heat_index"]) \
            .tag("location", "Testing")

        print(point)
        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point) # The point object is written into the database
        print('Point written')
        print()

    print("Data uploaded to InfluxDB 2.0")

def main():
    data_points = read_csv_data(csv_file=CSV_FILE_PATH) # The data_points list is equated to the list returned by the read_csv_data function
    upload_data_to_influxdb(data_points=data_points) # The list objects are now uploaded into InfluxDB 2.0

if __name__ == "__main__":
    main()
