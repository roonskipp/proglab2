#Oving 6
import random
import time
from irproximity_sensor import IRProximitySensor
from motors import Motors
from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from camera import Camera
from imager2 import Imager
#update

class BBCON:

    def __init__(self, behav=None, sensob=None, motobs=None, arbitrator=None):
        self.behaviors = [] if behav is None else behav
        self.act_behaviors = []
        self.sensor_objs = [] if sensob is None else sensob
        self.motor_objs = [] if motobs is None else motobs
        self.arbitrator = Arbitrator(self) if arbitrator is None else arbitrator

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
        breakProg = False
        #TODO
        # 1. Update all sensobs - These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values (as described below)
        for sensob in self.sensor_objs:
            sensob.update()
        print("Har kjørt 1")
        # 2. Update all behaviors - These updates involve reading relevant sensob values and producing a motor recommendation.
        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag and behavior not in self.act_behaviors:
                self.activate_behavior(behavior)
            elif not behavior.active_flag and behavior in self.act_behaviors:
                self.deactivate_behavior(behavior)
        print("Har kjørt 2")
        # 3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        arbitratorResult = self.arbitrator.choose_action()
        print("Har kjørt 3")
        # 4. Update the motobs based on these motor recommendations. The motobs will then update the settings of all motors.
        if arbitratorResult[1]:
            return True
        for motob in self.motor_objs:
            motob.update(arbitratorResult[0])
        print("Har kjørt 4")
        # 5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        sleepingTime = 0
        for x in range(len(arbitratorResult[0])):
            sleepingTime += arbitratorResult[0][x][2]
        time.sleep(sleepingTime)
        print("Har kjørt 5")
        # 6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.
        print("Har kjørt 6")
        for sensob in self.sensor_objs:
            sensob.reset()
        return False


class Sensob:
    """Hovedsaklig gjenstående her, finn ut hva slags data som er relevant å returnere til behaviour-opbjektene.
    gå så i hvert tilfelle av returnValue, og manipuler value slik vi ønsker den og return dette."""
    def __init__(self, type):
        self.object = type

    def update(self):
        self.object.update()

    def getValue(self):
        return self.object.get_value()

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
        self.value = recommendation
        self.operationalize()

    def operationalize(self, operation=None): # Skal utføre motoroperasjonen den har fått, enten via operation eller self.value fra update. Endrer alle motorer i motorlisten til objektet
        use_operation = operation
        if operation is None:
            use_operation = self.value
        for motor in self.motors:
            print("motor recommendations som skal kjøre:", use_operation)
            for rec in use_operation:
                motor.set_value(rec)
                time.sleep(rec[2])
            
class Behavior:
    #   Classvariables
    def __init__(self, bbcon, sensobs, motor_recommendations, active_flag, halt_request, priority, match_degree, weight, behavior_number):
        self.bbcon = bbcon                                           # BBCON objektet som denne behavioren hører til
        self.sensobs = sensobs                                       # Liste over de sensob-objektene som behavior-objektet bruker
        self.motor_recommendations = motor_recommendations           # Liste over recommendations en per motob, sendes til arbitratoren
        self.active_flag = active_flag                               # Boolean som forteller om denne behavioren er aktiv eller ikke
        self.halt_request = halt_request                             # UVISST?? Se dokumentasjonen på behavior i oppgaven
        self.priority = priority                                     # Statisk, forteller viktigheten til denne behavioren
        self.match_degree = match_degree                             # Reelttall, mellom 0 og 1, sier noe om hvor naturlig det er å gjøre denne handlingen
        self.weight = weight                                         # Produktet av priority og match_degree, brukes for av arbitrator for å bestemme hvilken behavior som skal utføres.
        self.behavior_number = behavior_number                       # For å vite hvilken behavior de ulike er

    def consider_activation(self):

        values = []
        for sensob in self.sensobs:
            values.append(sensob.getValue())

        if self.behavior_number == 1:
            # MÅ DEFINERES I MAIN AT BEHAVIOR 1 objektet (kamera behavior) har avstandsmåler som andre sensob
            # slik at avstandsmåleren havner i slot 2 på values
            print(values)
            distance = values[1]
            if distance < 4:
                return True

        elif self.behavior_number == 2:
            # values er her en liste som inneholder liste med 6 verdier (1 p/ sensor)
            for value in values[0]:
                if value < 0.1: # sjekker om verdien på en av sensorene tilavarer sort -> nådd edge, MÅ endre retning
                    return True

        elif self.behavior_number == 3:
            if values[0] < 5:
                self.active_flag = True
                return True
            for surface_color in values[0]:
                if not -0.1 < surface_color <  + 0.1:
                    return True

        elif self.behavior_number == 4: # Bare kjører fremover, lav prioritet slik at hvis ingenting annet skjer, så kjører den fremover.
            return True

    def consider_deactivation(self):
        # TODO

        values = []
        for sensob in self.sensobs:
            values.append(sensob.getValue())

        if self.behavior_number == 1:
            distance = values[1]
            if distance > 4:
                return True
            return False

        elif self.behavior_number == 2:
            for value in values[0]:
                if value < 0.1:  # kan ikke deaktiveres dersom sort kant fortsatt er tilstede
                    return False
                return True

        elif self.behavior_number == 3:
            self.sensobs[0].update()
            if self.sensobs[0].getValue() > 5:
                return True
            return False

        elif self.behavior_number == 4: # vi vil ikke at denne skal deaktiveres
            return False

    def update(self):
        # TODO
        # Sjekke om behavioren er aktiv eller ikke

        if self.active_flag:
            if self.consider_deactivation() == False:
                # Behavior er aktiv og skal forbli aktiv.
                self.sense_and_act()

            elif self.consider_deactivation() == True:
                # Behavior er aktiv, men skal deaktiveres
                self.active_flag = False

        else:
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
        print("Sense and act er kalt...")
        # bilde, stoppe på rød vegg = behavior nr1
        if self.behavior_number == 1:
            # TODO
            # Her har values bare 1 element, et pil objekt
            imageObject = values[0]
            hits = 0
            for x in range(128):
                for y in range(96):
                    rgbValue = imageObject.getpixel((x,y))
                    if rgbValue[0] > 30:
                        hits += 1
                    print(rgbValue)
            hitPercent = hits/12288
            self.match_degree = hitPercent
            #self.weight = self.match_degree * self.priority
            self.halt_request = True

            #Lag en motor-recommendation

        elif self.behavior_number == 2:
            self.match_degree = 1
            self.motor_recommendations = [[-0.1, -0.1, 1], [0.1, -0.1, 1]]

        elif self.behavior_number == 3:
            self.match_degree = (5 - self.sensobs[0].getValue())/5
            self.motor_recommendations = [[-0.1, -0.1, 1], [0.1, -0.1, 1]]

        elif self.behavior_number == 4:
            self.match_degree = 1
            self.motor_recommendations = [[0.1, 0.1, 1]]
        print("Prøver å sette vekt")
        print("priority:", self.priority)
        print("match degree:", self.match_degree)
        self.weight = self.priority * self.match_degree
        print("Har satt weight:", self.weight, "for behavior nummer:", self.behavior_number)



