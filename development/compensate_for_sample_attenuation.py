def run(source_origin_pixel_angle_list_deg, pixel_value, source, sample_normal):

    import calc_angle_between_vectors
    import numpy as np

    # This function will correct the intensity of each pixel, since the x-rays are attenuated by travelling through the
    # diffracting sample. This means that there will be an angular dependence on the correction to each pixel.

    print "Compensating for sample attenuation..."

    new_pixel_value = []
    correction_factor_list = []

    source_normal_angle = calc_angle_between_vectors.run(
        source, sample_normal
    )

    source_origin_incident_angle = 90.0 - source_normal_angle

    for i in range(len(source_origin_pixel_angle_list_deg)):

        current_pixel_value = pixel_value[i]

        current_source_origin_pixel_angle = source_origin_pixel_angle_list_deg[i]

        sample_pixel_diffraction_angle_deg = 180.0 - current_source_origin_pixel_angle - source_origin_incident_angle

        sample_pixel_diffraction_angle_rad = np.deg2rad(sample_pixel_diffraction_angle_deg)

        source_origin_incident_angle_rad = np.deg2rad(source_origin_incident_angle)

        # The following are used to calculate the correction factor due to sample absorption.

        diffraction_angle_term = (1/np.sin(sample_pixel_diffraction_angle_rad))

        incident_angle_term = (1/np.sin(source_origin_incident_angle_rad))

        complete_angle_term = diffraction_angle_term + incident_angle_term

        # The following term is the factor which, when multiplied by the source intensity, will give us the intensity
        # at the point of detection.

        sample_absorption_term = 1.0 / complete_angle_term

        # Since we are trying to correct for attenuation, we multiply the pixel intensity by the
        # inverse of the absorption term so as to simulate the intensity as if the sample were not
        # attenuating the diffraction signal.

        current_correction_factor = 1.0 / sample_absorption_term

        current_pixel_value = current_pixel_value * current_correction_factor

        new_pixel_value.append(current_pixel_value)

        correction_factor_list.append(current_correction_factor)

    return new_pixel_value, correction_factor_list
