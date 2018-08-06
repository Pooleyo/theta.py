def run(gsqr, phi, pixel_value, gsqr_bin_size, phi_bin_size):
        
    import math
    import numpy as np
    from PIL import Image 
   
    gsqr_res = int( math.ceil( (max(gsqr)- min(gsqr)) / gsqr_bin_size ) )
    phi_res = int( math.ceil( 2 * max(phi) / phi_bin_size ) )
    
    print max(phi)
    print min(phi)
    print gsqr_res
    print phi_res
    
    gsqr_phi_image = Image.new('L', (gsqr_res, phi_res), 255)

    print gsqr_phi_image.size
    bins_pixel_value = [0.0] * phi_res * gsqr_res
    print len(bins_pixel_value)
    
    for i in range(len(phi)):

        current_pixel_value = pixel_value[i]
    
    
        phi_bin_lower = 0.0
        phi_bin_upper = 0.0 + phi_bin_size
        phi_bin_index = 0
        
        while phi[i] < phi_bin_lower or phi[i] > phi_bin_upper:

            phi_bin_lower += phi_bin_size

            phi_bin_upper += phi_bin_size

            phi_bin_index += 1
        
            
        gsqr_bin_lower = 0.0
        gsqr_bin_upper = 0.0 + gsqr_bin_size
        gsqr_bin_index = 0
        
        while gsqr[i] < gsqr_bin_lower or gsqr[i] > gsqr_bin_upper:

            gsqr_bin_lower += gsqr_bin_size

            gsqr_bin_upper += gsqr_bin_size

            gsqr_bin_index += 1


        #print current_pixel_value
        bin_index = gsqr_bin_index * phi_bin_index   
        bins_pixel_value[bin_index] += current_pixel_value[0]
    
    #print max(bins_pixel_value)
    bins_pixel_value = np.asarray(bins_pixel_value)
    normalised_bins_pixel_value = bins_pixel_value/max(bins_pixel_value)
    image_data = 255 - (255 * normalised_bins_pixel_value)
    image_data[-1] = 0
    image_data[-2] = 0
    #print len(image_data)
    gsqr_phi_image.putdata(image_data)
    gsqr_phi_image.show()

        

    return
