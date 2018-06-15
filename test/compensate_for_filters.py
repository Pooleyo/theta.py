def run(filter_angles_list_deg, pixel_value, filter_attenuation_length_at_90_deg, filter_thickness):

    import numpy as np
    import math

    print "Compensating for filters..."
    attenuation_factor_list = []
    for i in range(len(filter_attenuation_length_at_90_deg)):
        current_attenuation_factor_list = []

        number_of_attenuation_lengths = filter_thickness[i]/filter_attenuation_length_at_90_deg[i]
        attenuation_factor_at_90_deg =  number_of_attenuation_lengths * (1 - 1/math.e) # This number represents the fraction of intensity absorbed by the filter at this angle.
         
        
        for j in range(len(pixel_value)):            
            effective_attenuation_factor = attenuation_factor_at_90_deg / np.cos(np.deg2rad(filter_angles_list_deg[j])) # This corrects for the angle of incidence of the scattered x-rays upon the filter, by looking at the effective thickness of the filter at the present angle.

            pixel_value[j] = pixel_value[j] * (1.0/(1.0 - effective_attenuation_factor))
            
            current_attenuation_factor_list.append(effective_attenuation_factor)
            
        attenuation_factor_list.append(current_attenuation_factor_list)

    return pixel_value, attenuation_factor_list
