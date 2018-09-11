def run(theta_phi_n_pixels_width, theta_phi_n_pixels_height, gsqr_limit, phi_limit):

    import numpy as np

    print "Making bins for theta-phi sorting..."

    gsqr_phi_bins = np.zeros((theta_phi_n_pixels_width, theta_phi_n_pixels_height))

    gsqr_phi_bin_pixel_counter = np.copy(gsqr_phi_bins)

    gsqr_bins = np.linspace(gsqr_limit[0], gsqr_limit[1], theta_phi_n_pixels_width)

    phi_bins = np.linspace(phi_limit[0], phi_limit[1], theta_phi_n_pixels_height)


    """
    new_image_bins = []  # This list will contain the theta_phi images' gsqr value at [0], phi value at [1], a list of
    #  pixel indices falling into this bin at [2], and the sum of the pixel values currently in this bin at [3].
    
    gsqr_range = np.linspace(gsqr_limit[0], gsqr_limit[1], num_gsqr_bins)
    
    phi_range = np.linspace(phi_limit[0], phi_limit[1], num_phi_bins)

    for i in gsqr_range:
    
        for j in phi_range:

            current_list_value = [i, j, [], 0.0]

            new_image_bins.append(current_list_value)
    """
    print gsqr_phi_bins.shape
    print gsqr_phi_bins
    print gsqr_phi_bin_pixel_counter
    print gsqr_bins
    print phi_bins

    return gsqr_phi_bins, gsqr_phi_bin_pixel_counter, gsqr_bins, phi_bins
