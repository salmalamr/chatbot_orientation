import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ChatBotFinalbackend as backend
import datetime
import csv
import os
#main interface
main=Tk()
multianswers=set()
answers={}
checkboxes=[]
radioboxes=[]

var1=IntVar(value=None)
var2=IntVar(value=None)
#function to clear the window
def clearWindow():
    for widget in main.winfo_children():
                                        widget.destroy()
questions=["Quel est votre nom complet ?","Quels sont les sujets qui vous passionnent?","Quels sont les types d'activités que vous préférez?","Quel est votre rêve de carrière?","Qu'est-ce qui vous motiverait dans un emploi?","Quel type d'environnement de travail préférez-vous?","Quelles sont vos principales aptitudes? ","Quels sont les types de problèmes que vous aimez résoudre? ","Est-ce que vous utilisez déjà des logiciels pour la manipulation d'images ou de vidéos ?"," Avez-vous déjà des notions sur la programmation ?","Est-ce que vous connaissez tous les réseaux sociaux et les utilisez-vous ?","Est-ce que vous avez une idée sur l'infrastructure numérique ?"]                                       
#chatbot window title
main.title("Chatbot")
#window size
main.geometry("1900x900")
question_num=0
choices={1:["arts","technologie","business","ingenierie","science"],2:["travailler en équipe","Travailler seul","Résoudre des problèmes","Apprendre des nouvelles choses","Analyse","Création","Prise de décision","voyage","lecture"],4:["Des opportunités de développement personnel et professionnel","La possibilité de prendre des décisions et d'avoir de l'autonomie","La possibilité de travailler sur des projets innovants","La possibilité de travailler avec des technologies de pointe","La possibilité de travailler dans un environnement international","La possibilité de voyager","L'équilibre vie professionnelle-vie privée"],6:["Esprit de logique","Esprit d’équipe","Esprit de management","Communication","Curiosité, l’envie de s’auto-former","Esprit d’analyse","Esprit de marketing","Esprit de création"],7:["Problèmes techniques","Problème de recherche","Problème commerciaux","Problème de gestion","Problème créatifs"]}
#colors
bg_color="#939BEC"

radios={5:["Bureau","Open-space","Travail à distance","Travail sur terrain"],3:["Entrepreneur","Ingénieur","Infographiste","Enseignant","Marqueteur","Freelancer"]}

button_color="white"
for x in radios:
                for radio in radios.get(x):
                        ind=radios.get(x).index(radio)
                        radios.get(x)[ind]=radio.casefold()
for x in choices:
        for choice in choices.get(x):
                ind=choices.get(x).index(choice)
                choices.get(x)[ind]=choice.casefold()
        


#window bg
main.configure(background=bg_color)
#first_message
welcome_message=tk.Label(main,text="Bienvenue sur notre chatbot d'orientation !\n Pour commencer, veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts,\n vos compétences et vos motivations.\n Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité.\n Nous vous remercions d'avance pour votre participation !",font=("arial,15px"),background=bg_color)
welcome_message.place(x=300,y=300)
indexa=1
#begin the chat button
font=("arial,10")
Y=500
X=900
direct_question=[]
space=' '*150
bot_icon=""
rule=[]


def result():
        global radios,choices
       
        backend.L=multianswers
        
        backend.Question_2()
        backend.Qestions_3(backend.L)
        backend.Question_4(answers["q4"])
        backend.Question_5()
        backend.Question_6(answers["q6"])
        backend.Question_7(backend.L)
        backend.Question_8(backend.L)
        backend.Question_9(answers["q9"])
        backend.Question_10(answers["q10"])
        backend.Question_11(answers["q11"])
        backend.Question_12(answers["q12"])
        filiere=backend.filiere
        options=filiere.values()
        value = [i for i in filiere if filiere[i]==max(options)]
        print(answers)
        print(multianswers)
        print(filiere)
        for x in value:
                if x=="Inf":
                        o=value.index(x)
                        value[o]="Infrastructure digital"
                if x=="Dev":
                        o=value.index(x)
                        value[o]="Développement digital"    

        Label(main,text=f"felicitation ! {answers['q0'] } le meilleur filiere pour vous est le:",background=bg_color,font=font).place(x=200,y=100)
        line=70
        for x in value:
                 Label(main,text="   "+x,font=font,background=bg_color).place(x=300,y=120+line)
                 line+=70
        f=open("file.csv","a")
        wsv=csv.writer(f,delimiter=";")
        wsv.writerow([f"nomComplet :{answers['q0']} filiere :{value}, reponses:{answers} {multianswers}"]) 
        f.close()

