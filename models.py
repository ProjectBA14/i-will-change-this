class Disease:
    def __init__(
            self,
            name,
            transmission_rate,
            symptoms,
            recovery_rate,
            mortality_rate
    ):
        self.name=name
        self.transmission_rate=transmission_rate
        self.symptoms=symptoms
        self.recovery_rate=recovery_rate
        self.mortality_rate=mortality_rate

class Citizen:
    def __init__(
            self,
            citizen_id
    ):
        self.id=citizen_id
        self.state="healthy"