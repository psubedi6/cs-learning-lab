class SensorReading:
    unit = "°C"
    def __init__(self, sensor_id, temperature,  location):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.location = location
        
sensor = SensorReading("S-101", 23.8, "Warehouse")
print(f"{sensor.sensor_id}\n{sensor.temperature}\n{sensor.location}\n{sensor.unit}")