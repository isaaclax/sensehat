from sense_hat import SenseHat
from datetime import datetime

def get_sense_data():
  sense_data=[]

  sense_data.append(sense.get_temperature_from_humidity())
  sense_data.append(sense.get_temperature_from_pressure())
  sense_data.append(sense.get_humidity())
  sense_data.append(sense.get_pressure())

  sense_data.append(datetime.now())

  return sense_data

def main():

  sense = SenseHat()

  while True:
    sense_data = get_sense_data()
    print(sense_data)
