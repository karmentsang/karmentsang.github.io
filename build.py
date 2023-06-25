import os
import re
import shutil
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

from assets.includes.album import album

# INCLUDES (make sure to call function at the end of the file for ones you'd like to include)

# directories
template_dir = 'templates'
outputs_dir = 'docs'
assets_dir = 'assets'
images_dir = 'assets/images/korea'  # images are all copyright free

# create jinja2 env
env = Environment(loader=FileSystemLoader(template_dir))


# converts md to html
def process_md(content):
    return markdown.markdown(content, output_format='html5')


# extracts the front matter and separates it from content body
def extract_fm(content):
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        # parse as YAML
        fm = yaml.safe_load(match.group(1))
        # return as a tuple
        return fm, match.group(2)


# generate the pages
def build_pages():
    categories = {}  # dictionary for page categories
    fav_pages = []
    # look for md files
    for path, names, filenames in os.walk('content'):
        for filename in filenames:
            if filename.endswith('.md'):
                # read the content of the file
                with open(os.path.join(path, filename), 'r') as f:
                    content = f.read()

                # extract the front matter and body
                fm, body = extract_fm(content)
                # extract the title, description, author and date from the front matter
                title = fm.get('title', os.path.splitext(filename)[0])
                description = fm.get('description', '')
                date = fm.get('date', '')
                author = fm.get('author', '')
                include = fm.get('include', '')
                category = fm.get('category', 'Uncategorized')
                favourite = fm.get('favourite', False)

                # process markdown content
                process = process_md(body)
                output_filename = os.path.splitext(filename)[0] + '.html'
                # define the URL for the page
                url = os.path.relpath(os.path.join(path, output_filename), 'content')

                # render the template and write the output to the output directory
                template = env.get_template('base.html')
                # allow front matter and content to be rendered
                output = template.render(content=process, title=title,
                                         author=author, date=date,
                                         description=description)
                with open(os.path.join(outputs_dir, url), 'w') as f:
                    f.write(output)

                # append the page to the list of generated pages with the correct category
                if not include:  # if page is not included do not generate on homepage
                    continue
                if favourite:
                    fav_pages.append({'title': title,
                                      'url': url,
                                      'description': description,
                                      'date': date})

                if category not in categories:
                    categories[category] = []
                categories[category].append({'title': title,
                                             'url': url,
                                             'description': description,
                                             'date': date})

    # sort the pages in ascending order by date
    for pages in categories.values():
        pages.sort(key=lambda p: p['date'], reverse=True)
    # sort categories into alphabetical order
    categories = dict(sorted(categories.items()))
    fav_pages.sort(key=lambda p: p['date'], reverse=True)

    # get the top 5 most recent pages
    # sort pages using date and pass through 5 items
    recent = []
    for pages in categories.values():
        recent.extend(pages[:5])
    recent.sort(key=lambda x: x['date'], reverse=True)
    recent = recent[:5]

    # generate homepage // TWO TEMPLATES FOR TWO DIFFERENT PERSONAS
    template = env.get_template('index.html')
    final = template.render(categories=categories, recent=recent, favourite=fav_pages)
    with open(os.path.join(outputs_dir, 'index.html'), 'w') as f:
        f.write(final)


# copies the css directory to the output directory
shutil.copytree(os.path.join(assets_dir), os.path.join(outputs_dir, assets_dir), dirs_exist_ok=True)

#  call functions
build_pages()
album()

