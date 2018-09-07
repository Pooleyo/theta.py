def run(width, height, pix, phi_limit, gsqr_limit, wavelength, a_lattice, normal, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, phi_0_plane_normal, phi_0_vector, debug):

    import give_gsqr_value
    import calc_angle_between_vectors
    import calc_phi_deg

    print "Calculating gsqr and phi for each pixel..."

    # This first set of lists is used to hold all of the values that fit within our phi and gsqr limits. These will \
    # later be used for the other calculations in the code.

    filter_angles_list_deg = []
    thomson_angles_list_deg = [] 
    gsqr = []
    pixel_value = []
    phi = []

    # This second set of list holds ALL of the values for every pixel; no pixel's values are filtered out including
    # those that exist outside of out phi and gsqr limits. These are only used to make the mask images of the
    # attenuation corrections.

    complete_filter_angles_list_deg = []
    complete_thomson_angles_list_deg = []
    complete_gsqr = []
    complete_pixel_value = []
    complete_phi = []

    for i in range(width):

        for j in range(height):
            current_pixel_value = pix[i,j]

            current_gsqr, vector_origin_to_current_pixel = give_gsqr_value.run(
                i, j, wavelength, a_lattice, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel,
                height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin,
                adjust_to_centre_of_pixel, width, height)

            current_phi_deg = calc_phi_deg.run(
                vector_origin_to_current_pixel, phi_0_plane_normal, phi_0_vector)

            current_filter_angle_deg = calc_angle_between_vectors.run(
                vector_origin_to_current_pixel, normal)

            current_thomson_angle_deg = calc_angle_between_vectors.run(
                vector_origin_to_current_pixel, unit_vector_source_to_origin)

            complete_filter_angles_list_deg.append(abs(current_filter_angle_deg))

            complete_thomson_angles_list_deg.append(abs(current_thomson_angle_deg))

            complete_gsqr.append(current_gsqr)

            complete_phi.append(current_phi_deg)

            complete_pixel_value.append(current_pixel_value)

            if phi_limit[0] <= current_phi_deg <= phi_limit[1] and gsqr_limit[0] <= current_gsqr <= gsqr_limit[1]:

                filter_angles_list_deg.append(abs(current_filter_angle_deg))

                thomson_angles_list_deg.append(abs(current_thomson_angle_deg))

                gsqr.append(current_gsqr)

                phi.append(current_phi_deg)

                pixel_value.append(current_pixel_value)

            else:
                continue

    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nwidth = " + str(width)
    + "\nheight = " + str(height)
    + "\npix = " + str(pix)
    + "\nphi_limit = " + str(phi_limit)
    + "\ngsqr_limit = " + str(gsqr_limit)
    + "\nwavelength = " + str(wavelength)
    + "\na_lattice = " + str(a_lattice)
    + "\nnormal = " + str(normal)
    + "\nnorm_view_x = " + str(norm_view_x)
    + "\nnorm_view_y = " + str(norm_view_y)
    + "\ncentral_pixel = " + str(central_pixel)
    + "\nwidth_mm_per_pixel = " + str(width_mm_per_pixel)
    + "\nheight_mm_per_pixel = " + str(height_mm_per_pixel)
    + "\nvector_origin_to_central_pixel = " + str(vector_origin_to_central_pixel)
    + "\nunit_vector_source_to_origin = " + str(unit_vector_source_to_origin)
    + "\nadjust_to_centre_of_pixel = " + str(adjust_to_centre_of_pixel)
    + "\nphi_0_plane_normal = " + str(phi_0_plane_normal)
    + "\nphi_0_vector = " + str(phi_0_vector) 
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\nfilter_angles_list_deg = " + str(filter_angles_list_deg)
    + "\nthomson_angles_list_deg = " + str(thomson_angles_list_deg)
    + "\ngsqr = " + str(gsqr)
    + "\npixel_value = " + str(pixel_value)
    + "\nphi = " + str(phi)
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return filter_angles_list_deg, thomson_angles_list_deg, gsqr, pixel_value, phi, complete_filter_angles_list_deg, \
           complete_thomson_angles_list_deg, complete_gsqr, complete_pixel_value, complete_phi

