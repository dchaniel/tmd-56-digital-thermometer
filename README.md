# TMD56 Temperature Sensor Library

This Python library provides an interface for the Amprobe TMD-56 Multi-logging Digital Thermometer. This thermometer is an internet favorite for temperature logging for coffee roasting. 

The library allows easy reading of temperature data from the sensor via a serial connection.

## Installation

1. Ensure you have Python 3.6 or later installed on your system.

2. Install the required `pyserial` library:

   ```
   pip install pyserial
   ```

3. Download the `tmd56.py` file and place it in your project directory or Python path.

## Usage

Here's a basic example of how to use the TMD56 library:

```python
from tmd56 import TMD56, list_serial_ports

def main():
    # List available serial ports
    print("Available serial ports:")
    for port in list_serial_ports():
        print(f"  {port}")

    # You may want to prompt the user to select a port or use a configuration file
    device = "/dev/tty.usbserial-AK05FW1M"  # Example for macOS

    # Create TMD56 instance
    tmd56 = TMD56(device)

    # Get temperature readings
    t1, t2 = tmd56.get_temperature()
    print(f"Temperature readings: {t1}, {t2}")

if __name__ == "__main__":
    main()
```