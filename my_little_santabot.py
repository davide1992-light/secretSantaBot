import sys 
import random 
from utils.envVariables import *
from utils.jsonValidator import getJSONdata
from utils.emailDeleter import deleteAllSentEmails
from utils.checkMessageFile import getMessage
import argparse

from mailer import Mailer 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='SecretSantaBot', 
                                     description='A program that helps you create a secret-santa with your distant friends.' )
    parser.add_argument('peopleFile', type=str, metavar='peopleFile', 
                        help="file which contains info about who's partecipating to the secret santa")
    parser.add_argument('messageFile', type=str, metavar='messageFile', 
                         help="file which contains a template of the mail tha will be sent to your friends")
    parser.add_argument('-a', '--address', action='store_true', 
                        help='if this flag is used, address of the person will be sent together with the emails')
    args = vars(parser.parse_args())
    peopleFile, messageFile, address = args['peopleFile'], args['messageFile'], args['address']


    people_data = getJSONdata(peopleFile, addressFlag=address)
    message = getMessage(messageFile, addressFlag=address)
    
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
        message_text = message.format( sender=santa, 
                                       receiver=receiversanta, 
                                       address=people_data[receiversanta]['address'])
        SantaBot.send(receiver=people_data[santa]['mail'],
                      subject='Ho! Ho! Ho!',
                      message=message_text)
        
    deleteAllSentEmails(SANTA_MAIL, SANTA_PASS, 'Ho! Ho! Ho!')
    
    
