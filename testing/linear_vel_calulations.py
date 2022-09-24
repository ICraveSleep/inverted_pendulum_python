def linear_vel_from_rpm(rpm: float, pitch: float, gear_ratio: float = 1.0):
    """
    :param rpm: angular velocity [rev/min]
    :param pitch: Screw pitch [mm/rev]
    :param gear_ratio: The gearing ratio from the motor to the lead screw [-]
    :return: linear velocity [mm/s]
    """

    linear_velocity = rpm*pitch/60
    return round(linear_velocity, 2)


def kv_to_rpm(kv: float, voltage: float):
    return round(kv*voltage, 2)


def main():
    screw_pitch_list = [4, 5, 10]
    rpm_list = [100, 250, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 10000]

    for pitch in screw_pitch_list:
        print(f"Calculating linear velocity at RPMs for {pitch}mm pitch")
        for rpm in rpm_list:
            print(f"{linear_vel_from_rpm(rpm, pitch)}[mm/s] at {rpm}[rpm]")
        print("-"*40)

    voltage_list = [1, 2, 5, 10, 12, 15, 20, 24]
    kv_list = [520, 720, 880]

    for kv in kv_list:
        print(f"Calculating rpm for {kv}Kv")
        for voltage in voltage_list:
            print(f"{kv_to_rpm(kv, voltage)}[rpm] at {voltage}[V]")
        print("-" * 40)


if __name__ == '__main__':
    main()