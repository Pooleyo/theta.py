def run(height, width, filter_angles_list_deg, pixel_value, filter_attenuation_length_at_90_deg, filter_thickness,
        attenuation_correction, pixel_value_corrected_for_attenuation):

    import numpy as np

    print "Compensating for filters..."

    for i in range(height):

        for j in range(width):

            effective_path_length = filter_thickness / np.cos(np.deg2rad(filter_angles_list_deg[i][j]))  # By taking the
            # angle of incidence into account we can calculate an effective thickness of the filter at this incidence
            # angle.

            attenuation_factor = np.exp(- effective_path_length / filter_attenuation_length_at_90_deg)  # By
            # following the equation: I = I_0 * e^(- path_length / attenuation_length)

            correction_factor = 1.0 / attenuation_factor
            pixel_value_corrected_for_attenuation[i][j] = pixel_value[i][j] * correction_factor  # We multiply by the reciprocal of the
            #  attenuation to revert to the original intensity.

            attenuation_correction[i][j] = correction_factor

            if correction_factor < 0.0:
                print "#### WARNING: NEGATIVE CORRECTION FACTOR ####"

    return pixel_value_corrected_for_attenuation, attenuation_correction
