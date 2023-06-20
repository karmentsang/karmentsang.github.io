import os
from PIL import Image
from jinja2 import Environment, FileSystemLoader

# make sure to include this py file in build.py if you would like to generate a photo albums page.

# directories
template_dir = 'templates'
outputs_dir = 'docs'
images_dir = 'assets/images/original_album'

# create jinja2 env
env = Environment(loader=FileSystemLoader(template_dir))


def album():
    # list of image files in the images folder
    photos = os.listdir(images_dir)

    image = [os.path.join(images_dir, f) for f in photos if f.endswith('.jpg')
             or f.endswith('.jpeg') or f.endswith('.png')]

    # extract image properties for each image file
    images = []
    for image in images:
        with Image.open(image) as img:
            filename = os.path.basename(img)
            width, height = img.size
            form = img.format
            size_bytes = os.path.getsize(img)  # get size in bytes
            size_kb = size_bytes / 1024

        # add image properties to list of images
        images.append({'filename': filename,
                       'width': width,
                       'height': height,
                       'format': form,
                       'size_kb': size_kb
                       })

    template = env.get_template('album.html')
    output = template.render(image=image)

    with open(os.path.join(outputs_dir, 'album.html'), 'w') as f:
        f.write(output)
