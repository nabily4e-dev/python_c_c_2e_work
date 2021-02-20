
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




def car_info_builder(manufacturer, model, **car_info):
    """Making car information"""

    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model

    return car_info


def make_sandwitch(*sandwitches):

    if sandwitches:
        for sandwitch in sandwitches:
            print(f"The {sandwitch} sandwitch has been ordered!")





############################################
print('\n')  # Spaces for convention only!
############################################
