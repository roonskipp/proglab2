# Oving 6
import random


# update

class BBCON:
    def __init__(self, behav=None, sensob=None, motobs=None, arbitrator=None):
        self.behaviors = [] if behav is None else behav
        self.act_behaviors = []
        self.sensor_objs = [] if sensob is None else sensob
        self.motor_objs = [] if motobs is None else motobs
        self.arbitrator = Arbitrator() if arbitrator is None else arbitrator

    def add_behavior(self, behavior):  # Legger til aktiviteter roboten kan utføre
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):  # Legger til sensor som kan brukes av roboten
        self.sensor_objs.append(sensob)

    def activate_behavior(self,
                          behavior):  # Legger til aktivitet som utføres av roboten nå. Skal kjøre når en behavior starter
        self.act_behaviors.append(behavior)

    def deactivate_behavior(self,
                            behavior):  # Fjerner aktivitet som ikke lenger utføres. Skal kjøre når en behavior er ferdig
        if behavior in self.act_behaviors:
            self.act_behaviors.remove(behavior)

    def run_one_timestep(self):
        # TODO
        # 1. Update all sensobs - These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values (as described below)
        # 2. Update all behaviors - These updates involve reading relevant sensob values and producing a motor recommendation.
        # 3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        # 4. Update the motobs based on these motor recommendations. The motobs will then update the settings of all motors.
        # 5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        # 6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.
        pass


class Sensob:
    """Hovedsaklig gjenstående her, finn ut hva slags data som er relevant å returnere til behaviour-opbjektene.
    gå så i hvert tilfelle av returnValue, og manipuler value slik vi ønsker den og return dette."""

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
            # sensob-objektet jobber med en IR-leser eller en proximity-leser
            if isinstance(value[0], bool):
                # jobber med proximity-leser.
                # behandle dataen på et eller annet vis og returner det
                # TODO
                pass
            else:
                # jobber med IR-leser
                # behandle dataen på et eller annet vis og returner det
                # TODO
                pass

        elif isinstance(value, float):
            # sensob-objektet jobber med ultrasonic-leser
            # behandle dataen på et eller annet vis og returner det
            # TODO
            pass

        else:
            # sensob-objektet jobber med kameraet
            # TODO
            # behandle dataen på et eller annet vis og returner det
            pass


class Motob:
    def __init__(self, motors=None, value=None):
        self.motors = motors
        self.value = value

    def update(self, recommendation):
        # TODO Sjekke denne. Skal laste motor recomandation til value, men vet ikke om value må hentes ut av eller er recomandation
        self.value = recommendation
        self.operationalize()

    def operationalize(self,
                       operation=None):  # Skal utføre motoroperasjonen den har fått, enten via operation eller self.value fra update. Endrer alle motorer i motorlisten til objektet
        use_operation = operation
        if operation is None:
            use_operation = self.value
        for motor in self.motors:
            motor.set_value(use_operation)  # TODO Kan hende vi må endre eller legge til en hjelpeklasse her for å få det til å funke


class Behavior:
    #   Classvariables
    def __init__(self, bbcon, sensobs, priority, behavior_number, motor_recommendations=[], active_flag=False, halt_request=False, match_degree=0, weight=None):
        self.bbcon = bbcon  # BBCON objektet som denne behavioren hører til
        self.sensobs = sensobs  # Liste over de sensob-objektene som behavior-objektet bruker
        self.motor_recommendations = motor_recommendations  # Liste over recommendations en per motob, sendes til arbitratoren
        self.active_flag = active_flag  # Boolean som forteller om denne behavioren er aktiv eller ikke
        self.halt_request = halt_request  # UVISST?? Se dokumentasjonen på behavior i oppgaven
        self.priority = priority  # Statisk, forteller viktigheten til denne behavioren
        self.match_degree = match_degree  # Reelttall, mellom 0 og 1, sier noe om hvor naturlig det er å gjøre denne handlingen
        self.weight = weight  # Produktet av priority og match_degree, brukes for av arbitrator for å bestemme hvilken behavior som skal utføres.
        self.behavior_number = behavior_number  # For å vite hvilken behavior de ulike er.

    def consider_activation(self):  # Sjekker om en inaktiv behavior burde aktiviseres
        # TODO

        values = []
        for sensob in self.sensobs:
            values.append(sensob.getValue())

        if self.behavior_number == 1:  # Stoppe på rød vegg
            # TODO
            pass

        elif self.behavior_number == 2:  # Følg linje
            # TODO
            pass

        elif self.behavior_number == 3:  # Sving til venstre ved vanlig vegg
            if values[0] < 5:
                self.active_flag = True

    def consider_deactivation(self):  # Sjekker om en aktiv behavior burde deaktiviseres
        # TODO

        values = []
        for sensob in self.sensobs:
            values.append(sensob.getValue())

        if self.behavior_number == 1:
            # TODO
            pass

        elif self.behavior_number == 2:
            # TODO
            pass

        elif self.behavior_number == 3:
            self.sensobs[0].update()
            if self.sensobs[0].get_value() > 5:
                self.active_flag = False

    def update(self):
        # TODO
        # Sjekke om behavioren er aktiv eller ikke

        if self.active_flag == True:
            if self.consider_deactivation() == False:
                # Behavior er aktiv og skal forbli aktiv.
                self.sense_and_act()

            elif self.consider_deactivation() == True:
                # Behavior er aktiv, men skal deaktiveres
                self.active_flag = False

        elif self.active_flag == False:
            if self.consider_activation() == True:
                self.active_flag = True
                self.sense_and_act()

    def sense_and_act(self):
        # TODO
        # Må for hver behavior se på values ( sensor data ) og lage motob recommendations, og legge disse i sin egen liste
        # over motob recommendations. Må også oppdatere match_degree basert på dataen, og oppdatere sin egen match degree.
        values = []
        for sensob in self.sensobs:
            values.append(sensob.getValue())

        if self.behavior_number == 1:
            # TODO
            pass

        elif self.behavior_number == 2:
            # TODO
            pass

        elif self.behavior_number == 3:
            self.match_degree = 5 - self.sensobs[0].get_value()
            self.motor_recommendations = [[-1, -1, 1], [1, -1, 1]]


class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):  # Skal ta inn alle aktive behavoirs og velge én av de
        cur_val = 0
        intervall = []
        for act_behv in self.bbcon.act_behaviors:
            intervall.append([cur_val,
                              cur_val + act_behv.weight])  # Lager intervall med størresle bassert på vekten deres. Dvs. hvis du har to behaviors med vekt 0.8 og 0.5 vil intervallet bli [[0, 0.8],[0.8, 1.3]]
            cur_val = cur_val + act_behv
        win_weight = random.randrange(intervall[-1][
                                          -1])  # Velger tilfeldig ut en verdi innenfor intervallet. Større intervall vil da ha større sanns. for å vinne
        for i in range(len(intervall)):
            if win_weight >= intervall[i][0]:
                if win_weight <= intervall[i][1]:  # Sjekker hvilket intervall tallet havnet innenfor og returnerer indexen
                    win_index = i
                    break
        win_behv = self.bbcon.act_behaviors[i]
        return_val = []
        for mr in win_behv.motor_recommendations:  # Lager en liste med alle motorrecommendations for winner behavior pluss en boolean for halt_request på slutten
            return_val.append(mr)
        return_val.append(win_behv.halt_request)

        return return_val


