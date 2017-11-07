class BBCON():
    # TODO
    pass

class Sensob():

    def __init__(self, type):
        self.object = type

    def update(self):
        self.object.update()

    def getValue(self):
        self.object.get_value()

    def reset(self):
        self.object.reset()

    def returnValue(self):
        self.update()
        value = self.getValue()

        if isinstance(value, list):
            # sensob-objektet jobber med en IR-leser
            # TODO
            pass

        elif isinstance(value, float):
            # sensob-objektet jobber med ultrasonic-leser
            # TODO
            pass

        else:
            # sensob-objektet jobber med kameraet
            # TODO
            pass


class Motob():
    # TODO
    pass

class Behavior():
    # TODO
    pass

class Arbitrator():
    # TODO
    pass
