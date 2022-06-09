from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tweets = [
    "Sick of having to go to 2 different huts to buy pizza & sunglasses.", 
    "Waabalubbadubbdub", 
    "This is the most annoying part of the assignment",
    "I hate applying concepts from my English high school experiences",
    "Meh, directing my dislike for creating content towards creating content seems to be working",
    "I hope I am doing this first step correctly...",
    "MMMMM pretty sure six isn't enough tweets yet, well here's seven then!",
    "Thankful for machines and how I hopefully won't have to re-type this nonsense a million times!!!",
    "You know, I'm sure I could have just done shorter quotes...",
    "True!"
]

@app.get('/api/tweets')
def tweets_get():
    args = request.args
    # tweetId
    tweet_id = int(args.get('tweetId'))
    # if not tweet_id
    if tweet_id == None:
        return jsonify(tweets), 200
    else:
        return jsonify(tweets[tweet_id]), 200
    
