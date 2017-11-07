#Oving 6


class BBCON:

    def __init__(self, behav=None, sensob=None, motobs=None, arbitrator=None):
        self.behaviors = [] if behav is None else behav
        self.act_behaviors = []
        self.sensor_objs = [] if sensob is None else sensob
        self.motor_objs = [] if motobs is None else motobs
        self.arbitrator = Arbitrator() if arbitrator is None else arbitrator

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensor_objs.append(sensob)

    def activate_behavior(self, behavior):
        self.act_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavoir in self.act_behaviors:
            self.act_behaviors.remove(behavior)

    def run_one_timestep(self):
        #TODO
        pass


class Sensob:
    # TODO
    pass


class Motob:
    # TODO
    pass


class Behavior:
    # TODO
    pass


class Arbitrator:
    # TODO
    pass

