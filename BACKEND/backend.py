from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
api=FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
dsans1=["P","O","P","D","R","R","C","A","F","R","E","E","I","E","A","N","T","W","O","O","Z","L","G","S","R","M","A","L","L","O","C","T","I","S","I","A","T","T","N","P","O","T","Y","A","R","R","A","G","E","I","C","D","C","L","I","N","K","O","B","I","N","A","R","Y"]
lrans1=["F","L","O","C","K","I","O","H","W","I","N","D","O","W","F","W","C","N","R","O","T","E","F","E","D","Y","I","A","A","S","N","M","H","I","E","V","I","L","S","X","S","T","A","R","J","Y","O","M","A","R","R","I","E","D","K","T","H","O","U","S","A","N","D","O","N","E"]
eians1=["S","E","L","F","C","O","N","T","R","O","L","T","O","N","E","R","H","M","N","S","E","E","P","E","T","F","N","A","O","E","R","E","G","L","S","S","A","A","T","I","U","U","I","R","H","N","R","A","N","G","E","M","P","A","T","H","Y","P","E","A","C","E","I","N","T","U","T","I","O","N"]

class Dsnode:
    def __init__(self,pos,clue):
        self.pos=pos
        self.clue=clue
        self.prev=None
        self.next=None

ds_a1=Dsnode("a1","Across 1: A user implements undo-redo features using two stacks,that operation is done when undo is triggered?") 
ds_a2=Dsnode("a2","Across 2:To prevent memory leaks in a dynamic list which operation must accompany deletion?")
ds_a3=Dsnode("a3","Across 3:Perform the following operations:push(4),pop(3),push(1)") 
ds_a4=Dsnode("a4","Across 5 :Which kind of memory allocation is used in creation of an array?") 
ds_a5=Dsnode("a5","Across 7:To locate current element in stack what do we use?") 
ds_a6=Dsnode("a6","Across 8:You want to access elements in O(1) time using an index which structure offers this?") 
ds_a7=Dsnode("a7","Across 10:In a node we have data along with ?")
ds_a8=Dsnode("a8","Across 11:When seraching through a sorted array halving the range each time,which method is used? " )
ds_d1=Dsnode("d1","Down 1:A queue where each element has a key and is processed by that key is called?") 
ds_d2=Dsnode("d2","Down 2:Array index starts from?") 
ds_d4=Dsnode("d4","Down 4:A node is deleted but the pointer is not updated in the previous node,what problem arises?") 
ds_d3=Dsnode("d3","Down 3:A recursive function exhausts the call memory and crashes,what has likely been exceeded?") 
ds_d6=Dsnode("d6","Down 6:What type of memory allocation does a C array uses by default?") 
ds_d5=Dsnode("d5","Down 5:Memory leak occurs if this isnt freed?") 

ds_a1.prev=None
ds_a2.prev=ds_a1
ds_a3.prev=ds_a2
ds_a4.prev=ds_a3
ds_a5.prev=ds_a4
ds_a6.prev=ds_a5
ds_a7.prev=ds_a6
ds_a8.prev=ds_a7
ds_d1.prev=ds_a8
ds_d2.prev=ds_d1
ds_d3.prev=ds_d2
ds_d4.prev=ds_d3
ds_d5.prev=ds_d4
ds_d6.prev=ds_d5

ds_a1.next=ds_a2
ds_a2.next=ds_a3
ds_a3.next=ds_a4
ds_a4.next=ds_a5
ds_a5.next=ds_a6
ds_a6.next=ds_a7
ds_a7.next=ds_a8
ds_a8.next=ds_d1
ds_d1.next=ds_d2
ds_d2.next=ds_d3
ds_d3.next=ds_d4
ds_d4.next=ds_d5
ds_d5.next=ds_d6
ds_d6.next=None

class Einode:
    def __init__(self,pos,clue):
        self.pos=pos
        self.clue=clue
        self.prev=None
        self.next=None
    
ei_a1=Einode("a1","Across 1:Jordan got negative feedback but stayed calm asked questions and thanked the manager what skill did he use?")
ei_a2=Einode("a2","Across 9:At a party Arjun notices his friend's body language shift after a joke. He pulls him aside to check in. What is this an example of?")
ei_a3=Einode("a3","Across 10:Nina didnt react to the rude DM. She choose?")
ei_a4=Einode("a4","Across 11:You walk into a room and feels something off no one said anything but you just know what is this inner sense called?")
ei_d1=Einode("d1","Down 1:You know you need help and asking for it takes courage. What do you need?")
ei_d2=Einode("d2","Down 3: heated arguement breaks out ans while others shout, you listen and speak calmy what skill are you showing?")
ei_d3=Einode("d3","Down 5:Silent red flag in a conflict:")
ei_d4=Einode("d4","Down 7:You are really angry with your classmates but you decide to write your feelings down before talking,what are you showing?")
ei_d5=Einode("d6","Down 8:Despite emotional pain you take care of you body and mind through therapy , rest and reflection")
ei_d6=Einode("d9","Down 9:Feeling your heart race before a test equals to this emotion:")
ei_d7=Einode("d10","Down 11:Key EI habit -- stopping before reacting:")

ei_a1.next=ei_a2
ei_a2.next=ei_a3
ei_a3.next=ei_a4
ei_a4.next=ei_d1
ei_d1.next=ei_d2
ei_d2.next=ei_d3
ei_d3.next=ei_d4
ei_d4.next=ei_d5
ei_d5.next=ei_d6
ei_d6.next=ei_d7
ei_d7.next=None

