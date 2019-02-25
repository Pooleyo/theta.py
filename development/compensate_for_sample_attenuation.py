def run(working_pixel_value, sample_normal, source, vector_origin_to_pixels):

    import calc_angle_between_vectors
    import numpy as np

    print "Compensate for sample attenuation..."

    source_normal_angle = calc_angle_between_vectors.run(
        source, sample_normal)

    source_origin_incident_angle = 90.0 - source_normal_angle

    incident_angle_term = 1/np.sin(np.deg2rad(source_origin_incident_angle))

    working_height, working_width = np.shape(working_pixel_value)

    corrected_pixel_value = np.zeros((working_height, working_width))

    sample_correction_factor = np.zeros((working_height, working_width))
    print "start loop"
    for i in range(working_height):
        print i
        for j in range(working_width):

            current_vector_origin_pixel = vector_origin_to_pixels[(i * working_width) + j]

            if current_vector_origin_pixel is int(0):

                correction_factor = 0

                sample_correction_factor[i][j] = correction_factor

                corrected_pixel_value[i][j] = working_pixel_value[i][j] * correction_factor

            else:

                angle_normal_origin_pixel_deg = calc_angle_between_vectors.run(current_vector_origin_pixel, sample_normal)

                diffraction_angle = 90.0 - angle_normal_origin_pixel_deg

                diffraction_angle_term = 1/np.sin(np.deg2rad(diffraction_angle))

                correction_factor = diffraction_angle_term + incident_angle_term

                sample_correction_factor[i][j] = correction_factor

                corrected_pixel_value[i][j] = working_pixel_value[i][j] * correction_factor
    exit()

    return corrected_pixel_value, sample_correction_factor