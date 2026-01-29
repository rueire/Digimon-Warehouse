from digimon_list import get_digimons
from digimon_levels import get_digimon_levels
from digimon_attributes import get_attribute_list
from digimon_details import get_digimons_details


def use_apis():
    get_digimons()
    # print('digimon list fetched')

    get_digimon_levels()
    print('digimon levels fetched')

    get_attribute_list()
    print('digimon attributes fetched')

    # get_digimons_details()
    print('digimon details fetched')


use_apis()