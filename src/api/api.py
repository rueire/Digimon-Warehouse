from digimon_list import get_digimons
from digimon_levels import get_digimon_levels, level_info
from digimon_attributes import attribute_info, get_attribute_list
from digimon_details import get_digimons_details
from digimon_fields import get_digimon_fields, field_info


def use_apis():
    get_digimons()

    get_digimon_levels()

    get_attribute_list()

    get_digimons_details()

    get_digimon_fields()


    field_info()
    attribute_info()
    level_info()


use_apis()