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
        bbcon = bbcon                                           # BBCON objektet som denne behavioren hører til
        sensobs = sensobs                                       # Liste over de sensob-objektene som behavior-objektet bruker
        motor_recommendations = motor_recommendations           # Liste over recommendations en per motob, sendes til arbitratoren
        active_flag = active_flag                               # Boolean som forteller om denne behavioren er aktiv eller ikke
        halt_request = halt_request                             # UVISST?? Se dokumentasjonen på behavior i oppgaven
        priority = priority                                     # Statisk, forteller viktigheten til denne behavioren
        match_degree = match_degree                             # Reelttall, mellom 0 og 1, sier noe om hvor naturlig det er å gjøre denne handlingen
        weight = weight                                         # Produktet av priority og match_degree, brukes for av arbitrator for å bestemme hvilken behavior som skal utføres.
        behavior_number = behavior_number                       # For å vite hvilken behavior de ulike er.


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
