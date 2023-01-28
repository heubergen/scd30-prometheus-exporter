# scd30-prometheus-exporter
A prometheus exporter that reads data from the SCD-30 CO2 sensor

It's expected that the sensor is connected and calibrated. Otherwise, please read the manuals from the vendor how to do this.

## Installation
Only steps for Debian are provided, for other distros or OS they might differ.
1. `sudo apt install python pip`
2. `mkdir /opt/co2-exporter`
3. `cp server.py /opt/co2-exporter/`
4. `cp co2-exporter.service /etc/systemd/system/`
5. `sudo systemctl enable co2-exporter`
6. `pip install prometheus-client`
7. Setup the access to the sensor for python. If you have the adafruit that runs e.g. with a Raspberry PI check out [Adafruit_CircuitPython_SCD30](https://github.com/adafruit/Adafruit_CircuitPython_SCD30)
8. Edit /opt/co2-exporter/server.py with your favorite editor and change the temperature offset if needed
9. `sudo systemctl start co2-exporter`
