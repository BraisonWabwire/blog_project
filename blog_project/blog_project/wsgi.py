# backend/blog_project/blog_project/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.blog_project.settings')

application = get_wsgi_application()