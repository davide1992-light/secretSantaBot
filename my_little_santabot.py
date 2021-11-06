import sys 
import random 
from utils.envVariables import *
from utils.jsonValidator import getJSONdata
from utils.emailDeleter import deleteAllSentEmails
from utils.checkMessageFile import getMessage

from mailer import Mailer 

if __name__ == '__main__':
    try:        #first we check that both the necessary arguments are passed to the script
        peopleFile, messageFile = sys.argv[1], sys.argv[2]
    except:
        raise Exception('\n\npeoplefile argument or messagefile are missing\n\ncorrect usage: python3 my_littlesantabot.py peoplefile messagefile')
    
    people_data = getJSONdata(peopleFile)
    message = getMessage(messageFile)
    
    SantasWannabe = list(people_data.keys())
    NSantas = len(SantasWannabe) 
    
    #just a normal check on the number of people in the people file; if there are less than three santas, doesn't make sense to do a secret santa...
    if NSantas == 0:
        print('Nobody in the file..')
        raise SystemExit()
    if NSantas == 1: 
        print('You are all alone... Just give a big gift to yourself!')
        raise SystemExit()
    if NSantas == 2:
        print('Well if there are only two people, it is not exactly a "secret" santa')
        raise SystemExit()
    
    #we extract here the names, however we check that the extraction obey certan rules
    goodSantaPermutation = None
    while True:
        shuffledSantas = random.sample(SantasWannabe, k=NSantas)
        SantaToOtherSanta = { santa : othersanta for santa,othersanta in zip(SantasWannabe, shuffledSantas) }
        good = True 
        
        for santa, othersanta in SantaToOtherSanta.items():
            #check for a good permutation (SEE README)
            if (santa == othersanta) or (SantaToOtherSanta[othersanta] == santa) or (othersanta == people_data[santa]['previousSanta']):        
                good = False 
                break 
        if good:
            goodSantaPermutation = SantaToOtherSanta
            break   
    

    SantaBot = Mailer(email=SANTA_MAIL, password=SANTA_PASS)
    for santa, receiversanta in goodSantaPermutation.items():
        SantaBot.send(receiver=people_data[santa]['mail'],
                      subject='Ho! Ho! Ho!',
                      message=message.format( sender=santa, receiver=receiversanta))
        
    deleteAllSentEmails(SANTA_MAIL, SANTA_PASS, IMAP_SERVER, 'Ho! Ho! Ho!')
    
    
