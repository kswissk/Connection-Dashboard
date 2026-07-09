import pandas as pd


class Angle:
    def __init__(self, name, leg1, leg2, thickness, area, Ix, Iy, weight):
        self.name = name
        self.leg1 = leg1
        self.leg2 = leg2
        self.t = thickness
        self.area = area
        self.Ix = Ix
        self.Iy = Iy
        self.weight = weight


class AngleDatabase:
    def __init__(self, excel_path="aisc-shapes-database-v150.xlsx"):
        self.angles = []
        self.load_angles(excel_path)

    def load_angles(self, path):
        df = pd.read_excel(path, sheet_name="Database v15.0")

        # Filter ANGLES ONLY
        df = df[df["Type"] == "L"]

        for _, row in df.iterrows():
            try:
                self.angles.append(
                    Angle(
                        name=row["AISC_Manual_Label"],
                        leg1=float(row["b"]),
                        leg2=float(row["d"]),
                        thickness=float(row["t"]),
                        area=float(row["A"]),
                        Ix=float(row["Ix"]),
                        Iy=float(row["Iy"]),
                        weight=float(row["W"])
                    )
                )
            except:
                continue

    def get_all_angles(self):
        return self.angles


class AngleSelector:
    def __init__(self, db):
        self.db = db

    def select_angle(self, Vu, Fy=50, phi=0.9):
        """
        Returns lightest angle that satisfies shear demand
        """

        candidates = []

        for angle in self.db.get_all_angles():

            # Nominal shear capacity (AISC approx)
            Vn = 0.6 * Fy * angle.area
            phiVn = phi * Vn

            # Skip very thin angles (practical filter)
            if angle.t < 0.25:
                continue

            if phiVn >= Vu:
                candidates.append((angle, phiVn))

        if not candidates:
            return None, None

        # Select lightest
        best = sorted(candidates, key=lambda x: x[0].weight)[0]

        return best
