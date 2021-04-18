import matplotlib.pyplot as plt
import serial.tools.list_ports
import time

def get_com_port_number(expected_hwid):
    """This function returns COM port of a requested device. Do not remove delay - it is required to detect device as soon as it iterates in the system.

    Returns:
        [str]: [COM port]
    """
    for i in range(100):
        time.sleep(0.05)
        ser_list = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ser_list):
            our_hwid = format(hwid)
            our_com = format(port)
            if expected_hwid in our_hwid:
                return  our_com
    return "nie wykryto urzadzenia"


def read_data(seconds, port):
    datapoints = []
    with serial.Serial(port, timeout=0, parity="N") as ser:
        start = time.time()
        while (time.time() - start < seconds):
            a = ser.readline()
            if len(a) <3:
                continue
            a = a.decode()
            datapoints.append(a)
    return datapoints

def plot_data(datapoints):
    plt.plot(datapoints)
    plt.show()
    
    
if __name__ == '__main__':
    com_p = get_com_port_number("0483")
    with open("odczyt.txt", "w+") as inf:
        d = read_data(20, com_p)
        for i in d:
            inf.writelines(str(i))
        plot_data(d)
        