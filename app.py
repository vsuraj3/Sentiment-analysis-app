import nltk
from textblob import TextBlob
from nltk.tokenize import word_tokenize
nltk.download("punkt")
import pickle
from flask import Flask, render_template, request


app = Flask(__name__)
app._static_folder = ''
# open a file, where you stored the pickled data
file = open('word_dict', 'rb')
words_dict = pickle.load(file)
file.close()

def sentiment(text):
    words = word_tokenize(text)
    votes = []
    pos_polarity = 0
    neg_polarity = 0
    #adverbs, nouns, adjective, verb are only used
    allowed_words = ['a','v','r','n']
    for word in words:
        if word in words_dict:
            #if word in dictionary, it picks up the positive and negative score of the word
            pos_tag, pos, neg = words_dict[word]
            # print(word, pos_tag, pos, neg)
            if pos_tag in allowed_words:
                if pos > neg:
                    pos_polarity += pos
                    votes.append(1)
                elif neg > pos:
                    neg_polarity += neg
                    votes.append(0)
    #calculating the no. of positive and negative words in total in a review to give class labels
    pos_votes = votes.count(1)
    neg_votes = votes.count(0)
    if pos_votes > neg_votes:
        return 1
    elif neg_votes > pos_votes:
        return 0
    else:
        if pos_polarity < neg_polarity:
            return 0
        else:
            return 1

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact", methods = ['GET','POST'])
def contact():
    return render_template("contact.html")

@app.route("/english",methods=["GET","POST"])
def eng():
    return render_template("eng.html")

@app.route("/hindi",methods=["GET","POST"])
def hindi():
    return render_template("hindi.html")

@app.route("/predict_hindi", methods=["GET","POST"])
def predict_hindi():
    text=request.form.get('text2')
    output=sentiment(text)
    if output==1:
        op="Positive"
    else:
        op="Negative"
    return render_template("hindi.html",prediction_text="Sentiment of given text is {}".format(op))

@app.route("/predict_eng", methods=["GET","POST"])
def predict_eng():
    text=request.form.get('text1')
    blob=TextBlob(text)
    p=blob.polarity
    if p<0:
        op="Neagtive"
    elif p==0:
        op="Neutral"
    else:
        op="Positive"
    return render_template("eng.html",prediction_text="Sentiment of given text is {}".format(op))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
