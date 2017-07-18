## LIBRARIES ##
from sense_hat import SenseHat
from datetime import datetime

## LOGGING SETTINGS ##
FILENAME = ""
WRITE_FREQUENCY = 50

## FUNCTIONS ##
def log_data():
  output_string = ",".join(str(value) for value in sense_data)
  batch_data.append(output_string)

def get_sense_data():
  sense_data=[]

  sense_data.append(sense.get_temperature_from_humidity())
  sense_data.append(sense.get_temperature_from_pressure())
  sense_data.append(sense.get_humidity())
  sense_data.append(sense.get_pressure())

  sense_data.append(datetime.now())

  return sense_data

def file_setup(filename):
  header  =["temp_h","temp_p","humidity","pressure","timestamp"]

  with open(filename,"w") as f:
      f.write(",".join(str(value) for value in header)+ "\n")

## MAIN PROGRAM ##
sense = SenseHat()

batch_data= []

if FILENAME == "":
  filename = "SenseLog-"+str(datetime.now())+".csv"
else:
  filename = FILENAME+"-"+str(datetime.now())+".csv"

file_setup(filename)

while True:
  sense_data = get_sense_data()
  log_data()

  if len(batch_data) >= WRITE_FREQUENCY:
      print("Writing to file..")
      with open(filename,"a") as f:
          for line in batch_data:
              f.write(line + "\n")
          batch_data = []
