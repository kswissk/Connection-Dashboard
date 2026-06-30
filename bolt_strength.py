from bolt_properties import BoltDatabase


class BoltStrength:

    def __init__(self, diameter, bolt_grade="A325", threads_included=True, shear_planes=1):
        self.diameter = diameter
        self.threads_included = threads_included
        self.shear_planes = shear_planes

        db = BoltDatabase()
        props = db.get_properties(diameter)

        self.Ab = props["Ab"]

        self.phi = 0.75

        if bolt_grade == "A325":
            self.Fnt = 90
            self.Fnv = 54 if threads_included else 68
        else:
            raise ValueError("Only A325 supported")

    def shear_capacity(self):
        return self.phi * self.Fnv * self.Ab * self.shear_planes

    def modified_tensile_stress(self, shear):
        frv = shear / self.Ab
        Fnt_prime = 1.3 * self.Fnt - (self.Fnt / (self.phi * self.Fnv)) * frv
        return min(Fnt_prime, self.Fnt)

    def tension_capacity_with_shear(self, shear):
        Fnt_prime = self.modified_tensile_stress(shear)
        if Fnt_prime < 0:
            return 0
        return self.phi * Fnt_prime * self.Ab

    def check_combined_shear_tension(self, shear, tension):

        shear_cap = self.shear_capacity()
        tension_cap = self.tension_capacity_with_shear(shear)

        shear_ratio = shear / shear_cap
        tension_ratio = tension / tension_cap if tension_cap > 0 else 999

        status = "OK" if shear_ratio <= 1.0 and tension_ratio <= 1.0 else "NG"

        return {
            "shear_per_bolt": shear,
            "tension_per_bolt": tension,
            "shear_capacity": shear_cap,
            "tension_capacity_reduced": tension_cap,
            "shear_ratio": shear_ratio,
            "tension_ratio": tension_ratio,
            "status": status
        }
