
def show_post(post):
    print("*********************************************")
    print(f"{post['title']}")
    print(f"Description :\n {post["description"]}")
    print(f"Image: {post["image_url"]}")
    print(f"Posted by: {post["user"]}")

def add_post(id, title, description, image_url, user):
    post = {
        "id": id,
        "title": title,
        "description": description,
        "image_url": image_url,
        "user": user
    }
    posts.append(post)

def update_post(id, key, value):
    # get the post with given id from the database
    # update key with value
    pass

def delete_post(id):
    print("deletin post..")

def get_post(id):
    print("Getting post by id")

posts = [
    {
        "id": 'adk',
        "title": "Learning Python",
        "description": "Learning python",
        "image_url": "https://www.somurl.com/somefile.png",
        "user": ""
    },
    {
        "id": 'adk',
        "title": "Learning Databases",
        "description": "Learning python",
        "image_url": "https://www.somurl.com/somefile.png",
        "user": ""
    },
    {
        "id": 'adk',
        "title": "Learning SQL",
        "description": "Learning python",
        "image_url": "https://www.somurl.com/somefile.png",
        "user": ""
    },
    {
        "id": 'adk',
        "title": "Learning JAVA",
        "description": "Learning python",
        "image_url": "https://www.somurl.com/somefile.png",
        "user": ""
    },
]

# CRUD -> Create, Read, Update, Delete