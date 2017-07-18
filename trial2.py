from sense_hat import SenseHat
import csv
sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    data = (t,p,h)

with open(data.csv, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

    # msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)

    # sense.show_message(msg, scroll_speed=0.05)