def Chatmessage():
        global Y,user_inputlabel,X,indexa
        
        chat=Listbox(main,background="#838DEF",highlightbackground="green",selectbackground="green",font=font,highlightcolor="black",foreground="black",yscrollcommand=50,borderwidth=0,width=125,activestyle='none',disabledforeground="green",highlightthickness=0)
        entry=Entry(main)
        entry.place(x=900,y=500)
        
        chat.insert(1,f"ChatBot:{questions[question_num]}")
        chat.insert(2,space)
        time=datetime.datetime.now()
       
        
       
        # s.insert(2,tim.strftime("%H:%M"))
        
        chat.config()
        chat.place(x=50,y=50)

        def sent():
                global indexa,question_num,Y,answers,checkboxes,radioboxes,multianswers,direct_question,rule,temp
                temp=set()
                
                chat.insert(indexa,space+f"User:")
                try:
                   if question_num in [8,9,10,11]:
                        for x in direct_question:
                                key="q"+str(question_num+1)
                                indexa+=1
                                if x[2].get()==1:
                                        
                                        answers[key]="oui"
                                        chat.insert(indexa,space+f"        oui")
                                        
                                else: 
                                        answers[key]="non"
                                        chat.insert(indexa,space+f"        non")  
                                break             
                        for x in direct_question:
                                 x[0].destroy()
                        direct_question=[]                  
                except Exception as e:
                        print(e)
                try:
                     if question_num in [5,3]:
                        
                                for x in radioboxes:
                                        if x[0]==x[1].get():
                                                key="q"+str(question_num+1)
                                                
                                                answers[key]=(x[2])
                                                indexa+=1
                                                chat.insert(indexa,space+f"         {x[2]}")
                                                
                                                
                         
                                for x in radioboxes:
                                        x[3].destroy()
                                radioboxes=[]                       
                except Exception as e:
                        print(e)                
                try:
                   if question_num in [1,2,4,6,7]:
                        for x in checkboxes:
                                
                                if x[1].get()==1:
                                        rule.append(1)
                                        temp.add(str(x[1]))
                                        
                                        
                                   
                        if len(temp)==0 or len(temp)>3:
                                        messagebox.showinfo("Info","please check at least 1 answer and no more than 3  ")   
                                        question_num-=1  
                                       
                                        temp=set() 
                                         
                                     
                        else:                
                                for l in temp:
                                        indexa+=1
                                        multianswers.add(str(l))
                                        chat.insert(indexa,space+f"     {l}")
                   for x in checkboxes:
                                x[0].destroy()
                                
                   checkboxes=[]  
                        
                                                

                                

                except Exception as e:
                        print(e)
                          

                try:
                        
                        if len(entry.get())==0:
                                messagebox.showinfo("Info","please provide your name") 



                        else:
                                chat.insert(indexa,space+f"User:{entry.get()}")
                                answers["q0"]=entry.get()
                                entry.destroy()
                                question_num+=1
                                             
                except:
                        question_num+=1
                        
                chat.yview_scroll(5,'units')
                
               
                indexa+=1
                try:
                   chat.insert(indexa,f"ChatBot:{questions[question_num]}")
                except:
                        
                        clearWindow()

                        result()
                
                if question_num in choices:
                        Y=380
                        
                        for choice in choices[question_num]:
                                  
                                
                                
                                a=Checkbutton(main,text=choice,font=font,background=bg_color,onvalue=1,offvalue=0,activebackground=bg_color)
                                
                                
                                checkboxes.append( (a,IntVar(name=choice)) )
                                checkboxes[-1][0].configure(variable=checkboxes[-1][1])
                                checkboxes[-1][0].place(x=900,y=Y)
                                Y+=35
                elif question_num in radios:
                       Y=380
                       
                       for radio in radios[question_num]:
                                    
                                
                        
                                a=Radiobutton(main,text=radio,variable=var1,background=bg_color,font=font,value=radios[question_num].index(radio),activebackground=bg_color)
                                
                                
                                radioboxes.append( (radios[question_num].index(radio),var1,radio,a) )
                                a.place(x=900,y=Y)
                                Y+=35
                elif question_num in [8,9,10,11] :
                        Y=500
                        a=Radiobutton(main,text="oui",variable=var2,background=bg_color,value=1,font=font,activebackground=bg_color)
                        b=Radiobutton(main,text="non",variable=var2,background=bg_color,value=0,font=font,activebackground=bg_color)
                        direct_question.append((a,str(question_num-1),var2))
                        direct_question.append((b,str(question_num-1),var2))
                        a.place(x=900,y=Y)
                        b.place(x=900,y=Y+35)

                indexa+=1
        tk.Button(main,text="Send",command=lambda:sent(),width=25,height=4,background=button_color).place(x=900,y=700)  
        tk.Button(main,text="Credits",command=lambda:messagebox.showinfo("Credits","réalisé par:\n\nLAMRIBAH SALMA\n\nEZ-ZYGHAM SOUKAINA\n\nEL AAOUAM MOHAMED"),width=25,height=4,background=button_color).place(x=200,y=700)       
       

                
def conversation():
        clearWindow()
        Chatmessage()

begin=Button(main,text="Commencer",command=conversation,background=button_color,font=font).place(x=750,y=500)        
main.mainloop()


