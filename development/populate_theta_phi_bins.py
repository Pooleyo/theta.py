def run(working_width, working_height, gsqr, phi, gsqr_bins, phi_bins, gsqr_phi_bins, gsqr_phi_bin_pixel_counter, working_pixel_value, subpixel_value, gsqr_limit, phi_limit):

    import numpy as np   

    print "Populating G^2 and phi bins..."

    dumped_pixel_counter = 0

    for pixel_row in range(working_height):

        for pixel_col in range(working_width):

            # This first statement checks if the pixel value is 0. We don't want this to be counted, since it will
            # decrease the integrated intensity without actually being a contributing pixel.
            if subpixel_value[pixel_row][pixel_col] == 0.0:

                dumped_pixel_counter += 1

                pass

            # This statement checks that the gsqr value of the pixel is within the user-set limits.
            elif not gsqr_limit[0] < gsqr[pixel_row, pixel_col] < gsqr_limit[1]:

                dumped_pixel_counter =+ 1

                pass

            # This statement checks that the phi value of the pixel is within the user-set limits.
            elif not phi_limit[0] < phi[pixel_row, pixel_col] < phi_limit[1]:

                dumped_pixel_counter = + 1

                pass

            else:

                current_gsqr = gsqr[pixel_row, pixel_col]

                gsqr_subtract = abs(gsqr_bins - current_gsqr)

                bin_col = np.argmin(gsqr_subtract)

                current_phi = phi[pixel_row, pixel_col]

                phi_subtract = abs(phi_bins - current_phi)

                bin_row = np.argmin(phi_subtract)

                gsqr_phi_bins[bin_row, bin_col] += working_pixel_value[pixel_row, pixel_col]

                gsqr_phi_bin_pixel_counter[bin_row, bin_col] += 1

    print "Dumped pixels = " + str(dumped_pixel_counter)
    print "Sorted pixels = " + str(np.sum(gsqr_phi_bin_pixel_counter))
    print "Total pixels processed = " + str(dumped_pixel_counter + np.sum(gsqr_phi_bin_pixel_counter))
    print "Total pixels in raw image = " + str(np.size(working_pixel_value))

    return gsqr_phi_bins, gsqr_phi_bin_pixel_counter, dumped_pixel_counter
