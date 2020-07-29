import sys
sys.path.append('../')
import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','songs_project.settings')
django.setup()
from songs_app.models import *
dir_path=os.path.dirname(os.path.realpath('__file__'))
import json
from songs_app.models import Post
with open('api.json') as f:
    posts_json=json.load(f)
for post in posts_json:
    post=Post.objects.create(sname=post['sname'],aname=post['aname'],limit=post['limit'])
