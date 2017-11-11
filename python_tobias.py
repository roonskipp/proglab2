class BBCON():
    # TODO
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
    # TODO
    pass

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
        self.behavior_number = behavior_number                       # For å vite hvilken behavior de ulike er.


    def consider_activation(self):
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
            # TODO
            pass

    def consider_deavtivation(self):
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
            # TODO
            pass

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
            # TODO
            pass

        pass



class Arbitrator:
    # TODO
    pass
