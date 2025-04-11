from faker import Faker
from datetime import datetime, timedelta
from models import Post, User
import random

fake = Faker()

def generate_fake_data():
    # Generate users
    users = []
    for i in range(5):
        user = User(
            id=i+1,
            username=fake.user_name(),
            email=fake.email(),
            created_at=fake.date_time_between(start_date='-1y', end_date='now'),
            posts=[]
        )
        users.append(user)

    # Generate posts
    posts = []
    for i in range(20):
        author = random.choice(users)
        created_at = fake.date_time_between(start_date='-6m', end_date='now')
        post = Post(
            id=i+1,
            title=fake.sentence(),
            content='\n\n'.join(fake.paragraphs(nb=3)),
            author_id=author.id,
            author_name=author.username,
            created_at=created_at,
            updated_at=created_at + timedelta(days=random.randint(1, 30)) if random.random() > 0.5 else None
        )
        posts.append(post)
        author.posts.append(post)

    return posts, users