def run(image_bin_list, image, gsqr_bin_list, phi_bin_list):

    print "Building theta-phi image..."
    
    new_pixel_values = []
    
    for i in image_bin_list:
        new_pixel_values.append(i[3])
        
    
    normalisation_constant = max(new_pixel_values)/float(255)

    for i in range(len(new_pixel_values)):
        
        new_pixel_values[i] = new_pixel_values[i]/normalisation_constant
    
    for i in range(len(new_pixel_values)):

        new_pixel_values[i] = int(abs(new_pixel_values[i] - 255))

    
        

    image_pixels = image.load()
    for i in range(len(gsqr_bin_list)):
        for j in range(len(phi_bin_list)):
            current_pixel_index = i * len(phi_bin_list) + j
            image_pixels[i,j] = (new_pixel_values[current_pixel_index])
     
    return image
    