class Arbitrator:

    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self): # Skal ta inn alle aktive behavoirs og velge én av de
        cur_val = 0
        intervall = []
        for act_behv in self.bbcon.act_behaviors:
            print(self.bbcon.act_behaviors)
            print(act_behv)
            print(act_behv.weight)
            print("Eier:", act_behv.behavior_number)
            intervall.append([cur_val, cur_val + act_behv.weight])  # Lager intervall med størresle bassert på vekten deres. Dvs. hvis du har to behaviors med vekt 0.8 og 0.5 vil intervallet bli [[0, 0.8],[0.8, 1.3]]
            cur_val = cur_val + act_behv.weight
        win_weight = random.uniform(0, intervall[-1][-1]) # Velger tilfeldig ut en verdi innenfor intervallet. Større intervall vil da ha større sanns. for å vinne
        for i in range(len(intervall)):
            if win_weight >= intervall[i][0]:
                if win_weight <= intervall[i][1]: # Sjekker hvilket intervall tallet havnet innenfor og returnerer indexen
                    win_behv = self.bbcon.act_behaviors[i]
                    break
        print("Winner:", win_behv.behavior_number)
        return win_behv.motor_recommendations, win_behv.halt_request


def main():
    irSens = Sensob(IRProximitySensor())
    ultraSens = Sensob(Ultrasonic())
    refSens = Sensob(ReflectanceSensors())
    camSens = Sensob(Camera())

    print("Sensobs opprettet")

    sensList = [irSens, ultraSens, refSens, camSens]

    motor1 = Motors()
    motor1.set_value([0, 0, 1])
    motob1 = Motob([motor1], None)
    motobList = [motob1]

    print("Motorer opprettet")

    bbcon = BBCON(None, sensList, motobList, None)

    print("BBCON opprettet")

    detectEdgeBehavior = Behavior(bbcon,[refSens], None, False, False, 10, None, None,2)
    redBehavior = Behavior(bbcon, [camSens, ultraSens], None, False, False, 0.9, None, None, 1)
    dodgeBehavior = Behavior(bbcon, [ultraSens], None, False, False, 0.8, None, None, 3)
    driveBehavior = Behavior(bbcon, [], None, True, False, 0.1, None, None, 4)

    print("Behaviors opprettet")

    bbcon.add_behavior(detectEdgeBehavior)
    bbcon.add_behavior(redBehavior)
    bbcon.add_behavior(dodgeBehavior)
    bbcon.add_behavior(driveBehavior)

    print("Behaviors lagt til. \n Forsøker å starte roboten.")

    runProg = False
    zumoButton = ZumoButton()
    zumoButton.wait_for_press()
    while not runProg:
        runProg = bbcon.run_one_timestep()
    motor1.set_value([0, 0, 1])

main()




