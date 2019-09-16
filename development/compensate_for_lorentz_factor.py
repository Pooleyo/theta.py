def run(working_pixel_value, height, width, bragg_angles_deg):

    import numpy as np

    print "Compensating for polarisation..."

    new_pixel_value = np.zeros((height, width))
    lorentz_correction_factor = np.zeros((height, width))

    for i in range(height):

        for j in range(width):

            # The effect of the lorentz factor is 1/sin(bragg_angle).
            # The correction factor below is inverted since we want to get the intensity as if this effect never
            # occurred.

            correction_factor = (1.0 + (np.cos(np.deg2rad(bragg_angles_deg[i][j]))**2)) / (np.sin(2 * np.deg2rad(bragg_angles_deg[i][j])) * np.sin(np.deg2rad(bragg_angles_deg[i][j])))

            new_pixel_value[i][j] = correction_factor * working_pixel_value[i][j]

            lorentz_correction_factor[i][j] = correction_factor

            if correction_factor < 0.0:

                print "#### WARNING: NEGATIVE CORRECTION FACTOR ####"

    return new_pixel_value, lorentz_correction_factor