class BoltDatabase:
    def __init__(self):
        self.database = {
            0.75: {"Ab": 0.442, "At": 0.334},
            0.875: {"Ab": 0.601, "At": 0.462},
            1.0: {"Ab": 0.785, "At": 0.606},
            1.125: {"Ab": 0.994, "At": 0.763},
            1.25: {"Ab": 1.227, "At": 0.969},
            1.375: {"Ab": 1.485, "At": 1.155},
            1.5: {"Ab": 1.767, "At": 1.405},
            1.75: {"Ab": 2.405, "At": 1.900},
            2.0: {"Ab": 3.142, "At": 2.500}
        }

    def get_properties(self, diameter):
        if diameter not in self.database:
            raise ValueError(f"Bolt size {diameter} not found.")
        return self.database[diameter]