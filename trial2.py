import keen
from sense_hat import SenseHat
from datetime import datetime

keen.project_id = "596e366ec9e77c00015d99e3"
keen.write_key = "4C65FC4CAFC0EBF6BDD3919989C27C23A591DE227A92E8E1C45DBB8D7E84500EC6AACF57D8BC361877F923B8DC457B08C083BABAB80083FA67E14D7C3B355C1EB34FBE1E8D140543B608C08AEAA1737C9778C30159EE74351BE56327C5FD1F5C"

def record_data():
    sense = SenseHat()

    d = get_timestamp()
    t = sense.temperature
    h = sense.humidity
    values = (d, t, h)

keen.add_event("data", {
  "device": "hodor",
  "time_stamp": d,
  "temperature": t,
  "humidity": h
})


def get_timestamp():
    dt = datetime.now()
    dt_date = str(dt.date())
    dt_time = str(dt.time())
    timestamp = "%s %s" % (dt_date, dt_time[:8])
    return timestamp

 def main():
    record_data()

if __name__ == '__main__':
    main()