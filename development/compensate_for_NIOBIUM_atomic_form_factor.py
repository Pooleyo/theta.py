def run(working_pixel_value, working_height, working_width, bragg_angle, output_folder, wavelength):

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.interpolate import interp1d

    # This first section sets up the interpolated function from atomic form factor data. This data is taken from
    # "X-ray Diffraction" by Warren, pg 372.

    sin_theta_over_lambda = np.linspace(0.0, 1.5, num=16, endpoint=True)
    niobium_atomic_form_factor_table_data = np.array([41.0, 37.91, 32.40, 27.81, 24.01, 20.98, 18.49, 16.45, 14.74,
                                                      13.31, 12.08, 11.04, 10.13, 9.33, 8.64, 8.02])

    interpolated_form_factor = interp1d(sin_theta_over_lambda, niobium_atomic_form_factor_table_data, kind='cubic')

    plt.plot(interpolated_form_factor(sin_theta_over_lambda))
    plt.title('Atomic form factor for niobium')
    plt.ylabel('Atomic Form Factor')
    plt.xlabel('sin$\Theta$/$\lambda$ (A$^{-1}$)')
    plt.savefig(output_folder + '/atomic_form_factor_plot.png')
    plt.close()

    # Now that the interpolated function has been created, we loop over the pixels so as to calculate the correction
    # that is to be applied.

    atomic_form_factor_correction = np.zeros((working_height, working_width))
    new_pixel_value = np.zeros((working_height, working_width))

    normalising_factor = interpolated_form_factor(0.0)

    for i in range(working_height):

        for j in range(working_width):

            # The correction factor below is inverted since we want to get the intensity as if this effect never
            # occurred.

            current_sin_theta_over_lambda = np.sin(np.deg2rad(bragg_angle[i][j])) / wavelength

            current_atomic_form_factor = interpolated_form_factor(current_sin_theta_over_lambda)

            normalised_atomic_form_factor = current_atomic_form_factor / normalising_factor

            correction_factor = 1.0 / normalised_atomic_form_factor

            new_pixel_value[i][j] = correction_factor * working_pixel_value[i][j]

            atomic_form_factor_correction[i][j] = correction_factor

            if correction_factor < 0.0:

                print "#### WARNING: NEGATIVE CORRECTION FACTOR ####"

    return new_pixel_value, atomic_form_factor_correction
