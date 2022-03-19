import time
import prometheus_client
from prometheus_client import start_http_server, Summary
import board
import adafruit_scd30

i2c = board.I2C()   # uses board.SCL and board.SDA
scd = adafruit_scd30.SCD30(i2c)

scd.temperature_offset = 2 #change if needed

CO2_GAUGE = prometheus_client.Gauge("co2_ppm", "CO2 in ppm")
TEMPERATURE_GAUGE = prometheus_client.Gauge("temperature_celcius", "Temperature in Celcius")
HUMIDITY_GAUGE = prometheus_client.Gauge("humidity_percent", "Humidity percentage")

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        CO2_GAUGE.set(scd.CO2)
        TEMPERATURE_GAUGE.set(scd.temperature)
        HUMIDITY_GAUGE.set(scd.relative_humidity)
        time.sleep(840)