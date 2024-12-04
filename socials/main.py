from uuid import uuid4
from posts import posts, add_post, update_post, show_post
# get and display all the posts from the database
from utils import display_all_posts_on_homepage


while True:
    question = input("Type 'd' to display all posts, 'a' Add a post,")
    if question == 'd':
        display_all_posts_on_homepage(posts)
    elif question == 'a':
        title = input("Enter the title of your post: ")
        description = input("Enter the description of your post: ")
        image_url = input("Enter the image_url of your post: ")
        user = input("Enter the user of your post: ")
        id = 323
        add_post(id, title, description, image_url, user)
