import pandas as pd
import tkinter as tk
import numpy

def submit():
    win.destroy()
    
prob=[]
PB=[]
def probability_neg(choice,weakness,thrush,visual,itching,healing,stiffness,obesity,rows):
    if choice[0]==1:
        prob.append(weakness[2]/(weakness[0]+weakness[2]))
        PB.append((weakness[2]+weakness[3])/row)
    else:
        prob.append(weakness[0]/(weakness[0]+weakness[2]))
        PB.append((weakness[0]+weakness[1])/row)
    if choice[1]==1:
        prob.append(thrush[2]/(thrush[0]+thrush[2]))
        PB.append((thrush[2]+thrush[3])/row)
    else:
        prob.append(thrush[0]/(thrush[0]+thrush[2]))
        PB.append((thrush[0]+thrush[1])/row)
    if choice[2]==1:
        prob.append(visual[2]/(visual[0]+visual[2]))
        PB.append((visual[2]+visual[3])/row)
    else:
        prob.append(visual[0]/(visual[0]+visual[2]))
        PB.append((visual[0]+visual[1])/row)
    if choice[3]==1:
        prob.append(itching[2]/(itching[0]+itching[2]))
        PB.append((itching[2]+itching[3])/row)
    else:
        prob.append(itching[0]/(itching[0]+itching[2]))
        PB.append((itching[0]+itching[1])/row)
    if choice[4]==1:
        prob.append(healing[2]/(healing[0]+healing[2]))
        PB.append((healing[2]+healing[3])/row)
    else:
        prob.append(healing[0]/(healing[0]+healing[2]))
        PB.append((healing[0]+healing[1])/row)
    if choice[5]==1:
        prob.append(stiffness[2]/(stiffness[0]+stiffness[2]))
        PB.append((stiffness[2]+stiffness[3])/row)
    else:
        prob.append(stiffness[0]/(stiffness[0]+stiffness[2]))
        PB.append((stiffness[0]+stiffness[1])/row)
    if choice[6]==1:
        prob.append(obesity[2]/(obesity[0]+obesity[2]))
        PB.append((obesity[2]+obesity[3])/row)
    else:
        prob.append(obesity[0]/(obesity[0]+obesity[2]))
        PB.append((obesity[0]+obesity[1])/row)
    return prob,PB

def probability_pos(choice,weakness,thrush,visual,itching,healing,stiffness,obesity,rows):
    total=weakness[1]+weakness[3]
    if choice[0]==1:
        prob.append(weakness[3]/total)
        PB.append((weakness[2]+weakness[3])/row)
    else:
        prob.append(weakness[1]/total)
        PB.append((weakness[0]+weakness[1])/row)
    if choice[1]==1:
        prob.append(thrush[3]/total)
        PB.append((thrush[2]+thrush[3])/row)
    else:
        prob.append(thrush[1]/total)
        PB.append((thrush[0]+thrush[1])/row)
    if choice[2]==1:
        prob.append(visual[3]/total)
        PB.append((visual[2]+visual[3])/row)
    else:
        prob.append(visual[1]/total)
        PB.append((visual[0]+visual[1])/row)
    if choice[3]==1:
        prob.append(itching[3]/total)
        PB.append((itching[2]+itching[3])/row)
    else:
        prob.append(itching[1]/total)
        PB.append((itching[0]+itching[1])/row)
    if choice[4]==1:
        prob.append(healing[3]/total)
        PB.append((healing[2]+healing[3])/row)
    else:
        prob.append(healing[1]/total)
        PB.append((healing[0]+healing[1])/row)
    if choice[5]==1:
        prob.append(stiffness[3]/total)
        PB.append((stiffness[2]+stiffness[3])/row)
    else:
        prob.append(stiffness[1]/total)
        PB.append((stiffness[0]+stiffness[1])/row)
    if choice[6]==1:
        prob.append(obesity[3]/total)
        PB.append((obesity[2]+obesity[3])/row)
    else:
        prob.append(obesity[1]/total)
        PB.append((obesity[0]+obesity[1])/row)
    return prob,PB
    
    
win=tk.Tk()
win.title("Questionaire")
#win['background']="grey15"
weakness_check=tk.IntVar()
thrush_check=tk.IntVar()
visual_check=tk.IntVar()
itching_check=tk.IntVar()
healing_check=tk.IntVar()
stiffness_check=tk.IntVar()
obesity_check=tk.IntVar()
mainframe=tk.Frame(win,width=36,height=30)
#mainframe.config(bg='grey15')

tk.Label(mainframe,text="Select the symptoms you are facing", justify = tk.LEFT,padx = 20).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Weakness",variable=weakness_check,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Genetical Thrush",variable=thrush_check,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Visual blurring",variable=visual_check,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Itching",variable=itching_check,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Delayed Healing",variable=healing_check,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Muscle Stiffness",variable=stiffness_check,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainframe,text="Obesity",variable=obesity_check,value=1).pack(anchor=tk.W)
tk.Button(mainframe,text="Submit",bg='grey53',command=submit).pack()
mainframe.pack(side=tk.TOP,pady=(5, 10))
win.mainloop()

choices=[weakness_check.get(),thrush_check.get(),visual_check.get(),itching_check.get(),healing_check.get(),stiffness_check.get(),obesity_check.get()]




data_file = pd.read_excel (r'E:\Abdullah\Notes\ptob cep\diabetes_data.xlsx') 
data = pd.DataFrame(data_file)
row=data.shape[0]

weakness=data.pivot_table(index=['weakness','diabetes'], aggfunc='size')
thrush=data.pivot_table(index=['Genital thrush','diabetes'], aggfunc='size')
visual=data.pivot_table(index=['visual blurring','diabetes'], aggfunc='size')
itching=data.pivot_table(index=['Itching','diabetes'], aggfunc='size')
healing=data.pivot_table(index=['delayed healing','diabetes'], aggfunc='size')
stiffness=data.pivot_table(index=['muscle stiffness','diabetes'], aggfunc='size')
obesity=data.pivot_table(index=['Obesity','diabetes'], aggfunc='size')

prob_of_diabetes_pos=(weakness[1]+weakness[3])/row
prob_of_diabetes_neg=(weakness[0]+weakness[2])/row


prob_neg,Pb=probability_neg(choices,weakness,thrush,visual,itching,healing,stiffness,obesity,row)
prob_negative=(numpy.prod(prob_neg)*prob_of_diabetes_neg)/(numpy.prod(Pb)) 

prob_pos,Pb=probability_pos(choices,weakness,thrush,visual,itching,healing,stiffness,obesity,row)
prob_positive=(numpy.prod(prob_pos)*prob_of_diabetes_pos)/(numpy.prod(Pb)) 


prob_sum=prob_negative+prob_positive
positive=(prob_positive/prob_sum)
negative=(prob_negative/prob_sum)

if negative>positive:
    msg="Your results are NEGATIVE"
else:
    msg="Your results are POSITIVE"
#tk.messagebox.showinfo(title='Result',message=msg)
tk.messagebox.showinfo(title="Result",message=msg)