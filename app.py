from jinja2 import Environment, FileSystemLoader
import os
import json
import shutil

with open('data.json') as fobj:
    site_data = json.load(fobj)

file_loader = FileSystemLoader("template")
env = Environment(loader=file_loader)

template = env.get_template('content.html').render(site_data)

public_dir = "public"
try:
    #if path already exists, remove it before copying with copytree()
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        shutil.copytree("template/static", public_dir)
except Exception as e:
    print(e)

with open(public_dir+"/index.html","w") as fobj:
    fobj.writelines(template)



