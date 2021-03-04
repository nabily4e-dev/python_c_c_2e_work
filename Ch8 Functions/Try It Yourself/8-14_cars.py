
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




def car_info_builder(manufacturer, model, **car_info):
    """Making car information"""

    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model

    return car_info


car_info = car_info_builder('subaru', 'outback', color='blue', tow_package=True)

print(car_info)



############################################
print('\n')  # Spaces for convention only!
############################################
