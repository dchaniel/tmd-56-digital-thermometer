#!/usr/bin/env python3

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