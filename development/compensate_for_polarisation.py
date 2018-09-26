def run(working_pixel_value, height, width, polarisation_angles):

    import numpy as np

    new_pixel_value = np.zeros((height, width))
    polarisation_correction_factor = np.zeros((height, width))

    for i in range(height):

        for j in range(width):

            # The correction factor below is inverted since we want to get the intensity as if this effect never
            # occurred.
            correction_factor = 2.0 / (1 + np.cos(np.deg2rad(polarisation_angles[i][j])))

            new_pixel_value[i][j] = correction_factor * working_pixel_value[i][j]

            polarisation_correction_factor[i][j] = correction_factor

    return new_pixel_value, polarisation_correction_factor