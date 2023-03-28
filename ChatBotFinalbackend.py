filiere={"Dev":0,"Inf":0,"Marketing":0,"Design":0}
L=[]
D={}

#Question1 : la demande de la 

# print("Quel est votre nom complet ?")
nom_complet=""

#Question2

# print("Quels sont les sujets qui vous passionnent?")
def Question_2():
    global filiere
    
    if "arts".casefold() in L:
        filiere["Design"]=+1
    if "technologie".casefold() in L:
        filiere["Dev"]=+1

    if "business".casefold() in L:
        filiere["Marketing"]=+1
        

    if "ingenierie".casefold() in L:
        filiere["Inf"]=+1
    




  

# Question 3 : Quels sont les types d'activités que vous préférez? (plusieurs réponses possibles)
def Qestions_3(answers):
    Reponses_Q3  = answers

    if "Travailler en équipe".casefold() in Reponses_Q3 : 
        filiere["Dev"] += 1
        filiere["Inf"] += 1
        filiere["Marketing"] += 1
        filiere["Design"]

    if "Travailler seul".casefold() in Reponses_Q3 : 
        filiere["Dev"] += 1
        filiere["Design"] +=1

    if "Résoudre des problèmes".casefold() in Reponses_Q3 : 
        filiere["Dev"] += 1
        

    if "Apprendre des nouvelles choses".casefold() in Reponses_Q3 : 
        filiere["Dev"] += 1
        filiere["Marketing"] += 1
        filiere["Design"] += 1

    if "Analyse".casefold() in Reponses_Q3 : 
        filiere["Dev"] += 1
        filiere["Inf"] += 1
        

    if "Création".casefold() in Reponses_Q3 : 
        
        filiere["Design"] +=1

    if "Prise de décision".casefold() in Reponses_Q3 : 
        
        filiere["Marketing"] += 1
        

    if "voyage".casefold() in Reponses_Q3 : 
        
        filiere["Inf"] += 1
        

    if "lecture".casefold() in Reponses_Q3 : 
        filiere["Dev"] += 1
        filiere["Inf"] += 1
        filiere["Marketing"] += 1
        filiere["Design"] += 1

  

# Question 4 : Quel est votre rêve de carrière?
def Question_4(input_user) :
    
    choix = input_user

    # le premier choix
    if choix.casefold() == "Entrepreneur".casefold() :

        filiere["Dev"] += 1

    # le deuxieme choix
    elif choix.casefold() == "Ingénieur".casefold() :

        filiere["Dev"] += 1
        filiere["Inf"] += 1
        filiere["Marketing"] += 1

    # le troisieme choix
    elif choix.casefold() == "Infographiste".casefold() :

        filiere["Design"] += 1
        
    # le quatrieme choix
    elif choix.casefold() == "Enseignant".casefold() :

        filiere["Inf"] += 1
        
    # le cinqueme choix
    elif choix.casefold() == "Marqueteur".casefold() :

        filiere["Marketing"] += 1
        
    # le deuxieme choix
    elif choix.casefold() == "Freelancer".casefold() :

        filiere["Dev"] += 1
        filiere["Marketing"] += 1
        filiere["Design"] += 1
        
    


#Question5

# print("Qu'est-ce qui vous motiverait dans un emploi?")
def Question_5():
    if "des opportunités de développement personnel et professionnel" in L:
        filiere["Marketing"]+=1
        filiere["Design"]+=1

    if "la possibilité de prendre des décisions et d'avoir de l'autonomie" in L:

        filiere["Design"]+=1

    if "la possibilité de travailler sur des projets innovants" in L:
        filiere["Dev"]+=1

    if "la possibilité de travailler avec des technologies de pointe" in L:
        filiere["Dev"]+=1


    if "la possibilité de travailler dans un environnement international" in L:
        filiere["Dev"]+=1
        
    if "la possibilité de voyager" in L:
        filiere["Inf"]+=1
        
    if "L'équilibre vie professionnelle-vie privée" in L:
        filiere["Dev"]+=1
        filiere["Marketing"]+=1
        filiere["Design"]+=1
        
  