ei_a1.prev=None
ei_a2.prev=ei_a1
ei_a3.prev=ei_a2
ei_a4.prev=ei_a3
ei_d1.prev=ei_a4
ei_d2.prev=ei_d1
ei_d3.prev=ei_d2
ei_d4.prev=ei_d3
ei_d5.prev=ei_d4
ei_d6.prev=ei_d5
ei_d7.prev=ei_d6

class Lrnode:
    def __init__(self,pos,clue):
        self.pos=pos
        self.clue=clue
        self.prev=None
        self.next=None

lr_a1=Lrnode("a1","Across 1:Fish is to school as Bird is to?")
lr_a2=Lrnode("a2","Across 2:I am made of glass and let the outside in. I can open to the world , but I am often closed. What am I?")
lr_a3=Lrnode("a3","Across 7:I am the opposite of good,and when reversed , I let you live. What am I???")
lr_a4=Lrnode("a4","Across 8:Forwards I am something that gives light and warmth, backwards, I am found in sewers")
lr_a5=Lrnode("a5","Across 10:You see a boat filled with people , but there isnt a single person on board. How is that possible?")
lr_a6=Lrnode("a6","Across 11:The smallest number divisible by 7,11,13")
lr_d1=Lrnode("d1","Down 1:A 5 digit number has digits in strictly increasing order. How many such numbers exists?")
lr_d2=Lrnode("d2","Down 2:Hot is to Cold as High is to ____.")
lr_d3=Lrnode("d3","Down 3:I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
lr_d4=Lrnode("d4","Down 6:I have no beginning and no end, yet people often try to define me. I am larger than any number , and my share is sideways eight. What am I??")
lr_d5=Lrnode("d5","Down 8:I visit you every night without warning and leave memories that fade by morning. You chase me when you are awake , but I vanish if you catch me. What am I??")
lr_d6=Lrnode("d6","Down 10:I appear when there is light. But vanish at night.What am I??")
lr_d7=Lrnode("d7","Down 11:I can be cracked , made , told and playes. What am I?")

lr_a1.next=lr_a2
lr_a1.prev=None
lr_a2.next=lr_a3
lr_a2.prev=lr_a1
lr_a3.next=lr_a4
lr_a3.prev=lr_a2
lr_a4.next=lr_a5
lr_a4.prev=lr_a3
lr_a5.next=lr_a6
lr_a5.prev=lr_a4
lr_a6.next=lr_d1
lr_a6.prev=lr_a5
lr_d1.next=lr_d2
lr_d1.prev=lr_a6
lr_d2.next=lr_d3
lr_d2.prev=lr_d1
lr_d3.next=lr_d4
lr_d3.prev=lr_d2
lr_d4.next=lr_d5
lr_d4.prev=lr_d3
lr_d5.next=lr_d6
lr_d6.prev=lr_d5
lr_d7.prev=lr_d6
lr_d6.next=lr_d7
lr_d7.next=None

class INPUTX(BaseModel):
    answers:list[str]
    

#id=1 is ds.2 is ei,3is lr
dsc= Dsnode("head","")
eic= Einode("head","")
lrc= Lrnode("head","")


@api.get("/firstclue/{id}")
def get_firstclue(id: int):
    global dsc, eic, lrc
    if id == 1:
        dsc = ds_a1
        return dsc.clue
    elif id == 2:
        eic = ei_a1
        return eic.clue
    elif id == 3:
        lrc = lr_a1
        return lrc.clue
    else:
        return "Invalid category ID"

@api.get("/nextclue/{id}")
def nextclue(id:int):
    global dsc,eic,lrc
    if id ==1:
        if dsc.next != None:
            dsc= dsc.next
            return dsc.clue  
         
    if id == 2: 
        if eic.next != None:
            eic= eic.next
            return eic.clue
    if id == 3:
        if lrc.next != None:
            lrc=lrc.next
            return lrc.clue 
    else:
        return "invalid path"
   

@api.get("/prevclue/{id}")
def prevclue(id:int):
    global dsc,eic,lrc
    if id==1:
        if dsc.prev != None:
            dsc = dsc.prev
            return dsc.clue
        
    elif id==2:
       if eic.prev!=None:
           eic=eic.prev
           return eic.clue
    elif id==3:
        if lrc.prev!=None:
            lrc=lrc.prev
            return lrc.clue
    else:
        return "INVALID"


def check_answers(ans,inputs):
    result=0
    for ua, ca in zip(ans, inputs):
        if ua!=ca:
            result=1
            break
    return result

@api.post("/checkds")
def dscheck(inputs: INPUTX):
    result = check_answers(dsans1, inputs.answers)
    if result == 0:
        return {"message": "✅ All answers correct!"}
    else:
        return {"message": "❌ Some answers are wrong."}
    
@api.post("/checkei")
def eicheck(inputs: INPUTX):
    result = check_answers(eians1, inputs.answers)
    if result == 0:
        return {"message": "✅ All answers correct!"}
    else:
        return {"message": "❌ Some answers are wrong."}    

@api.post("/checklr")
def lrcheck(inputs: INPUTX):
    result = check_answers(lrans1, inputs.answers)
    if result == 0:
        return {"message": "✅ All answers correct!"}
    else:
        return {"message": "❌ Some answers are wrong."} 

