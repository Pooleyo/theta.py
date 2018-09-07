forward_scatter_filename = "PSL_plate_4_s10268_BBXRD.tif" #"3x3_white_test_image.tif"


source_position = [50.0,0.0,50.0] # In mm
offset = [0,11,270] # X offset (mm), Y offset (mm), rotation (degrees)

normal = [-23.5, 0.0, 12.3] # The normal to the plane of the image plate with units mm.

x_scale = 56 # In mm
y_scale = 44 # In mm

view_x = [0.0, 1.0, -0.00] # "normalised"
view_y = [0.46, 0.00, 0.89] # "normalised"


wavelength = 1.851 # In Angstroms
a_lattice = 3.3 # In Angstroms

filter_thickness = [10.0, 6.0]
filter_attenuation_length = [34.1,109.7] # The attenuation length(s) of filter(s) used, in microns. Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1 microns. Al, at 9 keV, has attenuation length of 109.7 microns.

phi_limit = [-10.0, 10.0]

theta_phi_n_pixels_width = 100
theta_phi_n_pixels_height = 30

plot = True
debug = False
