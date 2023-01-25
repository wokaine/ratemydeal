from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect():
    print("Connecting to database...")
    try:
        client = MongoClient(
        "mongodb+srv://ratemydeal1:'uzcOAvi7vz2b5RYM'@cluster0.u1zrqbz.mongodb.net/?retryWrites=true&w=majority", 
        server_api=ServerApi('1'))
        db = client.get_database('meal_deals')
        posts = db.posts
        print("...Connected")
    except Exception as e:
        print("Error: ", e)

    return client, posts

def uploadPost(main, snack, drink, name="Anonymous"):
    client, posts = connect()
    post = {
        "main": main,
        "snack": snack,
        "drink": drink,
        "submitter": name,
        "likes": 0,
        "dislikes": 0,
        "comments": []
    }
    post_id = posts.insert_one(post).inserted_id

    client.close()

def getPosts():
    client, posts = connect()
    all_posts = list(posts.find({}))

    client.close()

    return all_posts

