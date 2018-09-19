def run(num_gsqr_bins, num_phi_bins, gsqr_limit, phi_limit):

    import numpy as np

    print "Making bins for theta-phi sorting..."

    gsqr_phi_bins = np.zeros((num_phi_bins, num_gsqr_bins))

    gsqr_phi_bin_pixel_counter = np.copy(gsqr_phi_bins)

    gsqr_bins = np.linspace(gsqr_limit[0], gsqr_limit[1], num_gsqr_bins)

    phi_bins = np.linspace(phi_limit[0], phi_limit[1], num_phi_bins)

    return gsqr_phi_bins, gsqr_phi_bin_pixel_counter, gsqr_bins, phi_bins
