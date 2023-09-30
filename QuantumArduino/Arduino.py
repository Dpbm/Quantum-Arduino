from Board import Board

class Arduino(Board):
    def __init__(self, port="COM0", rate=19200, timeout=0.1):
        """
            Init an Arduino Board

            Arguments:
                port<string>: default="COM0"
                rate<int>: default=19200
                timeout<float>: default=0.1
        """

        super.__init__(port, rate, timeout)
