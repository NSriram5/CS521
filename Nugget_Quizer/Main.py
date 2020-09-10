#Quiz Nugget class
class Quiz_nugget:
    def __init__(self,statement,typeofnugget,date):
        self.statement = statement
        self.datecreated = date
        self.crucialwords = [] #stores crucial word and crucial word pairs along with their index locations in the nugget
        self.noncrucialwords = []
        self.type = typeofnugget
        self.listeditems = []

#Crucial words. These are single or pairs of words that will be swapped out with wrong words.
class CrucialWord:
    def __init__(self,word, index):
        self.word = word
        self.index = index
        self.replacers = []


#Judge if string of text is a list and return the lines if it is
def isList(str):
    array_list = str.splitlines()
    if len(array_list) == 1:
        return False
    else:
        return array_list

#Split a line of text into words so they can be fed into a keyword processing function
def parseWords(str):
    #Code needed here to remove punctuation including {, . /  ( ) ! ? }
    array_words = str.split(' ')
    return array_words

#Need code here to generate a list of pairs of words

#Add words to 