'''
Created on 30 mag 2016

@author: corrado
'''
import numpy

global TEST

TEST = ""

pigreco = [0.0000]*26
transition_p = numpy.zeros(shape = (26, 26))


def isletter(carattere):
    return ord(carattere) > 96 and ord(carattere) < 123

def ground_truth():
    
  
    if (TEST == "T"):
        lettere = ["a   ", "b   ", "c   ", "d   ", "e   ", "f   ", "g   ", "h   ", "i   ", "j   ", "k   ", "l   ", "m   ", "n   ", "o   ", "p   ", "q   ", "r   ", "s   ", "t   ", "u   ", "v   ", "w   ", "x   ", "y   ", "z   "]

    word_counter = 0

    #file per il ground truth
    inputfile = open('csv\clean_tweets.csv')



    def iswordcorrect(parola):
        for i in range(len(parola) - 1) :
            if not isletter(parola[i]) :
                if not isletter(parola[i+1]) :
                    return False
        return True

    #def lettercounter(ascii_letter_number) :
    #    return 1          

    for line in inputfile : #leggo tutte le parole 
        line = line.lower() #tutte minuscole #DOVREBBE ESSERE INUTILE PERCHE' E' STATO GIA FATTO NEL PARSE TWEETS, TOGLI
        for word in line.split() : #divido lo stream di char in string appena trovo uno spazio
            if iswordcorrect(word): #if word.isalpha() : #se la word contiene solo char alfabetici(escludo i # ma anche la punteggiatura)
                if isletter(word[0]) : #se il primo char non e' lettera skippo(hashtag o tag o che)
                    pigreco[ord(word[0]) - 97] += 1
                    word_counter += 1
                #ora controllo le P di passare da una lettera all'altra
                if not len(word) == 1 : #se la parola ha length almeno uguale a 2
                    for i in range(len(word)-1): #primo iteratore
                        i += 1 #perdoname madre por mi code loco
                        j = i-1 #j sta dietro a i
                        if isletter(word[i]): #se e' falso qua itera unaltra volta
                            if isletter(word[j]): #se sono tutti e due lettere
                                transition_p[ord(word[i]) - 97][ord(word[j])- 97] += 1
                            else: #se la j non e' lettera vado indietro al massimo di uno ancora
                                if j-1>0 and isletter(word[j-1]):
                                    transition_p[ord(word[i]) - 97][ord(word[j-1])- 97] += 1
  
    inputfile.close()

    if not word_counter == 0:
        for i in range(len(pigreco)):
            pigreco[i] = round(pigreco[i]/word_counter, 4) #divido ogni i dell'array per il # di parole cosi' ho la distr. di P

    for i in range(len(transition_p)):
        counter = 0
        for j in range(len(transition_p[i])):
            counter += transition_p[i][j]
        if not counter == 0:
            for j in range(len(transition_p[i])):
                transition_p[i][j] = transition_p[i][j]/counter #round(transition_p[i][j]/(counter), 4)
    
    
    if (TEST == "T"):
        #stampa vettore pigreco
        print "vettore pigreco:"
        print pigreco
        print "\n" 
        
        #stampa matrice di transizioni
        
        print "matrice transizione:"
        for line in transition_p:
            print line


    print "fine calcolo matrice di transizione"
    
