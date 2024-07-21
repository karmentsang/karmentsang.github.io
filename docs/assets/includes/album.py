import os
from PIL import Image
from jinja2 import Environment, FileSystemLoader

# make sure to include this py file in build.py if you would like to generate a photo albums page.

# directories
template_dir = 'templates'
outputs_dir = 'docs'
images_dir = 'assets/images/subs'

# create jinja2 env
env = Environment(loader=FileSystemLoader(template_dir))


def album():
    # list of subdirectories within the images folder
    subdirectories = [f.path for f in os.scandir(images_dir) if f.is_dir()]
    folder_list = []

    for subdir in subdirectories:
        folder_name = os.path.basename(subdir)

        # list of image files in the subdirectory
        photos = os.listdir(subdir)
        images = [os.path.join(subdir, f) for f in photos if
                  f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

        if images:
            folder_data = {
                'folder': folder_name,
                'images': images
            }
            folder_list.append(folder_data)

    template = env.get_template('album.html')
    output = template.render(folders=folder_list)

    with open(os.path.join(outputs_dir, 'album.html'), 'w') as f:
        f.write(output)

