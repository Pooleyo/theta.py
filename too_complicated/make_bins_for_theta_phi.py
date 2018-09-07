def run(num_gsqr_bins, num_phi_bins, gsqr_limit, phi_limit, debug):

    import numpy as np   

    print "Making bins for theta-phi sorting..."
    
    new_image_bins = []  # This list will contain the theta_phi images' gsqr value at [0], phi value at [1], a list of
    #  pixel indices falling into this bin at [2], and the sum of the pixel values currently in this bin at [3].
    
    gsqr_range = np.linspace(gsqr_limit[0], gsqr_limit[1], num_gsqr_bins)
    
    phi_range = np.linspace(phi_limit[0], phi_limit[1], num_phi_bins)

    for i in gsqr_range:
    
        for j in phi_range:

            current_list_value = [i, j, [], 0.0]

            new_image_bins.append(current_list_value)

    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nnum_gsqr_bins = " + str(num_gsqr_bins)
    + "\nnum_phi_bins = " + str(num_phi_bins)
    + "\ngsqr_limit = " + str(gsqr_limit)
    + "\nphi_limit = " + str(phi_limit)
    
    + "\n\nOUTPUTS:"
    + "\ngsqr_range = " + str(gsqr_range)
    + "\nphi_range = " + str(phi_range)
    + "\nnew_image_bins = " + str(new_image_bins)
    
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return gsqr_range, phi_range, new_image_bins
