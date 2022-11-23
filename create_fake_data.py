
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()


from faker import Faker
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post


fake = Faker("ru_RU")

for i in range(5):
    profile = fake.simple_profile()
    if i % 2 == 0:
        last_name = fake.last_name_male()
        first_name = fake.first_name_male()
    else:
        last_name = fake.last_name_female()
        first_name = fake.first_name_female()
    password = fake.password()
    user = User.objects.create_user(profile['username'],
                                    profile['mail'],
                                    password
                                    )
for _ in range(100):
    title = fake.sentence()
    text = fake.paragraph(10)
    author = User.objects.order_by("?")[0]
    post = Post.objects.create(
      author = author,
      title = title,
      text = text
    )  
    post.publish()
