
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


import printing_functions
import printing_functions as pf
from printing_functions import *
from printing_functions import car_info_builder
from printing_functions import car_info_builder as cib



car_info = printing_functions.car_info_builder('subaru', 'outback', color='blue', tow_package=True)
car_info = pf.car_info_builder('subaru', 'outback', color='blue', tow_package=True)
car_info = car_info_builder('subaru', 'outback', color='blue', tow_package=True)
car_info = cib('subaru', 'outback', color='blue', tow_package=True)
print(car_info)






############################################
print('\n')  # Spaces for convention only!
############################################
