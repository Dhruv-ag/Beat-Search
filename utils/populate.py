import sys
sys.path.append('../')
import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'songs_project.settings')
django.setup()
from songs_app.models import *

dir_path = os.path.dirname(os.path.realpath(_file_))
import json
from songs_app.models import Post
with open('api.json') as f:
    posts_json=json.load(f)
for post in posts_json:

    post=Post.objects.create(sname=post['Track.Name'],aname=post['Artist.Name'],limit=post['Length'])
