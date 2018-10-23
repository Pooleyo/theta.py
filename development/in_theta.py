image_filename = ["3x4_pixel_value_1.tif"] # "3x4_pixel_value_1.tif" "s10260_PSL_forward_scatter_plate.tif" #"PSL_plate_4_s10268_BBXRD.tif" #"test_forward_scatter.tif"

source_position = [[50.0,0.0,50.0]]  # In mm
offset = [[0,0,0]]  # X offset (mm), Y offset (mm), rotation (degrees)
sample_normal = [[0.0, 0.0, 1.0]]


normal = [[-40.0, 0.0, 40.0]]  # The normal to the plane of the image plate with units mm.

x_scale = [20]  # In mm
y_scale = [20]  # In mm

view_x = [[0.0, 1.0, 0.00]]  # "normalised"
view_y = [[0.71, 0.00, 0.71]]  # "normalised"


wavelength = 1.0  # In Angstroms
a_lattice = 1.0 # In Angstroms

num_subpixels_height = 1
num_subpixels_width = 1

correct_for_filter_attenuation = True
filter_thickness = [0.0]  # [10.0, 6.0]
filter_attenuation_length_at_90_deg = [100.0]  # [34.1, 109.7] # The attenuation length(s) of filter(s) used, in microns.
# Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1
# microns. Al, at 9 keV, has attenuation length of 109.7 microns.

correct_for_sample_attenuation = True

correct_for_polarisation = True

gsqr_limit = [[0.0, 25.0]]
phi_limit = [[-160.0, 160.0]]

num_gsqr_bins = 200
num_phi_bins = 100

plot = True
debug = False
