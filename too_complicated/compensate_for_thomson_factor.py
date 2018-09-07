def run(angles_deg, pixel_value, debug):

    import numpy as np


    print "Compensate for Thomson factor..."

    new_pixel_value = []


    thomson_factor_list = []


    for i in range(len(pixel_value)):


        current_angle_rad = np.deg2rad(angles_deg[i])

    
        current_thomson_correction_intermediate = ( 1.0 + np.cos(current_angle_rad) ) / 2.0
    

        current_thomson_factor = 1.0/current_thomson_correction_intermediate

    
        current_new_pixel_value = current_thomson_factor * pixel_value[i]

    
        new_pixel_value.append(current_new_pixel_value)


        thomson_factor_list.append(current_thomson_factor)
    
     
     
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    
    + "\n\nINPUTS:"
    + "\nangles_deg = " + str(angles_deg)
    + "\npixel_value = " + str(pixel_value)
    + "\ndebug = " + str(debug)
  
    + "\n\nOUTPUTS:"
    + "\nnew_pixel_value = " + str(new_pixel_value)
    + "\nthomson_factor_list = " + str(thomson_factor_list)
    + "\n~~~~~~~~~~~~~~~")
    
    
    if debug:
    
        print debug_message


    
    return new_pixel_value, thomson_factor_list
