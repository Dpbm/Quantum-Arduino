class Board:
    serial = None

    def __init__(self, port, rate, timeout):
        """
            Init Serial Board

            Arguments:
                port<string>
                rate<int>
                timeout<float>
        """


        from serial import Serial
        
        self.serial  = Serial(port=port, baudrate=rate, timeout=timeout)



