use_previous_pixel_loop = False
image_filename = ["masked_s10054_PSL_plate1.tif", "masked_s10054_PSL_plate2.tif", "masked_s10054_PSL_plate3.tif", "masked_s10054_PSL_plate4.tif"] # "3x4_test_image_0_to_12_thru_columns.tif" "s10260_PSL_forward_scatter_plate.tif" #"PSL_plate_4_s10268_BBXRD.tif" #"test_forward_scatter.tif"

source_position = [[50.0, 0.0, 50.0], [50.0, 0.0, 50.0], [50.0, 0.0, 50.0],[50.0, 0.0, 50.0]]  # In mm
offset = [[0.0, 11.7, 180], [-0.5, 11.7, 90], [0.0, 11.7, 0], [0.0, 11.7, 270]]  # X offset (mm), Y offset (mm), rotation (degrees)
sample_normal = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]


normal = [[0.25, 24.6729, 10.9657], [25.704, 0.0, 11.1043], [0.6, -23.9, 12.0], [-24.2, 0.2, 11.1]]  # The normal to the plane of the image plate with units mm.

x_scale = [56.9, 57.1, 56.2, 56.7]  # In mm
y_scale = [42.8, 42.8, 43.0, 43.4]  # In mm

view_x = [[1.00, 0.0, -0.02], [0.0, -1.0, -0.00], [-1.00, 0.0, 0.05], [0.01, 1.0, -0.00]]  # "normalised"
view_y = [[0.02, -0.41, 0.91], [-0.40, -0.0, 0.92], [0.04, 0.45, 0.89], [0.42, 0.0, 0.92]]  # "normalised"


wavelength = 1.8505111  # In Angstroms
a_lattice = 3.3  # In Angstroms

num_subpixels_height = 1
num_subpixels_width = 1

correct_for_filter_attenuation = True
filter_thickness = [10.0, 10.0, 10.0, 10.0]  # [10.0, 6.0]
filter_attenuation_length_at_90_deg = [20.8513, 20.8513, 20.8513, 20.8513]  # [34.1, 109.7] # The attenuation length(s) of filter(s) used, in microns.
# Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1
# microns. Al, at 9 keV, has attenuation length of 109.7 microns.

correct_for_sample_attenuation = True

correct_for_lorentz_polarisation_factor = True

correct_for_atomic_form_factor = True

gsqr_limit = [[3.0, 13.0], [3.0, 13.0], [3.0, 13.0], [3.0, 13.0]]
phi_limit = [[-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0]]

num_gsqr_bins = 500
num_phi_bins = 500
minimum_pixels_per_bin = 6

minimum_pixels_in_column = 10


plot = True
debug = False
