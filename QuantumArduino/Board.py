class Board:
    serial_connection = None

    def __init__(self, port, rate, timeout):
        """
            Init Serial Board

            Arguments:
                port<string>
                rate<int>
                timeout<float>
        """

        from serial import Serial
        self.serial_connection  = Serial(port=port, baudrate=rate, timeout=timeout)



