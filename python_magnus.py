
class BBCON:

    def __init__(self, behav=None, sensob=None, motobs=None, arbitrator=None):
        self.behaviors = [] if behav is None else behav
        self.act_behaviors = []
        self.sensor_objs = [] if sensob is None else sensob
        self.motor_objs = [] if motobs is None else motobs
        self.arbitrator = Arbitrator() if arbitrator is None else arbitrator

    def add_behavior(self, behavior): # Legger til aktiviteter roboten kan utføre
        self.behaviors.append(behavior)

    def add_sensob(self, sensob): # Legger til sensor som kan brukes av roboten
        self.sensor_objs.append(sensob)

    def activate_behavior(self, behavior): # Legger til aktivitet som utføres av roboten nå. Skal kjøre når en behavior starter
        self.act_behaviors.append(behavior)

    def deactivate_behavior(self, behavior): # Fjerner aktivitet som ikke lenger utføres. Skal kjøre når en behavior er ferdig
        if behavior in self.act_behaviors:
            self.act_behaviors.remove(behavior)

    def run_one_timestep(self):
        #TODO
        # 1. Update all sensobs - These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values (as described below)
        # 2. Update all behaviors - These updates involve reading relevant sensob values and producing a motor recommendation.
        # 3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        # 4. Update the motobs based on these motor recommendations. The motobs will then update the settings of all motors.
        # 5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        # 6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.
        pass

class Sensob:
    pass


class Motob:

    def __init__(self, motors=None, value=None):
        self.motors = motors
        self.value = value

    def update(self, recommendation):
        #TODO Sjekke denne. Skal laste motor recomandation til value, men vet ikke om value må hentes ut av eller er recomandation
        self.value = recommendation
        self.operationalize()

    def operationalize(self, operation=None): # Skal utføre motoroperasjonen den har fått, enten via operation eller self.value fra update. Endrer alle motorer i motorlisten til objektet
        use_operation = operation
        if operation is None:
            use_operation = self.value
        for motor in self.motors:
            motor.set_value(use_operation)

class Behavior:
    pass


class Arbitrator:
    pass

