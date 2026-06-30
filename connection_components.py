from bolt_strength import BoltStrength


# ----------------------------
# COLUMN FLANGE BOLTS (DOUBLE ANGLE)
# ----------------------------
def design_column_flange_bolts(Vu, Tu, diameter, threads_included):
    """
    Method 2 (correct behavior):
    - Load splits between two angles
    - Each angle carries Vu/2 and Tu/2
    - Single shear per bolt
    """

    # ✅ FIX: use keyword arguments (THIS WAS YOUR ERROR)
    bolt = BoltStrength(
        diameter=diameter,
        threads_included=threads_included,
        shear_planes=1
    )

    # Load split between angles
    Vu_side = Vu / 2
    Tu_side = Tu / 2

    for n in range(2, 13):
        shear = Vu_side / n
        tension = Tu_side / n

        check = bolt.check_combined_shear_tension(shear, tension)

        if check["status"] == "OK":
            return {
                "bolts_per_angle": n,
                "total_bolts": 2 * n,
                "check": check
            }

    return {"status": "NG"}


# ----------------------------
# BEAM WEB WELD (DOUBLE ANGLE)
# ----------------------------
def design_beam_web_weld(Vu, Tu, weld_size, Lv, Lh, gap=0.5):
    """
    Weld logic from your Excel:

    L_total = 2 × [Lv + 2*(Lh - gap)]
    """

    phi = 0.75
    Fexx = 70  # ksi

    # Effective horizontal length
    Lh_eff = Lh - gap

    # Total weld length (two angles)
    total_length = 2 * (Lv + 2 * Lh_eff)

    # Weld throat area
    Aw = 0.707 * weld_size * total_length

    # Strength
    capacity = phi * 0.6 * Fexx * Aw

    # Resultant demand
    demand = (Vu**2 + Tu**2) ** 0.5

    # Ratio
    ratio = demand / capacity

    status = "OK" if ratio <= 1.0 else "NG"

    return {
        "total_length": total_length,
        "capacity": capacity,
        "demand": demand,
        "ratio": ratio,
        "status": status
    }
