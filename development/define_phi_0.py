def run(phi_plane_normal, phi_0_definer, debug):

    # Inputs: 
    # phi_plane_normal is the normal of the plane in which phi is defined. All vectors pointing from the origin to each
    # pixel will be collapsed into this plane to determine phi.
    # phi_0_definer is the vector which is used to define the phi = 0 degrees direction. The phi_0_definer vector is
    # collapsed into the phi-plane (defined by the phi_plane_normal above). All subsequent origin-pixel vectors are
    # related to this collapsed vector in order to determine their phi position. The phi_0_definer vector can have an
    # arbitrary definition (so long as it is not normal to the phi-plane)

    import numpy as np

    print "Defining phi_0..."

    length_phi_plane_normal = np.linalg.norm(phi_plane_normal)  
    
    unit_phi_plane_normal = phi_plane_normal/length_phi_plane_normal

    # The phi_0_definer is taken and collapsed into the phi_plane. This collapsed vector now defines phi_0.

    length_phi_0_definer = np.linalg.norm(phi_0_definer) 
    
    unit_phi_0_definer = phi_0_definer/length_phi_0_definer  

    parallel_component_unit_phi_0_definer = unit_phi_plane_normal * np.dot(unit_phi_0_definer, unit_phi_plane_normal)

    phi_0_vector = unit_phi_0_definer - parallel_component_unit_phi_0_definer # This vector is in the phi plane. By
    # subtracting the parallel component, the component of the vector in the plane is found.#

    # This check makes sure the vector is actually in the plane.

    if np.dot(phi_0_vector, unit_phi_plane_normal) != 0.0:
        print "\n\n###### Phi_0 definition may be wrong! ######\n\n"
        print "Dot product of unit_phi_0_definer and unit_phi_plane_normal = " + str(
            np.dot(phi_0_vector, unit_phi_plane_normal))
        print "This dot product should be zero, though usually it is very close.\nIf the value is something like e-16" \
              " it is probably fine.\n\n"

    elif np.dot(unit_phi_0_definer, unit_phi_plane_normal) == 1.0:
        print "\n\n###### Phi_0 definition has gone wrong! ######\n\n"

    else:
        pass

    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nphi_plane_normal = " + str(phi_plane_normal)
    + "\nphi_0_definer = " + str(phi_0_definer)
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\nunit_phi_plane_normal = " + str(unit_phi_plane_normal)
    + "\nphi_0_vector = " + str(phi_0_vector)

    + "\n~~~~~~~~~~~~~~~")

    if debug is True:
    
        print debug_message

    return unit_phi_plane_normal, phi_0_vector
