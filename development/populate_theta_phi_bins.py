def run(working_width, working_height, gsqr, phi, gsqr_bins, phi_bins, gsqr_phi_bins, gsqr_phi_bin_pixel_counter, working_pixel_value):

    import numpy as np   

    print "Populating G^2 and phi bins..."

    for pixel_row in range(working_height):

        for pixel_col in range(working_width):

            current_gsqr = gsqr[pixel_row, pixel_col]

            gsqr_subtract = abs(gsqr_bins - current_gsqr)

            bin_col = np.argmin(gsqr_subtract)

            current_phi = phi[pixel_row, pixel_col]

            phi_subtract = abs(phi_bins - current_phi)

            bin_row = np.argmin(phi_subtract)

            gsqr_phi_bins[bin_row, bin_col] += working_pixel_value[pixel_row, pixel_col]

            gsqr_phi_bin_pixel_counter[bin_row, bin_col] += 1

    return gsqr_phi_bins, gsqr_phi_bin_pixel_counter
