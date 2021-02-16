import pyvisa


# ser = serial.Serial("/dev/cu.usbserial-1410", timeout=1)      # USB-RS232
# ser = serial.Serial("/dev/cu.usbmodem481G201021", timeout=1)    #USBVCOM


class BKPrecision2840:
    def __init__(self, USBVCOM='ASRL2::INSTR'):
        """Connect to BK_Precision_2840 DC resistance meter through USBVCOM."""
        rm = pyvisa.ResourceManager()
        self.inst = rm.open_resource(USBVCOM)
        # self.resistance_data = []

    def get_resistance(self):
        resistance = self.inst.query('FETCh:AUTO 1')
        return resistance
        # self.resistance_data.append(resistance)








