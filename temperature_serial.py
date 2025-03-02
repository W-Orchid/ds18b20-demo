import serial

# Configure the serial connection
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Change 'COM3' to your port (e.g., '/dev/ttyUSB0' for Linux)

try:
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            data = ser.readline().decode('utf-8').strip()
            print(data)
finally:
    ser.close()
