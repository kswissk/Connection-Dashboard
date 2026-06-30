from bolt_properties import BoltDatabase

bolt_db = BoltDatabase()

# Example: 3/4" bolt
diameter = 0.75

At = bolt_db.get_area(diameter, threads_included=True)
Ab = bolt_db.get_area(diameter, threads_included=False)

print("Bolt size =", diameter, "in")
print("Tensile stress area (At) =", At, "in^2")
print("Gross area (Ab) =", Ab, "in^2")