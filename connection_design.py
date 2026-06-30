from connection_components import (
    design_column_flange_bolts,
    design_beam_web_weld
)

from connection_schedule import (
    generate_table_2,
    print_table_2,
    get_angle_and_weld
)

from connection_table import generate_table_1


# =========================
# USER INPUT
# =========================
Vu = float(input("Factored shear Vu (kips): "))
Tu = float(input("Factored tension Tu (kips): "))
d = float(input("Bolt diameter (in): "))

threads = input("Threads included? (Y/N): ").upper() == "Y"


# =========================
# TABLE 1 (FIRST)
# =========================
print("\n" + "="*60)
print("            TABLE 1: LOAD vs BOLT COUNT")
print("="*60)

generate_table_1(d, threads)


# =========================
# BOLT DESIGN
# =========================
bolt_res = design_column_flange_bolts(Vu, Tu, d, threads)

# Auto-select angle + weld
angle_data = get_angle_and_weld(bolt_res["bolts_per_angle"])

angle = angle_data["angle"]
weld_size = angle_data["weld"]

Lv = float(angle.split('x')[0][1:])
Lh = Lv


# =========================
# WELD DESIGN
# =========================
weld_res = design_beam_web_weld(Vu, Tu, weld_size, Lv, Lh)


# =========================
# TABLE 2 (SECOND)
# =========================
table2 = generate_table_2(bolt_res)

print("\n" + "="*60)
print("          TABLE 2: CONNECTION SCHEDULE")
print("="*60)

print_table_2(table2)


# =========================
# FINAL CONNECTION OUTPUT (LAST)
# =========================
print("\n" + "="*60)
print("              CONNECTION DESIGN SUMMARY")
print("="*60)

print("\nINPUT SUMMARY")
print("-"*60)
print(f"{'Factored Shear (Vu)':<30}: {Vu:.2f} kips")
print(f"{'Factored Tension (Tu)':<30}: {Tu:.2f} kips")
print(f"{'Bolt Diameter':<30}: {d:.2f} in")
print(f"{'Threads Included':<30}: {'Yes' if threads else 'No'}")
print(f"{'Angle Selected':<30}: {angle}")
print(f"{'Weld Size':<30}: {weld_size} in")

print("\nCOLUMN FLANGE BOLT DESIGN")
print("-"*60)

if bolt_res.get("status") != "NG":
    c = bolt_res["check"]

    print(f"{'Bolts per Angle':<30}: {bolt_res['bolts_per_angle']}")
    print(f"{'Total Bolts':<30}: {bolt_res['total_bolts']}")
    print(f"{'Shear per Bolt':<30}: {c['shear_per_bolt']:.2f} kips")
    print(f"{'Tension per Bolt':<30}: {c['tension_per_bolt']:.2f} kips")
    print(f"{'Shear Capacity':<30}: {c['shear_capacity']:.2f} kips")
    print(f"{'Tension Capacity':<30}: {c['tension_capacity_reduced']:.2f} kips")
    print(f"{'Shear Ratio':<30}: {c['shear_ratio']:.3f}")
    print(f"{'Tension Ratio':<30}: {c['tension_ratio']:.3f}")
    print(f"{'Status':<30}: {c['status']}")
else:
    print("Bolt design FAILED")

print("\nBEAM WEB WELD DESIGN")
print("-"*60)

print(f"{'Total Weld Length':<30}: {weld_res['total_length']:.2f} in")
print(f"{'Weld Capacity':<30}: {weld_res['capacity']:.2f} kips")
print(f"{'Demand (Resultant)':<30}: {weld_res['demand']:.2f} kips")
print(f"{'Utilization Ratio':<30}: {weld_res['ratio']:.3f}")
print(f"{'Status':<30}: {weld_res['status']}")