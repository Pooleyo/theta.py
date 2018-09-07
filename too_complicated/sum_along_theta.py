def run(image_bin_list, gsqr_bin_list, phi_bin_list, debug):
    
    print "Integrating intensity across phi..."
    
    gsqr_integrated_intensity = [0] * len(gsqr_bin_list)

    for i in range(len(gsqr_bin_list)):

        for j in range(len(phi_bin_list)):

            current_index = i * len(phi_bin_list) + j

            gsqr_integrated_intensity[i] += image_bin_list[current_index][3]

    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nimage_bin_list = " + str(image_bin_list)
    + "\ngsqr_bin_list = " + str(gsqr_bin_list)
    + "\nphi_bin_list = " + str(phi_bin_list) 
    + "\ndebug = " + str(debug)
  
    + "\n\nOUTPUTS:"
    + "\ngsqr_integrated_intensity = " + str(gsqr_integrated_intensity)
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return gsqr_integrated_intensity
