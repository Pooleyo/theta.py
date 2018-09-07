def run(plot_names, data_names):

    import os
    import shutil

    master_file_directory = "master_images_and_plots"

    if os.path.exists(master_file_directory):

        shutil.rmtree(master_file_directory)

    os.makedirs(master_file_directory)

    for i in plot_names:

        os.rename(i, master_file_directory + "/" + i)

    master_data_directory = "master_csv_data"

    if os.path.exists(master_data_directory):

        shutil.rmtree(master_data_directory)

    os.makedirs(master_data_directory)

    for i in data_names:

        os.rename(i, master_data_directory + "/" + i)

    return
