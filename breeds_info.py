import numpy as np
import pandas as pd

class Breed:
    dog={
        'breed':None,
        'url':None,
        'a_adaptability':None,
        'a1_adapts_well_to_apartment_living':None,
        'a2_good_for_novice_owners':None,
        'a3_sensitivity_level':None,
        'a4_tolerates_being_alone':None,
        'a5_tolerates_cold_weather':None,
        'a6_tolerates_hot_weather':None,
        'b_all_around_friendliness':None,
        'b1_affectionate_with_family':None,
        'b2_incredibly_kid_friendly_dogs':None,
        'b3_dog_friendly':None,
        'b4_friendly_toward_strangers':None,
        'c_health_grooming':None,
        'c1_amount_of_shedding':None,
        'c2_drooling_potential':None,
        'c3_easy_to_groom':None,
        'c4_general_health':None,
        'c5_potential_for_weight_gain':None,
        'c6_size':None,
        'd_trainability':None,
        'd1_easy_to_train':None,
        'd2_intelligence':None,
        'd3_potential_for_mouthiness':None,
        'd4_prey_drive':None,
        'd5_tendency_to_bark_or_howl':None,
        'd6_wanderlust_potential':None,
        'e_exercise_needs':None,
        'e1_energy_level':None,
        'e2_intensity':None,
        'e3_exercise_needs':None,
        'e4_potential_for_playfulness':None,
        'breed_group':None,
        'height':None,
        'weight':None,
        'life_span':None
    }

    dog_describe=None

    def __init__(self, series):
        # save the series' info
        for key, value in series.items():
            self.dog[key]=value

