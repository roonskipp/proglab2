
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

# 1. Update all sensobs - These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values (as described below)
# 2. Update all behaviors - These updates involve reading relevant sensob values and producing a motor recommendation.
# 3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
# 4. Update the motobs based on these motor recommendations. The motobs will then update the settings of all motors.
# 5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
# 6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.

class Sensob:
    pass


class Motob:
    pass


class Behavior:
    pass


class Arbitrator:
    pass

