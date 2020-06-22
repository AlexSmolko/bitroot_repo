import random


def weather():
    temperature = 0
    day = 0
    type_of_sky = ["clear", "intermediate", "overcast", "uniform"]
    precipitation = ["without_precipitation", "snow", "rain", "fog", "hail", "flood"]
    strengness_of_the_wind = ["light", "moderate", "intense", "tempest"]
    type_of_area_of_atm_pressure = ("Anticyclone", "Cyclone")
    changing_of_the_type_of_sky = random.choice(type_of_sky)
    type_of_the_sky_cyclone = random.choices(type_of_sky[2:4])
    type_of_the_sky_anticyclone = random.choices(type_of_sky[0:2])
    changing_of_the_type_of_precipitation = random.choices(precipitation[2:6])
    changing_of_the_type_of_the_wind = random.choice(strengness_of_the_wind)
    temperature = random.uniform(-90, 80)
    # changing_of_the_type_of_atm_pressure = random.choice(type_of_area_of_atm_pressure)

    while day < 1:
        if (changing_of_the_type_of_sky == "overcast" or changing_of_the_type_of_sky == "uniform") \
                and (40 > temperature > 0):
            print(
                f"{type_of_the_sky_cyclone} sky, {type_of_area_of_atm_pressure[1]}, {changing_of_the_type_of_precipitation}, "
                f"{changing_of_the_type_of_the_wind} wind")
            if changing_of_the_type_of_precipitation == "rain":
                print("Don't forget about umbrella")
            elif changing_of_the_type_of_precipitation == "fog":
                print("Do not accidentally find yourself in the arms of the Silent Hill creatures. Accidentally...")
            elif changing_of_the_type_of_precipitation == "hail":
                print("Poor plants. Hell hail!")
            elif changing_of_the_type_of_precipitation == "flood":
                print("Sometimes it's nice to feel like a gondolier, bit Only sometimes")
        elif -40 < temperature < 0 and (changing_of_the_type_of_sky == "overcast" or
                                      changing_of_the_type_of_sky == "uniform"):
            print(
                    f"{type_of_the_sky_cyclone} sky, {type_of_area_of_atm_pressure[1]}, snow"
                    f"{changing_of_the_type_of_the_wind} wind", )
        elif changing_of_the_type_of_sky == "clear" or changing_of_the_type_of_sky == "intermediate" \
                and (temperature < 40 or temperature > -40):
            print((f" {type_of_the_sky_anticyclone} sky ,{type_of_area_of_atm_pressure[0]}, {precipitation[0]}, "
                   f"{changing_of_the_type_of_the_wind} wind"))
        elif temperature > 40 or temperature < -40 and ((changing_of_the_type_of_sky == "clear" or
                                                         changing_of_the_type_of_sky == "intermediate") and
                                                        type_of_area_of_atm_pressure[0]):
            print(f"{type_of_the_sky_anticyclone} sky, {type_of_area_of_atm_pressure[0]}, {precipitation[0]}")

        day += 1

    if temperature > 40:
        print(f"+{round(temperature)} Extremly hot!!! Don't take a risk, don't go out from home!")
    elif 27.5 < temperature < 40:
        print(f"+{round(temperature)} Hooot!")
    elif 15 < temperature < 27.5:
        print(f"+{round(temperature)} It's warmly. Just take a pleasure.")
    elif 0 < temperature < 15:
        print(f"+{round(temperature)} It's not such warm day.")
    elif 0 > temperature > -15:
        print(f"{round(temperature)} It's coldly. Dress something warm, please.")
    elif -15 > temperature > -40:
        print(f"{round(temperature)} It's very coldly. Don't forget about scarf and gloves.")
    elif temperature < -40:
        print(f"{round(temperature)} Extreme cold. Take care yourself")


weather()
