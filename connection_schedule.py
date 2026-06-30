def get_angle_and_weld(bolts_per_angle):

    if bolts_per_angle <= 2:
        return {"angle": "L4x4x3/8", "weld": 0.25}
    elif bolts_per_angle == 3:
        return {"angle": "L6x6x3/8", "weld": 0.25}
    elif bolts_per_angle == 4:
        return {"angle": "L6x6x1/2", "weld": 0.3125}
    elif bolts_per_angle == 5:
        return {"angle": "L8x8x1/2", "weld": 0.3125}
    else:
        return {"angle": "L8x8x1", "weld": 0.375}


def generate_table_2(result):

    if result.get("status") == "NG":
        return None

    n = result["bolts_per_angle"]

    props = get_angle_and_weld(n)

    return {
        "Connection": f"BC-{n}",
        "Bolts per angle": n,
        "Total bolts": result["total_bolts"],
        "Angle": props["angle"],
        "Weld": props["weld"]
    }


def print_table_2(t):

    print("\n===== TABLE 2 =====\n")

    print(f"{'Conn':<8} | {'Bolts/Ang':<10} | {'Total':<8} | {'Angle':<12} | Weld")
    print("-" * 60)

    if t:
        print(f"{t['Connection']:<8} | {t['Bolts per angle']:<10} | {t['Total bolts']:<8} | {t['Angle']:<12} | {t['Weld']}")
    else:
        print("No valid connection")