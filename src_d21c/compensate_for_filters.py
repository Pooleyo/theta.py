def run(filter_angles_list_deg, pixel_value, filter_attenuation_length_at_90_deg, filter_thickness, debug):

    import numpy as np

    print "Compensating for filters..."
    
    attenuation_correction_list = [] # This list will contain multiple sub-lists; each sublist represents the attenuation
    # factors for each filter.

    for i in range(len(filter_attenuation_length_at_90_deg)):
    
        current_attenuation_correction_list = []

        for j in range(len(pixel_value)):

            effective_path_length = filter_thickness[i] / np.cos(np.deg2rad(filter_angles_list_deg[j])) # By taking the
            # angle of incidence into account we can calculate an effective thickness of the filter at this incidence
            # angle.
            
            attenuation_factor = np.exp( - effective_path_length / filter_attenuation_length_at_90_deg[i]) # By
            # following the equation: I = I_0 * e^(- path_length / attenuation_length)

            correction_factor = 1.0 / attenuation_factor

            pixel_value[j] = pixel_value[j] * correction_factor  # We multiply by the reciprocal of the
            #  attenuation to revert to the original intensity.
            
            current_attenuation_correction_list.append(correction_factor)

        attenuation_correction_list.append(current_attenuation_correction_list)

    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nfilter_angles_deg = " + str(filter_angles_list_deg)
    + "\nraw_pixel_value = " + str(pixel_value)
    + "\nfilter_attenuation_length_at_90_deg = " + str(filter_attenuation_length_at_90_deg)
    + "\nfilter_thickness = " + str(filter_thickness)
    + "\ndebug = " + str(debug)
  
    + "\n\nOUTPUTS:"
    + "\nraw_pixel_value = " + str(pixel_value)
    + "\nattenuation_correction_list = " + str(attenuation_correction_list)
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return pixel_value, attenuation_correction_list
