def run(width, height, pix, phi_limit, gsqr_limit, wavelength, a_lattice, normal, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, phi0_plane_normal):

    import give_gsqr_value
    import calc_plane_from_two_vectors
    import calc_angle_between_vectors
        
    print "Calculating gsqr and phi for each pixel..."

    filter_angles_list_deg = []
    thomson_angles_list_deg = [] 
    gsqr = []
    pixel_value = []
    phi = []

    for i in range(width):
        for j in range(height):
            current_pixel_value = pix[i,j]

            current_gsqr, vector_origin_to_current_pixel = give_gsqr_value.run(i, j, wavelength, a_lattice, normal, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, width, height)
            
            
            current_normal_to_plane = calc_plane_from_two_vectors.run(vector_origin_to_current_pixel, [0.0, 0.0, 1.0])

            
            current_phi_deg = calc_angle_between_vectors.run(current_normal_to_plane, phi0_plane_normal)
        
            current_filter_angle_deg = calc_angle_between_vectors.run(vector_origin_to_current_pixel, normal)
            
            
            current_thomson_angle_deg = calc_angle_between_vectors.run(vector_origin_to_current_pixel, unit_vector_source_to_origin)

           
            if current_phi_deg >= phi_limit[0] and current_phi_deg <= phi_limit[1] and current_gsqr >= gsqr_limit[0] and current_gsqr <= gsqr_limit[1] : # Enforces the phi and gsqr limits.
            
                filter_angles_list_deg.append(abs(current_filter_angle_deg))
                thomson_angles_list_deg.append(abs(current_thomson_angle_deg))   
                gsqr.append(current_gsqr)        
                phi.append(current_phi_deg)        
                pixel_value.append(current_pixel_value)
                
            else:
                continue

    return filter_angles_list_deg, thomson_angles_list_deg, gsqr, pixel_value, phi

