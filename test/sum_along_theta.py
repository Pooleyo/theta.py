def run(image_bin_list, gsqr_bin_list, phi_bin_list):
    
    print "Integrating intensity across phi..."
    
    gsqr_integrated_intensity = [0] * len(gsqr_bin_list)
    for i in range(len(gsqr_bin_list)):
        for j in range(len(phi_bin_list)):
            current_index = i * len(phi_bin_list) + j   
            gsqr_integrated_intensity[i] += image_bin_list[current_index][3]               
    
    return gsqr_integrated_intensity
