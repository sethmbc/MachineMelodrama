#!/usr/bin/env python
# coding: utf-8

# In[46]:


import random


# In[47]:


Person_List = ["Sheriff Farnworth",
"Person Covered in Black",
"Iona",
"JJ",
"Diego",
"Frances",
"Cindy",
"Jeff Bridges",
"Stacy",
"Jono",
"Butler"
]


# In[48]:


Location_List = ["Early morning. The Schmitt Research Facility",
"Main lab of the Schmitt Research Facility","Randal is sitting in front of a computer frantically typing",
"A small house in a forest in Denmark",
"Blurred city lights from afar",
"A party in a crowded apartment",
"A house in a suburban lane",
"Suburban stripmall",
"Bakery interior",
"Suburban lane, but overgrown with tall grass and weeds",
"An open book on table",
"Driving on a lovely sunny day",
"In a temple",
"Years later",
"A tomb underneath an Egyptian pyramid",
"Agave farm in Oaxaca, Mexico",
"Kids sitting in a classroom",
"A quiet classroom-afternoon",
"Hallway deliberation",
"Years ahead",
"Standing in a construction site",
"Fishing",
"The sound of coffee dripping into the cup",
"A magical forest",
"Hiding from the president",
"The oval office",
"Eating a sandwich",
"A rundown building in the middle of a junkyard",
"Wealthy mansion living room",
"Karen in her apartment living room"]


# In[49]:


Sounds = ["Achoo",
"Babbling",
"Cough",
"Gargle",
"Gibberish",
"Hiccup",
"Hum",
"Chomp",
"Susurration",
"Ululation",
"Whisper",
"Yell"]


# In[57]:


int_list = ["A Baskin-Robbins Ice cream store", "driving along a suburban street", 
            "They appear anxious and ill at ease.",
           "interior of a 70’s car.", "A siren hangs in the distance", "Waiting for a couple umbrellas", 
           "Trying to hold back the pressure of flatulence", "spongebob cackles from a tv in the back",
           "there is no comfort here", "everyone crouches on all fours", "youtube video is buffering", 
           "phones explode in everyones pockets", "Clandestine operations", "sloppy seconds linger in the air", 
           "people cant stop slapping themselves", " a dance is waiting to happen", "Document archive room. Karen is rummaging through the cabins, documents scattered everywhere. Lloyd appears in the hallway holding a cup of coffee. He notices that the archive room door is slightly open, so he peeks in.",
           "Somewhere in the Sonoran Desert",
"Karen and Randal secretly sneak off into the desert to get some alone time from Lloyd."]


# In[58]:


lines2 = ['Ive seen you walk, and its not pretty ', 'What a false narrative you hogs ass']


# In[59]:


lines3 = ['Which side is the gascap lou?', "Does anybody smell oil?",
         "Does anyone hear that weird noise?"]


# In[60]:


anger = ["take it back and I wont tell mom", "I sweat when I look at you", "are male nipples even necessary",]


# In[61]:



lines = open('Fixed_List.txt').read().splitlines()
myline = random.choice(lines)


# In[62]:


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# In[63]:


print(color.BOLD + 'ACT 1' + color.END)
print(color.RED + "\n"+"cut to: "+ random.choice(Location_List) + color.END)
print(color.RED + "\n"+"int: " + random.choice(int_list) + color.END)
print("\n\n"+"Lloyd:")
print(random.choice(lines))
print("\n"+ "Karen(into phone):")
print(random.choice(lines))
print("\n"+"Lloyd:") 
print(random.choice(lines))
print("\n"+"Karen:")
print(random.choice(lines))
print ("\n\n"+"Lloyd:") 
print (random.choice(lines))
print("\n"+"-END SCENE-")
print("\n"+"\n")

print(color.BOLD + 'ACT 2' + color.END)
print(color.RED + "\n"+"cut to: " + random.choice(Location_List) + color.END)
print(color.RED + "\n"+"int: " + random.choice(int_list) + color.END)
print("\n\n"+"Randal:")
print(random.choice(lines))
print("\n"+"Karen:")
print(random.choice(lines))
print("\n"+"Randal:") 
print(random.choice(lines2))
print("\n\n" + "Karen(in a fit of rage):")
print(random.choice(anger))
print("\n\n"+"-END SCENE-")
print("\n\n")

a = random.choice(Person_List)
print(color.BOLD + 'ACT 3' + color.END)
print(color.RED + "\n"+"cut to: " + "Runway, where a Boeing 747 is waiting to take off" + color.END)
print(color.RED + "\n" + "int: Passenger cabin - night, Karen is seated next to Lloyd, Randal, and " + random.choice(Person_List) +" on the plane" + color.END)
print("\n"+"Karen:")
print(random.choice(lines))
print("\n" + "Lloyd:")
print(random.choice(lines))
print("\n"+"Karen:")
print(random.choice(lines))
print("\n\n"+"Pilot (over the telecom):")
print(random.choice(lines3))
print("\n\n"+"Karen(to the camera):")
print(random.choice(lines))
print ("\n"+"Lloyd (to "+ a +"):")
print(random.choice(lines))
print("\n\n"+a+":")
print(random.choice(lines))
print("\n" + "Karen([rolling eyes]):")
print(random.choice(lines))
print (color.RED + "\n\n"+ "cut to: Two police officers enter the plane. They are disheveled and sweating." + color.END) 
print("\n"+ "Police Man 1:") 
print(random.choice(lines))
print("\n"+"Police Woman 1:")
print(random.choice(lines))
print("\n"+a+":")
print(random.choice(lines))     
print("\n\n"+"Randall(yells):")  
print(random.choice(lines))       
print(color.RED + "\n" + "cut to: Police begin to escort " + a + " and Randal off the plane." + color.END )
print("\n" + "Randall(to Karen):") 
print(random.choice(lines))
print("\n"+"Karen(to " + a + "):")
print(random.choice(lines))
print("\n"+ a +"(in a pleading tone):")
print(random.choice(anger))   
print("\n\n"+"-END SCENE-")
print("\n\n")

print(color.BOLD + 'ACT 4' + color.END)
print(color.RED + "\n"+"cut to: " + random.choice(Location_List) + color.END)
print(color.RED + "\n" + "Lloyd died some years ago" + color.RED)
print(color.RED + "\n"+"int: " + random.choice(int_list) + color.END)
print("\n\n"+ "Karen:")
print(random.choice(lines))
print(color.RED + "\n" + "Suddenly Karen is interrupted by a " + random.choice(Sounds) + color.END)
print("\n" + "Karen:")
print(random.choice(lines))
print("\n\n" + "GHOST Lloyd:")
print(random.choice(lines))
print("\n" + "Karen:")
print(random.choice(lines))
print("\n" + "GHOST Lloyd:")
print(random.choice(lines))
print("\n\n"+"-END SCENE-")


# In[ ]:




