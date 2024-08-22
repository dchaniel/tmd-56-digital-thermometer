import serial
import time

class TMD56:
    # TMD56 constants
    ACK_BYTE0 = 0x3e
    ACK_BYTE1 = 0x0f
    TEMP1_HI = 5
    TEMP1_LO = 6
    TEMP2_HI = 10
    TEMP2_LO = 11

    def __init__(self, device, logfile="/tmp/tmd56log.txt", retries=10):
        self.device = device
        self.logfile = logfile
        self.retries = retries

    def device_read(self):
        with serial.Serial(self.device, baudrate=19200, bytesize=8, parity='E', stopbits=1, timeout=1) as ser:
            command = "#0A0000NA2\r\n" 
            ser.write(command.encode())
            data = b''
            start_time = time.time()
            while len(data) < 16:
                chunk = ser.read(16 - len(data))
                if chunk:
                    data += chunk
                if time.time() - start_time > 1:  # 1 second timeout
                    break
        return data if len(data) == 16 else None

    def get_temperature(self):
        with open(self.logfile, 'a+') as log:
            try:
                for i in range(self.retries):
                    r = self.device_read()
                    breakpoint()
                    if r is None:
                        print("no data returned", file=log)
                        continue
                    if (r[0] == self.ACK_BYTE0) and (r[1] == self.ACK_BYTE1):
                        t1 = ((r[self.TEMP1_HI] << 8) | r[self.TEMP1_LO])/10.0
                        t2 = ((r[self.TEMP2_HI] << 8) | r[self.TEMP2_LO])/10.0
                        if (i > 1):
                            print(f"good data ({t1},{t2}) found after {i} retries", file=log)
                        return t1, t2
                    else:
                        print("bad data found: ", end="", file=log)
                        print(" ".join(f"{b:02x}" for b in r), file=log)

                
                return 0, 0

            except serial.SerialException as e:
                print(e)
                print(e, file=log)
                return 0, 0

def list_serial_ports():
    import serial.tools.list_ports
    return [port.device for port in serial.tools.list_ports.comports()]