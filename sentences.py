import random


words=[" "]


def main():
    
    single_past = (get_determiner(1) + (" ") + get_noun(1)+ (" ") + get_verb (0,1)+ (" ") + get_preposition()+ (" ") + get_fun())
    single_present = (get_determiner(1)+ (" ")+ get_noun(1)+ (" ") + get_verb (0,3)+ (" ") + get_preposition()+ (" ") + get_fun())
    single_future = (get_determiner(1) +(" ") + get_noun(1) +(" ")+  get_verb(0,2)+ (" ") + get_preposition()+ (" ") + get_fun())
    plural_past = (get_determiner(2) +(" ") + get_noun(2) +(" ")+  get_verb(0,1)+ (" ") + get_preposition()+ (" ") + get_fun())
    plural_present = (get_determiner(2) +(" ") + get_noun(2) +(" ")+  get_verb(1,2)+ (" ") + get_preposition()+ (" ") + get_fun())
    plural_future = (get_determiner(2) +(" ") + get_noun(2) +(" ")+  get_verb(0,2)+ (" ") + get_preposition()+ (" ") + get_fun())
    
    print ( "-" * 30)
    print (single_past)
    print(single_present)
    print(single_future)
    print (plural_past)
    print (plural_present)
    print (plural_future)
    
    
    print ( "-" * 30)
   
    
    
    
   
   
   
def get_determiner(quantity):
    
     if quantity == 1:
          words = ["a", "one", "the"]
     else:
          words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
     word = random.choice(words).capitalize()
     return word    
    
def get_noun(quantity):
    
    
    if quantity == 1:
        words =["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        
    if quantity == 2:
    
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
        
    word = random.choice(words)

    return word


def get_verb (quantity,tense):
    
    
    if  tense ==1 :
         words= ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
         
    if tense ==2 and quantity == 1:
        words= ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        
    if tense== 2 and quantity == 0:
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
        
    if tense ==3 and quantity == 0: 
       words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    
    word = random.choice(words)
    return word
 
 
def get_preposition():
    
    words = [ "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word      

     #Exceeding the Requirements
     
     
def get_fun():
    
    words= ["the menu", "the car" , "the house", "the guardian", "the women", "the man"]
    
    word =random.choice(words)
    return word

main()
    
    

    
    
    
    
    
    
    
    
    
    
    
  