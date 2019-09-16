def run(gsqr_phi_bins, gsqr_phi_bin_pixel_counter, minimum_pixels_column):

    import numpy as np

    print "Integrating intensity across phi..."

    height, width = np.shape(gsqr_phi_bins)

    intensity_summed_across_phi = np.zeros((1, width))

    number_pixels_in_each_col = np.zeros((1, width))

    intensity_integrated_across_phi = np.zeros((1, width))

    for col in range(width):

        for row in range(height):

            intensity_summed_across_phi[0, col] += gsqr_phi_bins[row, col]

            number_pixels_in_each_col[0, col] += gsqr_phi_bin_pixel_counter[row, col]

    for col in range(width):

        # The below function returns a tuple containing a numpy array. The numpy array contains the indices of all the
        # non-zero entries to the current column.

        coords = np.nonzero(gsqr_phi_bin_pixel_counter[:, col])

        num_occupied_bins = len(coords[0])

        if number_pixels_in_each_col[0, col] <= minimum_pixels_column:

            intensity_integrated_across_phi[0, col] = 0.0

        else:

            intensity_integrated_across_phi[0, col] = intensity_summed_across_phi[0, col] / num_occupied_bins

    return intensity_integrated_across_phi, intensity_summed_across_phi
