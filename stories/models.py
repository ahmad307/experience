from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.experience


def add_user(name, email, password):
    """
    Adds a new user to the database.
    :return: True if successful.
    :return: False if user already exists.
    """
    users = db.Users
    # Prevent creating a user with a pre-existing email
    if users.find({'email': email}).count() > 0:
        return False

    user = {
        'name': name,
        'email': email,
        'password': password,
        'articles': []}
    users.insert(user)
    return True


def add_category(name):
    categories = db.CategoryArticles
    categories.insert({'name': name, 'articles': []})


def add_article(title, body, category, topic, email):
    article = {
        'title': title,
        'body': body,
        'category': category,
        'topic': topic,
        'up votes': 0,
        'down votes': 0,
    }

    articles = db.Articles
    users = db.Users
    categories = db.CategoryArticles

    article_id = articles.insert(article)
    # Add the article key to its owner user and its category
    users.update({'email': email},
                 {'$addToSet': {'articles': article_id}})
    categories.update({'name': category},
                      {'$addToSet': {'articles': article_id}})


def delete_user(email):
    """Deletes the given user with all his articles, and
    their corresponding entries in CategoryArticles."""

    articles_to_remove = db.Users.find({'email': email})[0]['articles']
    # Remove all articles from their categories
    db.CategoryArticles.update({}, {
        '$pullAll': {'articles': articles_to_remove}}, multi=True)

    db.Articles.delete_many({'_id': {'$in': articles_to_remove}})
    db.Users.delete_one({'email': email})


def user_valid(email, password):
    users = db.Users
    user = users.find({'email': email})
    if user.count() > 0 and user[0]['password'] == password:
        return True
    else:
        return False


def get_user_data(email):
    """
    Gets a specific user articles.
    :param email: User email.
    :return: Dictionary containing user's name and
     a cursor object containing user articles.
    """
    user = db.Users.find({'email': email})[0]
    articles = db.Articles.find({'_id': {'$in': user['articles']}})
    data = {'name': user['name'], 'articles': articles}
    return data


def add_session(email):
    """Creates a user session."""
    session_id = db.Sessions.insert({'user_email': email})
    return session_id


def get_session_email(session_id):
    return db.Sessions.find({'_id': ObjectId(session_id)})[0]['user_email']


def get_session_username(session_id):
    email = db.Sessions.find({'_id': ObjectId(session_id)})[0]['user_email']
    return db.Users.find({'email': email})[0]['name']


def get_all_articles():
    return db.Articles.find({})