def Question_6(input_user):
    
    choix = input_user

    # le premier choix
    if choix.casefold() == "Bureau".casefold() :

        filiere["Dev"] += 1
        filiere["Marketing"] += 1

    # le deuxieme choix
    elif choix.casefold() == "Open-space".casefold() :

        filiere["Design"] += 1

    # le troisieme choix
    elif choix.casefold() == "Travail à distance".casefold() :

        filiere["Marketing"] += 1
        filiere["Design"] += 1
        
    # le quatrieme choix
    elif choix.casefold() == "Travail sur terrain".casefold() :

        filiere["Inf"] += 1
        



# Question 7 : Quelles sont vos principales aptitudes? (plusieurs réponses possibles)
def Question_7(answers):
    Reponses_Q7  = answers

    if "Esprit de logique".casefold() in Reponses_Q7 : 

        filiere["Dev"] += 1 
        filiere["Design"] += 1

    if "Esprit d'équipe".casefold() in Reponses_Q7 : 

        filiere["Dev"] += 1
        filiere["Inf"] += 1
        
    if "Esprit de management".casefold() in Reponses_Q7 : 
        
        filiere["Inf"] += 1
        
    if "Communication".casefold() in Reponses_Q7 : 
        
        filiere["Dev"] += 1
        filiere["Marketing"] += 1
        filiere["Design"] += 1
        
    if "Curiosité, l'envie de s'auto-former".casefold() in Reponses_Q7 : 
        
        filiere["Dev"] += 1
        filiere["Design"] += 1

    if "Esprit d'analyse".casefold() in Reponses_Q7 : 

        filiere["Inf"] += 1
        
    if "Esprit de marketing".casefold() in Reponses_Q7 : 
        
        filiere["Marketing"] += 1
        
    if "Esprit de création".casefold() in Reponses_Q7 : 
        
        filiere["Design"] += 1

   

# Question 8 : Quels sont les types de problèmes que vous aimez résoudre? (plusieurs réponses possibles)
def Question_8(answers):
    Reponses_Q8  = answers

    if "Problèmes techniques".casefold() in Reponses_Q8 : 

        filiere["Dev"] += 1 
        filiere["Inf"] += 1

    if "Problème de recherche".casefold() in Reponses_Q8 : 

        filiere["Dev"] += 1
        
    if "Problème commerciaux".casefold() in Reponses_Q8 : 
        
        filiere["Marketing"] += 1
        
    if "Problème de gestion".casefold() in Reponses_Q8 : 
        
        filiere["Inf"] += 1
        filiere["Marketing"] += 1
        
    if "Problème créatifs".casefold() in Reponses_Q8 :  
        

        filiere["Design"] += 1

   

#Question 9
def Question_9(input_user):
    # while True:
    #     print("Est-ce que vous utilisez déjà des logiciels pour la manipulation d'images ou de vidéos ?")
    #     print("repond avec oui ou non")
        choix=input_user
        if(choix.casefold()=="oui".casefold()):
            filiere["Design"]+=1
        



#Question 10
def Question_10(input_user):
    # while True:
        
        choix=input_user
        if(choix.casefold()=="oui".casefold()):
            filiere["Dev"]+=1

        


#Question 11
def Question_11(input_user): 
    # while True: 
        choix=input_user
        
        
        if(choix.casefold()=="oui".casefold()):
            filiere["Marketing"]+=1

        
            # break

#Question 12
def Question_12(input_user):
    # while True:

        
        choix=input_user
        if(choix.casefold()=="oui".casefold()):
            filiere["Inf"]+=1

        print(filiere)
        

Base_donnees_chatbot=[{"nomComplet":nom_complet,"filiere":"resultat","reponses":D}]