import os
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


class IMDBTrainer():
    def __init__(self, path="aclImdb/train"):
        self.scores = []
        self.data = []
        self.size = 0
        # Load up positive and negative reviews
        for X in ["neg", "pos"]:
            for file in os.listdir( os.path.join( path, X ) ):
                s=file.split("_")
                score = int(s[1].replace(".txt",""))
                if X=="neg":
                    self.scores.append( -1 )
                else:
                    self.scores.append(  1 )
                # read the review..
                data = open( os.path.join( path, X, file ), encoding="utf-8" ).read()
                data = data.replace("/>", "").replace("<br", "") #Clean up before processing
                data = data.replace(",", "").replace("!", "") #Clean up before processing
                data = data.replace(".", "").replace("?", "") #Clean up before processing
                data = data.replace("'", "").replace('"', "") #Clean up before processing

                #cleaned_data= self.stopWords(data)
                self.data.append( data )
            
                self.size += 1

    def stopWords(self, data):
        ps = PorterStemmer()
        input_data = data
        stop_words = set(stopwords.words('english'))
 
        #word_tokens = word_tokenize(input_data)
 
        #filtered_sentence = [w for w in input_data if not w in stop_words]
 
        filtered_sentence = ""
        data2=data.split(" ")
        for w in data2:     
            if w not in stop_words:   
                stem=ps.stem(w)
                filtered_sentence += stem + " "
        #print (filtered_sentence)
        return filtered_sentence
 

    def train( self, sentiment ):
        # Spola fram till start
        for i in range(self.size):
            #print (self.data[i])
            sentiment.addStringScore( self.data[i] , self.scores[i] )
            #sentiment.addStringScore( self.data[i] , self.scores[i] ))

    def test( self, sentiment ):
        sentiment_sum = 0
        count = 0
        correct=0
        uncertain=0
        wrong=0
        for i in range(self.size):
            count += 1
            s = sentiment.getStringSentiment( self.data[i])
            if ( s < -0.01 ):
                if self.scores[i] < 0:
                    correct += 1
                else:
                    wrong += 1
            elif ( s > 0.01 ):
                if self.scores[i] > 0:
                    correct += 1
                else:
                    wrong += 1
            else:
                uncertain += 1
        print(correct)
        print("Correct: {}%".format( 100*correct/count ) )
        print("Wrong: {}%".format( 100*wrong/count ) ) 
        print("Uncertain: {}%".format( 100*uncertain/count ) )
        #test

