from connection_components import design_column_flange_bolts


def generate_table_1(diameter, threads):

    shear_vals = [20, 40, 60, 80]
    tension_vals = [0, 10, 20, 30]

    print("\n===== TABLE 1 =====\n")

    header = "Tu\\Vu |"
    for v in shear_vals:
        header += f"{v:>6}"
    print(header)

    print("-" * len(header))

    for t in tension_vals:
        row = f"{t:>5} |"

        for v in shear_vals:
            res = design_column_flange_bolts(v, t, diameter, threads)

            if res.get("status") == "NG":
                val = "NG"
            else:
                val = res["bolts_per_angle"]

            row += f"{str(val):>6}"

        print(row)
