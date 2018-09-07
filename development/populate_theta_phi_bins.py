def run(gsqr, phi, pixel_value, gsqr_bins, phi_bins, image_bins, gsqr_bin_width, phi_bin_height):

    import numpy as np   

    print "Populating theta and phi bins..."

    for i in range(len(pixel_value)):
        gsqr_diff = []    
        for j in gsqr_bins:
            gsqr_diff.append(abs(gsqr[i] - j))
        gsqr_bin_index = np.argmin(gsqr_diff)    
        
        phi_diff = []
        for j in phi_bins:
            phi_diff.append(abs(phi[i] - j))
        phi_bin_index = np.argmin(phi_diff)      

        bin_index = (gsqr_bin_index * len(phi_bins)) + phi_bin_index
        
        image_bins[bin_index][2].append(i)

                
    return image_bins
