def run(image_bin_list, pixel_value):

    print "Summing pixel values in each bin..."

    for current_bin in image_bin_list:
           
        new_pixel_value = 0
        
        for pixel_index in current_bin[2]:
            new_pixel_value += pixel_value[pixel_index]
            
        current_bin[3] = new_pixel_value
        
    return image_bin_list
