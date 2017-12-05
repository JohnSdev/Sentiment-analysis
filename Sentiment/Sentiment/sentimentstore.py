
class SentimentStore:
    def __init__(self):
        # TODO: decide which data structure you need to track
        #       the sentiment of each word
        # TODO: decide which data structure you need to track
        #       the number of times each word has been seen
        self.sent_word_count={}
        self.sent_word_score={}
        self.positive_counter=0
        self.negative_counter=0
        self.wordcount = 0


    
    def getNumberOfWords(self):
        total=0
        for w in self.sent_word_score:
            total += 1
        return total

    def getNumberOfPositiveWords(self):      
        return self.positive_counter

    def getNumberOfNegativeWords(self):   
        return self.negative_counter

    def getTotalWordCount(self):   
        return self.wordcount

    def addWordScore(self, word, score):
        # TODO: add a word with a score
        #        - add score to our running total score for that word
        #        - add 1 to our count for number of times this word has been seen           
            if word not in self.sent_word_score:
                self.sent_word_score[word] = 0 
                self.sent_word_count[word] = 0
            if score >0:
                self.positive_counter +=1
            if score <0:
                self.negative_counter +=1
            wordcount= self.sent_word_count[word]
            count = self.sent_word_score[word]        
            count += score
            wordcount += 1
            self.sent_word_score[word] = count
            self.sent_word_count[word] = wordcount
            self.addIncAndInv()

    def addIncAndInv(self):
        addinc=0
        for w in self.sent_word_score:
            if w == ("very" or "too"):
                self.sent_word_score[w] +=1
            if w == ("barely" or "little"):
                self.sent_word_score[w] -=1
                

    def addStringScore(self, string, score):
        words = string.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                print
                self.addWordScore(word, score)
                self.wordcount += 1

    def getWordSentiment(self, word):
        # TODO: return sentiment score for a given word,
        # TODO: return 0 if word not in store
        if word not in self.sent_word_score:
            return 0
            
        else:
            return self.sent_word_score[word]

    def getWordCount(self, word):
        # TODO: return how many times we have seen a word
        # TODO: return 0 if word not in store

        if word not in self.sent_word_count:
            return 0
        else:
            return self.sent_word_count[word]


    def getNormalizedWordSentiment(self, word):
        # This function is important - by normalizing the data we compensate
        # for the fact that some words occurs far more often than others.
        if self.getWordCount(word) != 0:
            #print (self.getWordCount(word))
            return self.getWordSentiment(word) / self.getWordCount(word)
        else:
            return 0


    def getStringSentiment(self, s):
        score = 0
        count = 0
        words = s.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                count += 1
                word = word.lower()
                score += self.getNormalizedWordSentiment(word)
        return score / count
