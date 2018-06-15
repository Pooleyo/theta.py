image_filename = "Nb_test_image.png"#"3x3_white_test_image.tif" #"PSL_plate4_s10257_BBXRD.tif"#"Nb_test_image.png"#"PSL_forward_scatter_plate.tif"


source_position = [50.0,0.0,50.0] # In mm
offset = [0.0,0.0,0.0] # X offset (mm), Y offset (mm), rotation (degrees)

normal = [-10.0, 0.0, 10.0] # The normal to the plane of the image plate with units mm.

x_scale = 20.0 #56 # In mm
y_scale = 20.0 #44 # In mm

view_x = [-0.71, 0.0, -0.71] # "normalised"
view_y = [0.0, 1.0, 0.0] # "normalised"


wavelength = 1.378 # In Angstroms
a_lattice = 3.3 # In Angstroms

filter_thickness = [0.0,0.0] #[10.0, 6.0]
filter_attenuation_length = [34.1,109.7] # The attenuation length(s) of filter(s) used, in microns. Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1 microns. Al, at 9 keV, has attenuation length of 109.7 microns.

phi_limit = [-180.0, 180.0]
gsqr_limit = [-100,100]

theta_phi_n_pixels_width = 100
theta_phi_n_pixels_height = 100

plot = True
debug = False
