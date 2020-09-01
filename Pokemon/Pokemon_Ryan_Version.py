"""
Name: Pokemon_Ryan_Version
Purpose: To create a small, playable version of Pokemon
Author: Ryan Blasetti
Created: 1/22/2018
"""

import pygame
import random

# Define some colors
BLACK      = (   0,   0,   0)
WHITE      = ( 255, 255, 255)
GREEN      = (   0, 255,   0)
RED        = ( 255,   0,   0)
BACKGROUND = (   1,   1,   1)
BACKGROUND2 = (  36,  36,  36)
BACKGROUND3 = ( 128, 255, 255)
BACKGROUND4 = ( 153, 217, 234)
FLOOR      = (  99, 178,  46)
TREE_BACK1 = ( 136, 216, 184)
TREE_BACK2 = ( 112, 200, 160)
TREE_BACK3 = (  64, 176, 136)
GRASS_BACK = (  82, 255, 148)
GRASS_BACK2 =(  78, 240, 142)
EXP_BLUE    =( 135, 206, 250)
BEIGE       =( 250, 235, 215)
SALMON      =( 250, 128, 114)

# Define drawing functions
def rect(colour,coords,pixels):
    pygame.draw.rect(screen,colour,coords,pixels)

def ellipse(colour,coords,pixels):
    pygame.draw.ellipse(screen,colour,coords,pixels)

def line(colour,start,end,pixels):
    pygame.draw.line(screen,colour,start,end,pixels)

def polygon(colour,coords,pixels):
    pygame.draw.polygon(screen,colour,coords,pixels)

def arc(colour,coords,start,end,pixels):
    pygame.draw.arc(screen,colour,coords,start,end,pixels)

def addTree(x,y):
    for i in range (0,450,75):
        screen.blit(tree,[x+675,y-450+i])
        screen.blit(tree,[x+450,y-450+i])
    for i in range(2):
        screen.blit(tree,[x+525+i*75,y-450])
    for i in range(0,1050,75):
        if i != 525 and i!=600:
            screen.blit(tree,[x+i,y])
        screen.blit(tree,[x+i,y+675])
    for i in range(0,750,75):
        screen.blit(tree,[x,y+i])
        screen.blit(tree,[x+975,y+i])

def addGrass(x,y):
    for j in range(y,y+301,50):
        for i in range(x,x+150,50):
            screen.blit(poke_grass,[i,j])

def textBox(words):
    rect(WHITE,[0,500,1050,250],0)
    rect(BLACK,[25,525,1000,200],3)
    for i in range (len(words)):
        screen.blit(words[i],[50,550+50*i])

def textBox_Sing(words):
    rect(WHITE,[0,600,1050,150],0)
    rect(BLACK,[25,625,1000,100],3)
    screen.blit(words,[50,650])

# Define functions to determine high scores
def maximum(myList):
    max_index=0
    max=-1
    for i in range(len(myList)):
        if myList[i]>max:
            max=myList[i]
            max_index=i
    return max_index

# Define funtion to animate character movement
def move_animate(counts,moves):
    if count>=0 and count<5:
        active=moves[0]
    elif count>=5 and count<10:
        active=moves[1]
    elif count>=5 and count<15:
        active=moves[2]

    return active

# Define function to save and update high scores
def score_organize(myList):
    new_list=[]
    final_list=[]
    for item in myList:
        new_item=item[:-1]
        new_list.append(int(new_item[6:]))
    for item in myList:
        highest=maximum(new_list)
        final_list.append(myList[highest])
        new_list[highest]=-1

    return final_list

# Define level up function
def level_up(poke_dict):
    stat_list=["Attack","Sp. Attack","Defence","Sp. Defence"]
    poke_dict["Level"]+=1
    health_up=random.randint(1,5)
    poke_dict["Current_HP"]+=health_up
    poke_dict["HP"]+=health_up
    for item in stat_list:
        upgrade_value=random.randint(1,3)
        poke_dict[item]+=upgrade_value
        poke_dict["Max "+item]+=upgrade_value
    return poke_dict

# Define function to display stats of user pokemon
def stat_check(poke_dicts):
    screen.fill(WHITE)
    for i in range(3):
        line(BLACK,[263+i*263,0],[263+i*263,750],3)

    for i in range(4):
        if poke_dicts[i]!="":
            text_1=font.render("Name: "+str(poke_dicts[i]["Name"]),True,BLACK)
            text_2=font.render("Level: "+str(poke_dicts[i]["Level"]),True,BLACK)
            picture=poke_dicts[i]["enemy_sprite"]
            text_3=font.render("Current HP: "+str(poke_dicts[i]["Current_HP"]),True,BLACK)
            text_4=font.render("Max HP: "+str(poke_dicts[i]["HP"]),True,BLACK)
            text_5=font.render("Attack: "+str(poke_dicts[i]["Attack"]),True,BLACK)
            text_6=font.render("Defence: "+str(poke_dicts[i]["Defence"]),True,BLACK)
            text_7=font.render("Sp. Attack: "+str(poke_dicts[i]["Sp. Attack"]),True,BLACK)
            text_8=font.render("Sp. Defence: "+str(poke_dicts[i]["Sp. Defence"]),True,BLACK)
            text_9=font.render("Move 1: "+str(poke_dicts[i]["Move1"]),True,BLACK)
            text_10=font.render("Move 2: "+str(poke_dicts[i]["Move2"]),True,BLACK)
            text_11=font.render("Move 3: "+str(poke_dicts[i]["Move3"]),True,BLACK)
            text_12=font.render("Move 4: "+str(poke_dicts[i]["Move4"]),True,BLACK)
            stats_list=[text_1,text_2,picture,text_3,text_4,text_5,text_6,text_7,text_8,text_9,text_10,text_11,text_12]
            for j in range(len(stats_list)):
                if j<=2:
                    screen.blit(stats_list[j],[15+i*263,60+j*40])
                else:
                    screen.blit(stats_list[j],[15+i*263,190+j*40])

# Define function to reset weakened stats and enemy HP after battle
def stat_reset(good_dict,bad_dict):
    stat_list=["Attack","Sp. Attack","Defence","Sp. Defence"]
    bad_dict["Current_HP"]=bad_dict["HP"]
    for item in stat_list:
        bad_dict[item]=bad_dict["Max "+item]
        good_dict[item]=good_dict["Max "+item]

# Initialize pygame
pygame.init()

# Define changes and variables
move_x=0
move_y=0
original_x=move_x
original_y=move_y
change_x=0
change_y=0
count=0
instructions=""
visible=False
battle=False
potions=1
poke_balls=1
attack=""
choice_poke=""
choice_item=""
score=0
option1=False
option2=False
option3=False
animating=False
counter=0
amount=0
assailant=""
intro=True
colour_active=8
scoreboard=False
tutorial=False
defeat=False
incorrect=True
single=0
read_num=0
gold=100
additional_text=False
one_time=False
fled=False
one_time2=False
stat_screen=False
name_screen=False
user_name=""
bad_name=False

# Set the width and height of the screen [width, height]
size = (1050, 750)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pokemon Ryan Version")

#Loop until the user clicks the close button.
done = False

# Define all images to be used along with colorkeys
still_down=pygame.image.load("still_down.png").convert()
still_down.set_colorkey(BACKGROUND)
move_down=pygame.image.load("move_down.png").convert()
move_down.set_colorkey(BACKGROUND)
middle_down=pygame.image.load("middle_down.png").convert()
middle_down.set_colorkey(BACKGROUND)
still_up=pygame.image.load("still_up.png").convert()
still_up.set_colorkey(BACKGROUND)
move_up=pygame.image.load("move_up.png").convert()
move_up.set_colorkey(BACKGROUND)
middle_up=pygame.image.load("middle_up.png").convert()
middle_up.set_colorkey(BACKGROUND)
still_left=pygame.image.load("still_left.png").convert()
still_left.set_colorkey(BACKGROUND)
move_left=pygame.image.load("move_left.png").convert()
move_left.set_colorkey(BACKGROUND)
middle_left=pygame.image.load("middle_left.png").convert()
middle_left.set_colorkey(BACKGROUND)
still_right=pygame.image.load("still_right.png").convert()
still_right.set_colorkey(BACKGROUND)
move_right=pygame.image.load("move_right.png").convert()
move_right.set_colorkey(BACKGROUND)
middle_right=pygame.image.load("middle_right.png").convert()
middle_right.set_colorkey(BACKGROUND)
left_animations=[still_left,middle_left,move_left]
right_animations=[still_right,middle_right,move_right]
up_animations=[still_up,middle_up,move_up]
down_animations=[still_down,middle_down,move_down]
tree=pygame.image.load("tree.png").convert()
tree.set_colorkey(TREE_BACK2)
poke_heal=pygame.image.load("poke_centre.png").convert()
poke_buy=pygame.image.load("poke_shop.png").convert()
poke_house=pygame.image.load("poke_house.png").convert()
poke_grass=pygame.image.load("tall_grass.png").convert()
poke_grass.set_colorkey(BACKGROUND)
charmander_still=pygame.image.load("charmander.png").convert()
ember1=pygame.image.load("Ember1.png").convert()
ember1.set_colorkey(BLACK)
ember2=pygame.image.load("Ember2.png").convert()
ember2.set_colorkey(BLACK)
ember3=pygame.image.load("Ember3.png").convert()
ember3.set_colorkey(BLACK)
defence1=pygame.image.load("Defence1.png").convert()
defence1.set_colorkey(BACKGROUND)
defence2=pygame.image.load("Defence2.png").convert()
defence2.set_colorkey(BACKGROUND)
defence3=defence1
charm1=pygame.image.load("charm1.png").convert()
charm1.set_colorkey(BACKGROUND2)
charm2=pygame.image.load("charm2.png").convert()
charm2.set_colorkey(BACKGROUND2)
charm3=pygame.image.load("charm3.png").convert()
charm3.set_colorkey(BACKGROUND2)
bite1=pygame.image.load("bite1.png").convert()
bite1.set_colorkey(BACKGROUND)
bite2=pygame.image.load("bite2.png").convert()
bite2.set_colorkey(BACKGROUND)
bite3=pygame.image.load("bite3.png").convert()
bite3.set_colorkey(BACKGROUND)
cut1=pygame.image.load("cut1.png").convert()
cut1.set_colorkey(BACKGROUND3)
cut2=pygame.image.load("cut2.png").convert()
cut2.set_colorkey(BACKGROUND3)
cut3=pygame.image.load("cut3.png").convert()
cut3.set_colorkey(BACKGROUND3)
worry1=pygame.image.load("worry1.png").convert()
worry1.set_colorkey(BACKGROUND3)
worry2=pygame.image.load("worry2.png").convert()
worry2.set_colorkey(BACKGROUND3)
worry3=pygame.image.load("worry3.png").convert()
worry3.set_colorkey(BACKGROUND3)
eye1=pygame.image.load("eye1.png").convert()
eye1.set_colorkey(WHITE)
eye2=pygame.image.load("eye2.png").convert()
eye2.set_colorkey(WHITE)
eye3=pygame.image.load("eye3.png").convert()
eye3.set_colorkey(WHITE)
energy1=pygame.image.load("energy1.png").convert()
energy1.set_colorkey(WHITE)
energy2=pygame.image.load("energy2.png").convert()
energy2.set_colorkey(WHITE)
energy3=pygame.image.load("energy3.png").convert()
energy3.set_colorkey(WHITE)
amnesia1=pygame.image.load("amnesia1.png").convert()
amnesia1.set_colorkey(BACKGROUND4)
amnesia2=pygame.image.load("amnesia2.png").convert()
amnesia2.set_colorkey(BACKGROUND4)
amnesia3=pygame.image.load("amnesia3.png").convert()
amnesia3.set_colorkey(BACKGROUND4)
leer1=pygame.image.load("leer1.png").convert()
leer1.set_colorkey(BACKGROUND4)
leer2=pygame.image.load("leer2.png").convert()
leer2.set_colorkey(BACKGROUND4)
leer3=pygame.image.load("leer3.png").convert()
leer3.set_colorkey(BACKGROUND4)
slash1=pygame.image.load("slash1.png").convert()
slash1.set_colorkey(BACKGROUND4)
slash2=pygame.image.load("slash3.png").convert()
slash2.set_colorkey(BACKGROUND4)
slash3=pygame.image.load("slash2.png").convert()
slash3.set_colorkey(BACKGROUND4)
bubble1=pygame.image.load("bubble1.png").convert()
bubble1.set_colorkey(BACKGROUND4)
bubble2=pygame.image.load("bubble2.png").convert()
bubble2.set_colorkey(BACKGROUND4)
bubble3=pygame.image.load("bubble3.png").convert()
bubble3.set_colorkey(BACKGROUND4)
level_up_img=pygame.image.load("level_up.png").convert()
level_up_img.set_colorkey(BACKGROUND)
potion_item=pygame.image.load("potion.png").convert()
potion_item.set_colorkey(BACKGROUND)
pokeball_item=pygame.image.load("pokeball.PNG").convert()
pokeball_item.set_colorkey(BACKGROUND4)
backspace_key=pygame.image.load("backspace_key.png").convert()
backspace_key.set_colorkey(WHITE)
enter_key=pygame.image.load("enter_key.png").convert()
enter_key.set_colorkey(WHITE)
bulbasaur_still=pygame.image.load("bulbasaur.png").convert()
bulbasaur_still_good=pygame.image.load("bulbasaur_good.png").convert()
charmander_bad=pygame.image.load("charmander_bad.png").convert()
charmander_bad.set_colorkey(BACKGROUND)
squirtle_still=pygame.image.load("squirtle.png").convert()
squirtle_still.set_colorkey(BACKGROUND)
squirtle_still_good=pygame.image.load("squirtle_still_good.png").convert()
poke_back=pygame.image.load("pokemon_back.png").convert()
intro_title=pygame.image.load("intro_text.png").convert()
intro_title.set_colorkey(BACKGROUND)
score_back=pygame.image.load("score_back.png").convert()
score_text=pygame.image.load("score_text.png").convert()
score_text.set_colorkey(BACKGROUND)
professor=pygame.image.load("professor.png").convert()
professor.set_colorkey(BACKGROUND)
professor_poke=pygame.image.load("professor_poke.png").convert()
professor_poke.set_colorkey(BACKGROUND)

# Define channels for sound effects
channel1=pygame.mixer.Channel(0)
channel2=pygame.mixer.Channel(1)
channel3=pygame.mixer.Channel(2)

# Define all music and sound effects
intro_music=pygame.mixer.Sound("intro_music.ogg")
intro_music.set_volume(0.4)
overworld_music=pygame.mixer.Sound("overworld_music.ogg")
overworld_music.set_volume(0.30)
combat_music=pygame.mixer.Sound("combat_music.ogg")
combat_music.set_volume(0.65)
text_ping=pygame.mixer.Sound("text_ping.ogg")
text_ping.set_volume(0.80)
ember_sound=pygame.mixer.Sound("Ember.ogg")
def_curl_sound=pygame.mixer.Sound("DefenseCurl.ogg")
bite_sound=pygame.mixer.Sound("Bite.ogg")
charm_sound=pygame.mixer.Sound("Charm.ogg")
cut_sound=pygame.mixer.Sound("Cut.ogg")
worry_sound=pygame.mixer.Sound("Worry.ogg")
eye_sound=pygame.mixer.Sound("MeanLook.ogg")
energy_sound=pygame.mixer.Sound("EnergyBall.ogg")
bubble_sound=pygame.mixer.Sound("Bubble.ogg")
slash_sound=pygame.mixer.Sound("Slash.ogg")
amnesia_sound=pygame.mixer.Sound("Amnesia.ogg")
leer_sound=pygame.mixer.Sound("Leer.ogg")
level_sound=pygame.mixer.Sound("level_up.ogg")
heal_sound=pygame.mixer.Sound("heal_sound.ogg")
pokeball_sound=pygame.mixer.Sound("pokeball.ogg")
centre_heal_sound=pygame.mixer.Sound("centre_heal.ogg")
centre_heal_sound.set_volume(0.60)
buy_sound=pygame.mixer.Sound("buy_sound.ogg")

# Define font type
font=pygame.font.Font("Mermaid1001.ttf",25)

# Define Pokemon stats, animations, sounds and moves
charmander={
"Name" : "Charmander",
"Level": 5,
"Current_HP": 50,
"HP": 50,
"Attack": 60,
"Max Attack": 60,
"Sp. Attack": 46,
"Max Sp. Attack": 46,
"Defence": 50,
"Max Defence": 50,
"Sp. Defence": 65,
"Max Sp. Defence": 65,
"Move1": "Ember",
"Move1_Dam": 45,
"Move1_Type": "Special",
"Move1_Animations": [ember1,ember2,ember3],
"Move1_Sound": ember_sound,
"Move1_Animation_Type": "Follow",
"Move2": "Bite",
"Move2_Dam": 35,
"Move2_Type": "Physical",
"Move2_Animations": [bite1,bite2,bite3],
"Move2_Sound": bite_sound,
"Move2_Animation_Type": "Enemy",
"Move3": "Charm",
"Move3_Stat": "Attack",
"Move3_Dam": 5,
"Move3_Type": "Stat_Decrease",
"Move3_Animations": [charm1,charm2,charm3],
"Move3_Sound": charm_sound,
"Move3_Animation_Type": "Front",
"Move4": "Defence Curl",
"Move4_Dam": 5,
"Move4_Stat": "Defence",
"Move4_Type": "Stat_Increase",
"Move4_Animations": [defence1,defence2,defence3],
"Move4_Sound":def_curl_sound,
"Move4_Animation_Type": "Self",
"friendly_sprite": charmander_still,
"enemy_sprite": charmander_bad,
"Experience": 0
}

bulbasaur={
"Name" :"Bulbasaur",
"Level": 5,
"Current_HP": 60,
"HP": 60,
"Attack": 35,
"Max Attack": 35,
"Sp. Attack": 51,
"Max Sp. Attack": 51,
"Defence": 70,
"Max Defence": 70,
"Sp. Defence": 70,
"Max Sp. Defence": 70,
"Move1": "Energy Ball",
"Move1_Dam": 50,
"Move1_Type": "Special",
"Move1_Animations": [energy1,energy2,energy3],
"Move1_Sound": energy_sound,
"Move1_Animation_Type": "Follow",
"Move2": "Cut",
"Move2_Dam": 40,
"Move2_Type": "Physical",
"Move2_Animations": [cut1,cut2,cut3],
"Move2_Sound": cut_sound,
"Move2_Animation_Type": "Enemy",
"Move3": "Worry Seed",
"Move3_Stat": "Sp. Attack",
"Move3_Dam": 7,
"Move3_Type": "Stat_Decrease",
"Move3_Animations": [worry1,worry2,worry3],
"Move3_Sound": worry_sound,
"Move3_Animation_Type": "Follow",
"Move4": "Mean Look",
"Move4_Dam": 6,
"Move4_Stat": "Sp. Defence",
"Move4_Type": "Stat_Decrease",
"Move4_Animations": [eye1,eye2,eye3],
"Move4_Sound":eye_sound,
"Move4_Animation_Type": "Self",
"friendly_sprite": bulbasaur_still_good,
"enemy_sprite": bulbasaur_still,
"Experience": 0
}

squirtle={
"Name" : "Squirtle",
"Level": 5,
"Current_HP": 40,
"HP": 40,
"Attack": 62,
"Max Attack": 62,
"Sp. Attack": 71,
"Max Sp. Attack": 71,
"Defence": 50,
"Max Defence": 50,
"Sp. Defence": 55,
"Max Sp. Defence": 55,
"Move1": "Bubble",
"Move1_Dam": 45,
"Move1_Type": "Special",
"Move1_Animations": [bubble1,bubble2,bubble3],
"Move1_Sound": bubble_sound,
"Move1_Animation_Type": "Follow",
"Move2": "Slash",
"Move2_Dam": 40,
"Move2_Type": "Physical",
"Move2_Animations": [slash1,slash2,slash3],
"Move2_Sound": slash_sound,
"Move2_Animation_Type": "Enemy",
"Move3": "Amnesia",
"Move3_Stat": "Sp. Attack",
"Move3_Dam": 6,
"Move3_Type": "Stat_Increase",
"Move3_Animations": [amnesia1,amnesia2,amnesia3],
"Move3_Sound": amnesia_sound,
"Move3_Animation_Type": "Front",
"Move4": "Leer",
"Move4_Dam": 3,
"Move4_Stat": "Defence",
"Move4_Type": "Stat_Decrease",
"Move4_Animations": [leer1,leer2,leer3],
"Move4_Sound":eye_sound,
"Move4_Animation_Type": "Enemy",
"friendly_sprite": squirtle_still_good,
"enemy_sprite": squirtle_still,
"Experience": 0
}

# Define all potential enemy pokemon
charmander_enemy=dict(charmander)
bulbasaur_enemy=dict(bulbasaur)
squirtle_enemy=dict(squirtle)
enemy_list=[charmander_enemy,bulbasaur_enemy,squirtle_enemy]

# Define starting user pokemon
poke_1=level_up(dict(charmander))
all_user_poke=[poke_1,"","",""]
user_poke_name=["Charmander","","",""]
user_poke=all_user_poke[0]

# Define instructive text to put on screen
instruction_1=font.render("Click to buy an item:"+" "*48+"Potion"+" "*12+"Pokeball",True,BLACK)
instruction_2=font.render("Do you want to heal your pokemon?"+" "*20+"Yes"+" "*22+"No",True,BLACK)
instruction_3=font.render("You have encountered a wild pokemon! What will you do?",True,BLACK)
instruction_4=font.render("Fight" +" "*130 + "Pokemon",True,BLACK)
instruction_5=font.render("Item" +" "*131 + "Flee",True,BLACK)
instruction_6=font.render("Select an attack",True,BLACK)
instruction_7=font.render(user_poke["Move1"] +" "*130 + user_poke["Move2"],True,BLACK)
instruction_8=font.render(user_poke["Move3"] +" "*131 + user_poke["Move4"],True,BLACK)
instruction_9=font.render("Choose a pokemon:",True,BLACK)
instruction_10=font.render(user_poke_name[0] +" "*130 + user_poke_name[1],True,BLACK)
instruction_11=font.render(user_poke_name[2] +" "*131 + user_poke_name[3],True,BLACK)
instruction_12=font.render("Choose an item:",True,BLACK)
instruction_13=font.render("Potion: " +str(potions) +" "*130 + "Pokeball: "+str(poke_balls),True,BLACK)
battle_words=[instruction_3,instruction_4,instruction_5]
battle_words_fight=[instruction_6,instruction_7,instruction_8]
battle_words_poke=[instruction_9,instruction_10,instruction_11]
battle_words_item=[instruction_12,instruction_13]
blank=font.render("",True,BLACK)
main_button1=font.render("Play",True,BLACK)
main_button2=font.render("Scoreboard",True,BLACK)
main_button3=font.render("Instructions",True,BLACK)
main_button4=font.render("Quit",True,BLACK)
buttons=[main_button1,main_button2,main_button3,main_button4]
return_choice=font.render("Back",True,BLACK)
bad_name_text=font.render("Your name cannot be more than five letters!",True,BLACK)
inform_name=font.render("Enter a name that is five letters or less:",True,BLACK)
cont=font.render("Continue:",True,BLACK)
back=font.render("Delete:",True,BLACK)
tutorial1=font.render("Hello there! Glad to meet you!",True,BLACK)
tutorial2=font.render("Welcome to the world of Pokemon!",True,BLACK)
tutorial3=font.render("Press space bar to continue dialogue.",True,BLACK)
tutorial4=font.render("My name is Oak.",True,BLACK)
tutorial5=font.render("People affectionately refer to me as the pokemon professor.",True,BLACK)
tutorial6=font.render("This world is inhbited far and wide,",True,BLACK)
tutorial7=font.render("By these creatures called pokemon,",True,BLACK)
tutorial8=font.render("Much like the one beside me.",True,BLACK)
tutorial9=font.render("In this world it is your objective to be the best pokemon trainer!",True,BLACK)
tutorial10=font.render("In order to do so, you must catch and defeat as many wild pokemon as possible.",True,BLACK)
tutorial11=font.render("After each battle that you win, your score will go up,",True,BLACK)
tutorial12=font.render("But watch out, if all your pokemon are defeated, you lose!",True,BLACK)
tutorial13=font.render("Don't worry though, there is a pokemon centre that you can use to prevent that.",True,BLACK)
tutorial14=font.render("As for controls, you can move with the arrow keys and press TAB to check your pokemon.",True,BLACK)
tutorial15=font.render("You can interact with either the orange or blue building with the space bar.",True,BLACK)
tutorial16=font.render("However, when you see text boxes, use the mouse to make your selection.",True,BLACK)
tutorial17=font.render("Some important things to note are that:",True,BLACK)
tutorial18=font.render("a) You can only have a maximum of 4 pokemon, so choose wisely.",True,BLACK)
tutorial19=font.render("b) Potions cost 100 gold while Pokeballs cost 200 gold.",True,BLACK)
tutorial20=font.render("As for the rest, I'm sure you'll learn very soon,",True,BLACK)
tutorial21=font.render("So when you're ready, press start to play!",True,BLACK)
tutorial_list=[[tutorial1,tutorial2,tutorial3],[tutorial4,tutorial5,tutorial6],[tutorial7,tutorial8,tutorial9],[tutorial10,tutorial11,tutorial12],[tutorial13,tutorial14,tutorial15],[tutorial16,tutorial17,tutorial18],[tutorial19,tutorial20,tutorial21]]
tutorial_read=tutorial_list[read_num]

# Set starting instructions
instructions=instruction_1

# Define animation changes
character=still_down

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        # Check to see if the user is on the main screen
        if intro:

            #Get mouse positions
            pos = pygame.mouse.get_pos()
            pos_x=pos[0]
            pos_y=pos[1]

            #Check where the user clicks and switch to the appropriate screen along with the colour of the button
            if pos_x>=425 and pos_x <= 625 and pos_y>=200 and pos_y<=280:
                colour_active=0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro=False
                    single=0
                    name_screen=True
                    user_name=""
                    channel2.play(text_ping)
                    channel1.stop()
            elif pos_x>=425 and pos_x <= 625 and pos_y>=325 and pos_y<=405:
                colour_active=1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    scoreboard=True
                    intro=False
                    channel2.play(text_ping)
                    channel1.stop()
            elif pos_x>=425 and pos_x <= 625 and pos_y>=450 and pos_y<=530:
                colour_active=2
                if event.type == pygame.MOUSEBUTTONDOWN:
                   tutorial=True
                   intro=False
                   channel2.play(text_ping)
                   channel1.stop()
            elif pos_x>=425 and pos_x <= 625 and pos_y>=575 and pos_y<=655:
                colour_active=3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done=True
            else:
                colour_active=8

        #Check to see if the user is on the naming screen and has a valid name
        elif name_screen and incorrect:

                # Let the user type their name and ress enter to continue
                try:
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_BACKSPACE:
                            user_name=user_name[:-1]
                            if len(user_name)<5:
                                bad_name=False
                        elif event.key==pygame.K_RETURN:
                            name_screen=False
                            name=user_name
                            while len(name)<5:
                                name+=" "
                            incorrect=False
                        elif event.key>=97 and event.key<=122:
                            if len(user_name)<5:
                                user_name+=chr(event.key)
                                bad_name=False
                            else:
                                raise ValueError
                        else:
                            pass
                except ValueError:
                    bad_name=True

        # Check to see if the user went to the tutorial screen
        elif tutorial:

            # Allow the user to navigate the tutorial with the space bar
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    read_num+=1
                    channel2.play(text_ping)
                    if read_num>6:
                        tutorial=False
                        intro=True
                        read_num=0
                    else:
                        tutorial_read=tutorial_list[read_num]

        # Check if the user is on the scoreboard screen
        elif scoreboard:

            # Allow the user to navigate the scoreboard screen and press back to return to main screen
            pos = pygame.mouse.get_pos()
            pos_x=pos[0]
            pos_y=pos[1]
            if pos_x>=250 and pos_x<=450 and pos_y>=655 and pos_y<=715:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    channel2.play(text_ping)
                    scoreboard=False
                    intro=True

        # Check if the user is in the over world
        elif not battle:

            # If instructions are on screen, do not allow the user to move, but navigate with mouse
            if visible:
                pos = pygame.mouse.get_pos()
                pos_x=pos[0]
                pos_y=pos[1]

            # Check if the user presses a key
            elif event.type==pygame.KEYDOWN:

                # Change variable that moves entire screen opposed to character
                if event.key==pygame.K_LEFT:
                    change_x=3
                elif event.key==pygame.K_RIGHT:
                    change_x=-3
                if event.key==pygame.K_UP:
                    change_y=3
                elif event.key==pygame.K_DOWN:
                    change_y=-3

                # If user holds tab, display stat screen
                if event.key==pygame.K_TAB:
                    stat_screen=True

                # Check if the user is near an interactable house when they press space, giving them options
                if event.key==pygame.K_SPACE:
                    if move_x>-366 and move_x<-273:
                        if move_y>75 and move_y<100:
                            instructions=instruction_1
                            channel2.play(text_ping)
                            visible=True
                    elif move_x>177 and move_x<279:
                        if move_y>75 and move_y<100:
                            instructions=instruction_2
                            channel2.play(text_ping)
                            visible=True

            # Check to see if user lifts a key
            elif event.type==pygame.KEYUP:

                # Stop displaying start screen if user stops holding tab
                if event.key==pygame.K_TAB:
                    stat_screen=False

                # Stop movement when the character lifts a key
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    change_x=0
                elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    change_y=0

        # Check to see if the user is in combat
        elif battle:

            # Update changing instructive text
            instruction_7=font.render(user_poke["Move1"] +" "*130 + user_poke["Move2"],True,BLACK)
            instruction_8=font.render(user_poke["Move3"] +" "*131 + user_poke["Move4"],True,BLACK)
            instruction_10=font.render(user_poke_name[0] +" "*130 + user_poke_name[1],True,BLACK)
            instruction_11=font.render(user_poke_name[2] +" "*131 + user_poke_name[3],True,BLACK)
            instruction_13=font.render("Potion: " +str(potions) +" "*130 + "Pokeball: "+str(poke_balls),True,BLACK)
            battle_words_fight=[instruction_6,instruction_7,instruction_8]
            battle_words_poke=[instruction_9,instruction_10,instruction_11]
            battle_words_item=[instruction_12,instruction_13]

            # Allow the user to navigate battle with mouse, not keyboard
            pos = pygame.mouse.get_pos()
            pos_x=pos[0]
            pos_y=pos[1]

            # Check if the user decided to flee and allow them to leave the battle but reset enemy HP
            if fled:
                pygame.time.wait(3000)
                one_time=False
                combat_music.stop()
                battle=False
                stat_reset(user_poke,enemy_poke)
                fled=False
                instructions=""

            #Check to see which combat option is selected by the user
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check to see if the upper left box is selected
                if pos_x>=27 and pos_x <= 524 and pos_y>=590 and pos_y<=637:

                    # If the pokemon option was selected prior, switch to pokemon 1
                    if option2:
                        if all_user_poke[0]!="":
                            channel2.play(text_ping)
                            choice_poke=all_user_poke[0]
                            option2=False

                    # If the item option was selected prior, allow use of potion if there is one
                    elif option3:
                        channel2.play(text_ping)
                        choice_item="potion"
                        option3=False

                    # If the fight option was selected prior, use move 1
                    elif option1:
                        channel2.play(text_ping)
                        attack=user_poke["Move1"]
                        attack_dam=user_poke["Move1_Dam"]
                        attack_type=user_poke["Move1_Type"]
                        attack_animation_type=user_poke["Move1_Animation_Type"]
                        animation_list=user_poke["Move1_Animations"]
                        attack_sound=user_poke["Move1_Sound"]
                        if attack_type!="Special" and attack_type!="Physical":
                            attack_stat=user_poke["Move1_Stat"]
                        option1=False

                    # Select the fight option
                    else:
                        channel2.play(text_ping)
                        instructions=battle_words_fight
                        option1=True

                # Check to see if the upper right box is selected
                elif pos_x>=525 and pos_x <= 1025 and pos_y>=590 and pos_y<=637:

                    # If the pokemon option was selected prior, switch to pokemon 2
                    if option2:
                        if all_user_poke[1]!="":
                            channel2.play(text_ping)
                            choice_poke=all_user_poke[1]
                            option2=False

                    # If the item option was selected prior, allow use of pokeball if there is one
                    elif option3:
                        channel2.play(text_ping)
                        choice_item="pokeball"
                        option3=False

                    # If the fight option was selected prior, use move 2
                    elif option1:
                        channel2.play(text_ping)
                        attack=user_poke["Move2"]
                        attack_dam=user_poke["Move2_Dam"]
                        attack_type=user_poke["Move2_Type"]
                        attack_animation_type=user_poke["Move2_Animation_Type"]
                        animation_list=user_poke["Move2_Animations"]
                        attack_sound=user_poke["Move2_Sound"]
                        if attack_type!="Special" and attack_type!="Physical":
                            attack_stat=user_poke["Move2_Stat"]
                        option1=False

                    # Select the pokemon option
                    else:
                        channel2.play(text_ping)
                        instructions=battle_words_poke
                        option2=True

                # Check to see if the lower left box is selected
                elif pos_x>=27 and pos_x <= 524 and pos_y>=638 and pos_y<=685:

                    # If the pokemon option was selected prior, switch to pokemon 3
                    if option2:
                        if all_user_poke[2]!="":
                            channel2.play(text_ping)
                            choice_poke=all_user_poke[2]
                            option2=False

                    # If the fight option was selected prior, use move 3
                    elif option1:
                        channel2.play(text_ping)
                        attack=user_poke["Move3"]
                        attack_dam=user_poke["Move3_Dam"]
                        attack_type=user_poke["Move3_Type"]
                        attack_animation_type=user_poke["Move3_Animation_Type"]
                        animation_list=user_poke["Move3_Animations"]
                        attack_sound=user_poke["Move3_Sound"]
                        if attack_type!="Special" and attack_type!="Physical":
                            attack_stat=user_poke["Move3_Stat"]
                        option1=False

                    # If the item option was selected prior, do not allow continuation as there is no item here
                    elif option3:
                        pass

                    # Select the item option
                    else:
                        channel2.play(text_ping)
                        instructions=battle_words_item
                        option3=True

                # Check to see if the lower right box is selected
                elif pos_x>=525 and pos_x <= 1025 and pos_y>=638 and pos_y<=685:

                    # If the pokemon option was selected prior, switch to pokemon 4
                    if option2:
                        if all_user_poke[3]!="":
                            channel2.play(text_ping)
                            choice_poke=all_user_poke[3]
                            option2=False

                    # If the fight option was selected prior, use move 1
                    elif option1:
                        channel2.play(text_ping)
                        attack=user_poke["Move4"]
                        attack_dam=user_poke["Move4_Dam"]
                        attack_type=user_poke["Move4_Type"]
                        attack_animation_type=user_poke["Move4_Animation_Type"]
                        animation_list=user_poke["Move4_Animations"]
                        attack_sound=user_poke["Move4_Sound"]
                        if attack_type!="Special" and attack_type!="Physical":
                            attack_stat=user_poke["Move4_Stat"]
                        option1=False

                    # If the item option was selected prior, do not allow continuation as there is no item here
                    elif option3:
                        pass

                    # Select the flee option
                    else:
                        channel2.play(text_ping)
                        flee_text1=font.render("You have fled from the battle.",True,BLACK)
                        instructions=[flee_text1,blank]
                        fled=True

                # Allow the user to return to the main selection page if they choose an option they did not want
                if instructions!=battle_words and not fled:
                    if pos_x>=350 and pos_x <= 570 and pos_y>=690 and pos_y<=720:
                        channel2.play(text_ping)
                        instructions=battle_words
                        option1=False
                        option2=False
                        option3=False



    # --- Game logic should go here
    # i.e calculations for positions, variable updates

    # Check if the user is on the intro page and play the intro music
    if intro:
        if not channel1.get_busy():
            channel1.play(intro_music)

    # Do not allow other pages' logic to be active if on name screen
    elif name_screen:
        pass

    # Do not allow other pages' logic to be active if on tutorial screen
    elif tutorial:
        pass

    # Check if the user is on the scoreboard screen
    elif scoreboard:

        # Open the score file and print the top 10 scores
        if single==0:
            infile=open("scores.txt","r")
            old_score_list=infile.readlines()
            infile.close()
            outfile=open("scores.txt","w")
            new_score_list=[]

            # If the user is brought to this screen by death, update the scores with the user's scores and name. Also reset game variable in case of retry
            if defeat:
                old_score_list.append(name+":"+str(score)+"\n")
                count=0
                charmander_enemy=dict(charmander)
                bulbasaur_enemy=dict(bulbasaur)
                squirtle_enemy=dict(squirtle)
                enemy_list=[charmander_enemy,bulbasaur_enemy,squirtle_enemy]
                poke_1=level_up(dict(charmander))
                all_user_poke=[poke_1,"","",""]
                user_poke_name=["Charmander","","",""]
                user_poke=all_user_poke[0]
                instructions=""
                potions=1
                poke_balls=1
                choice_poke=""
                choice_item=""
                score=0
                battle=False
                option1=False
                option2=False
                option3=False
                counter=0
                amount=0
                assailant=""
                incorrect=True
                read_num=0
                gold=100
                additional_text=False
                one_time=False
                move_x=0
                move_y=0

            # Update the file with the new scores to save between plays
            new_score_list=score_organize(old_score_list)
            single=1
            outfile.writelines(new_score_list)
            outfile.close()

    # Check to see if the user is in the overworld
    elif not battle:

        # PLay overworld music
        if not channel1.get_busy():
            channel1.play(overworld_music)

        # Check to see if instructions are being displayed
        if visible:

            #Check to see if the user clicks on the first box
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_x>=490 and pos_x <= 620 and pos_y>=630 and pos_y<=677:

                    # If the user is in the poke centre, heal their pokemon
                    if instructions==instruction_2:
                        channel2.play(text_ping)
                        for i in range(4):
                            if all_user_poke[i]!="":
                                all_user_poke[i]["Current_HP"]=all_user_poke[i]["HP"]
                        channel3.play(centre_heal_sound)
                        while channel3.get_busy():
                            pass
                        visible=False

                    # If the user is in the poke mart and they have enough gold, let them buy a potion
                    elif instructions==instruction_1:
                        if gold>=100:
                            channel2.play(text_ping)
                            potions+=1
                            gold-=100
                            channel3.play(buy_sound)
                            while channel3.get_busy():
                                pass
                            visible=False

                #Check to see if the user clicks on the second box
                elif pos_x>=635 and pos_x <= 765 and pos_y>=630 and pos_y<=677:

                    # If the user is in the poke centre, do not heal their pokemon
                    if instructions==instruction_2:
                        channel2.play(text_ping)
                        visible=False

                    # If the user is in the poke mart and they have enough gold, let them buy a pokeball
                    elif instructions==instruction_1:
                        if gold>=200:
                            channel2.play(text_ping)
                            poke_balls+=1
                            gold-=200
                            channel3.play(buy_sound)
                            while channel3.get_busy():
                                pass
                            visible=False

                # if the user is in the poke mart and clicks back, exit the store menu
                elif pos_x>=462 and pos_x <= 572 and pos_y>=695 and pos_y<=720:
                    if instructions==instruction_1:
                        visible=False

        # Check to see if the user presses a key
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:

                # Prevent player from walking through trees on main path
                if move_y>300:
                    if move_x<-65:
                        count+=1
                        if count>=15:
                            count=0
                        character=move_animate(count,left_animations)
                        move_x+=change_x

                # Prevent player from walking through buildings
                elif move_y>102 and move_y<258:
                    if move_x<-230 and move_x>-435:
                        count+=1
                    elif move_x<320 and move_x>120:
                        count+=1
                    else:
                        if move_x<390:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,left_animations)
                            move_x+=change_x

                # Prevent player from walking through buildings
                elif move_y>-180 and move_y<-30:
                    if move_x<-230 and move_x>-435:
                        count+=1
                    elif move_x<320 and move_x>120:
                        count+=1
                    else:
                        if move_x<390:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,left_animations)
                            move_x+=change_x

                # Prevent player from walking through trees in main area
                elif move_x<390:
                    count+=1
                    if count>=15:
                        count=0
                    character=move_animate(count,left_animations)
                    move_x+=change_x



            elif event.key==pygame.K_RIGHT:

                # Prevent player from walking through trees on main path
                if move_y>300:
                    if move_x>-175:
                        count+=1
                        if count>=15:
                            count=0
                        character=move_animate(count,right_animations)
                        move_x+=change_x

                # Prevent player from walking through buildings
                elif move_y>102 and move_y<258:
                    if move_x<-217 and move_x>-430:
                        count+=1
                    elif move_x<327 and move_x>125:
                        count+=1
                    else:
                        if move_x>-477:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,right_animations)
                            move_x+=change_x

                # Prevent player from walking through buildings
                elif move_y>-180 and move_y<-30:
                    if move_x<-217 and move_x>-430:
                        count+=1
                    elif move_x<327 and move_x>125:
                        count+=1
                    else:
                        if move_x>-477:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,right_animations)
                            move_x+=change_x

                # Prevent player from walking through trees in main area
                elif move_x>-477:
                    count+=1
                    if count>=15:
                        count=0
                    character=move_animate(count,right_animations)
                    move_x+=change_x

            elif event.key==pygame.K_DOWN:

                # Prevent player from walking through buildings
                if move_x<323 and move_x>125:
                    if move_y<265 and move_y>100:
                        count+=1
                    elif move_y>-180 and move_y<-24:
                        count+=1
                    else:
                        if move_y>-275:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,down_animations)
                            move_y+=change_y

                # Prevent player from walking through buildings
                elif move_x<-220 and move_x>-430:
                    if move_y<265 and move_y>100:
                        count+=1
                    elif move_y>-180 and move_y<-24:
                        count+=1
                    else:
                        if move_y>-275:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,down_animations)
                            move_y+=change_y

                # Prevent player from walking through trees in main area
                elif move_y>-275:
                    count+=1
                    if count>=15:
                        count=0
                    character=move_animate(count,down_animations)
                    move_y+=change_y


            elif event.key==pygame.K_UP:

                # Allow player to walk on main path
                if move_x>-182 and move_x<-60 and move_y<740:
                    count+=1
                    if count>=15:
                        count=0
                    character=move_animate(count,up_animations)
                    move_y+=change_y

                # Prevent player from walking through buildings
                elif move_x<323 and move_x>125:
                    if move_y<260 and move_y>95:
                        count+=1
                    elif move_y>-185 and move_y<-29:
                        count+=1
                    else:
                        if move_y>-275:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,up_animations)
                            move_y+=change_y

                # Prevent player from walking through buildings
                elif move_x<-220 and move_x>-430:
                    if move_y<260 and move_y>95:
                        count+=1
                    elif move_y>-185 and move_y<-29:
                        count+=1
                    else:
                        if move_y>-275:
                            count+=1
                            if count>=15:
                                count=0
                            character=move_animate(count,up_animations)
                            move_y+=change_y

                # Prevent player from walking trees in main area
                elif move_y<300:
                    count+=1
                    if count>=15:
                        count=0
                    character=move_animate(count,up_animations)
                    move_y+=change_y

    # Check to see if the user is in combat
    elif battle:

        # PLay battle music
        if not channel1.get_busy():
            channel1.play(combat_music)

        # Check if the user chose to attack
        if attack!="":

            # Animate the user attack
            if amount==0:
                animating=True
                assailant="friendly"

            # Calculate the user's damage output
            elif amount==1:
                pygame.time.wait(1500)
                if attack_type=="Special":
                    user_dam=int(round(((2*user_poke["Level"]/5.0+2)*attack_dam*user_poke["Sp. Attack"]/(float(enemy_poke["Sp. Defence"]+1)*3.2)/5.0+1)))
                    enemy_poke["Current_HP"]-=user_dam
                elif attack_type=="Physical":
                    user_dam=int(round(((2*user_poke["Level"]/5.0+2)*attack_dam*user_poke["Attack"]/(float(enemy_poke["Defence"]+1)*3.2)/5.0+1)))
                    enemy_poke["Current_HP"]-=user_dam
                elif attack_type=="Stat_Increase":
                    user_poke[attack_stat]+=attack_dam
                elif attack_type=="Stat_Decrease":
                    enemy_poke[attack_stat]-=attack_dam
                    if enemy_poke[attack_stat]<0:
                        enemy_poke[attack_stat]=0

                # Check if the enemy pokemon is dead, if so increase the user score
                if enemy_poke["Current_HP"]<=0:
                    enemy_poke["Current_HP"]=0
                    if not one_time:
                        score+=1
                        gained_xp=random.randint(1,10)+enemy_poke["Level"]
                        gained_gold=random.randint(1,100)
                        gold+=gained_gold
                        user_poke["Experience"]+=gained_xp
                        additional_text=True
                        win_text1=font.render("You have slain the wild pokemon and earned "+str(gained_xp)+" experience points",True,BLACK)
                        win_text2=font.render("and recieved "+str(gained_gold)+" gold.",True,BLACK)
                        add_text=[win_text1,win_text2]

                    # Check to see if the user's pokemon levelled up and increase it's stats
                    if user_poke["Experience"]>=125 and one_time:
                        if not one_time2:
                            pygame.time.wait(3000)
                            one_time2=True
                            user_poke=level_up(user_poke)
                            additional_text=True
                            lvl_text1=font.render("Your "+str(user_poke["Name"])+" has levelled up!",True,BLACK)
                            lvl_text2=font.render("It's stats have increased significantly, press tab to check them out of combat!",True,BLACK)
                            add_text=[lvl_text1,lvl_text2]
                            user_poke["Experience"]=0

                    # Give the user time to read the end of battle text and end the battle
                    if not additional_text:
                        pygame.time.wait(4000)
                        battle=False
                        instructions=""
                        option1=False
                        option2=False
                        option3=False
                        amount=0
                        attack=""
                        stat_reset(user_poke,enemy_poke)
                        combat_music.stop()
                        one_time=False
                        one_time2=False

                # If the enemy pokemon survives, they choose their attack
                else:
                    amount=2
                    selection=random.randint(1,4)
                    if selection==2:
                        selection=3
                    elif selection==3:
                        selection=2

            # Animate the enemy attack
            elif amount==2:
                enemy_attack=enemy_poke["Move"+str(selection)]
                enemy_attack_dam=enemy_poke["Move" +str(selection)+ "_Dam"]
                enemy_type=enemy_poke["Move" +str(selection)+ "_Type"]
                attack_animation_type=enemy_poke["Move" +str(selection)+"_Animation_Type"]
                animation_list=enemy_poke["Move"+str(selection)+"_Animations"]
                attack_sound=enemy_poke["Move"+str(selection)+"_Sound"]
                if enemy_type!="Special" and enemy_type!="Physical":
                    attack_stat=enemy_poke["Move" +str(selection)+ "_Stat"]
                animating=True
                assailant="enemy"

            # Calculate the enemy's damage output
            elif amount==3:
                pygame.time.wait(1500)
                if enemy_type=="Special":
                    enemy_dam=int(round(((2*enemy_poke["Level"]/5.0+2)*enemy_attack_dam*enemy_poke["Sp. Attack"]/(float(user_poke["Sp. Defence"]+1)*3.2)/5.0+1)))
                    user_poke["Current_HP"]-=enemy_dam
                elif enemy_type=="Physical":
                    enemy_dam=int(round(((2*enemy_poke["Level"]/5.0+2)*enemy_attack_dam*enemy_poke["Attack"]/(float(user_poke["Defence"]+1)*3.2)/5.0+1)))
                    user_poke["Current_HP"]-=enemy_dam
                elif enemy_type=="Stat_Increase":
                    enemy_poke[attack_stat]+=enemy_attack_dam
                elif enemy_type=="Stat_Decrease":
                    user_poke[attack_stat]-=enemy_attack_dam
                    if user_poke[attack_stat]<0:
                        user_poke[attack_stat]=0

                # Reset all attack values
                attack=""
                attack_type=""
                attack_dam=0
                attack_stat=""
                amount=0

                # Check to see if the user's pokemon is dead
                if user_poke["Current_HP"]<=0:
                    switch=""

                    # Check to see if there is another living pokemon
                    for i in range(len(all_user_poke)):
                        if all_user_poke[i]!="":
                            if all_user_poke[i]["Current_HP"]>=1:
                                switch=all_user_poke[i]

                    # If there is another living pokemon, switch to it
                    if switch !="":
                        user_poke=switch
                        instructions=battle_words
                        option1=False
                        option2=False
                        option3=False
                        amount=0

                    # If there are no other living pokemon, the user is defeated and brought to the scoreboard
                    else:
                        combat_music.stop()
                        scoreboard=True
                        defeat=True

                # If the user is alive, continue the battle
                else:
                    instructions=battle_words

        # Check to see if the user chose to switch pokemon
        elif choice_poke!= "":

            #Verify the user's choice of pokemon is still alive, otherwise, don't switch to it
            if choice_poke["Current_HP"]>0:
                user_poke=choice_poke

            # Enemy pokemon chooses their attack
            if amount<=1:
                amount=2
                selection=random.randint(1,4)

            # Animate the enemy attack
            elif amount==2:
                enemy_attack=enemy_poke["Move"+str(selection)]
                enemy_attack_dam=enemy_poke["Move" +str(selection)+ "_Dam"]
                enemy_type=enemy_poke["Move" +str(selection)+ "_Type"]
                attack_animation_type=enemy_poke["Move" +str(selection)+"_Animation_Type"]
                animation_list=enemy_poke["Move"+str(selection)+"_Animations"]
                attack_sound=enemy_poke["Move"+str(selection)+"_Sound"]
                if enemy_type!="Special" and enemy_type!="Physical":
                    attack_stat=enemy_poke["Move" +str(selection)+ "_Stat"]
                animating=True
                assailant="enemy"

            # Calculate the enemy's damage output
            elif amount==3:
                pygame.time.wait(1500)
                if enemy_type=="Special":
                    enemy_dam=int(round(((2*enemy_poke["Level"]/5.0+2)*enemy_attack_dam*enemy_poke["Sp. Attack"]/(float(user_poke["Sp. Defence"]+1)*3.2)/5.0+1)))
                    user_poke["Current_HP"]-=enemy_dam
                elif enemy_type=="Physical":
                    enemy_dam=int(round(((2*enemy_poke["Level"]/5.0+2)*enemy_attack_dam*enemy_poke["Attack"]/(float(user_poke["Defence"]+1)*3.2)/5.0+1)))
                    user_poke["Current_HP"]-=enemy_dam
                elif enemy_type=="Stat_Increase":
                    enemy_poke[attack_stat]+=enemy_attack_dam
                elif enemy_type=="Stat_Decrease":
                    user_poke[attack_stat]-=enemy_attack_dam
                    if user_poke[attack_stat]<0:
                        user_poke[attack_stat]=0

                # Check to see if the user's pokemon is dead
                if user_poke["Current_HP"]<=0:
                    switch=""

                    # Check to see if there is another living pokemon
                    for i in range(len(all_user_poke)):
                        if all_user_poke[i]!="":
                            if all_user_poke[i]["Current_HP"]>=1:
                                switch=all_user_poke[i]

                    # If there is another living pokemon, switch to it
                    if switch !="":
                        user_poke=switch
                        instructions=battle_words
                        option1=False
                        option2=False
                        option3=False
                        amount=0

                    # If there are no other living pokemon, the user is defeated and brought to the scoreboard
                    else:
                        combat_music.stop()
                        scoreboard=True
                        defeat=True

                # If the user is alive, continue the battle
                else:
                    instructions=battle_words
                    option1=False
                    option2=False
                    option3=False
                    amount=0

                # Reset pokemon choice values
                choice_poke=""

        # Check to see if the user chose to use an item
        elif choice_item!="":
            if amount==0:

                #If the user choice to use a potion, animate it
                if choice_item=="potion" and potions>0:
                    attack_animation_type="Self"
                    attack_type="Heal"
                    attack_sound=heal_sound
                    animation_list=[potion_item,potion_item,potion_item]
                    animating=True
                    assailant="friendly"

                #If the user choice to use a pokeball, animate it
                elif choice_item=="pokeball" and poke_balls>0:
                    attack_animation_type="Follow"
                    attack_type="Catch"
                    attack_sound=pokeball_sound
                    animation_list=[pokeball_item,pokeball_item,pokeball_item]
                    animating=True
                    assailant="friendly"

                else:
                    amount=1

            elif amount==1:

                # If the user chose a potion, calculate healing and reduce potions by 1
                if choice_item=="potion":
                    if potions>0:
                        potions-=1
                        if user_poke["Current_HP"]+20>user_poke["HP"]:
                            user_poke["Current_HP"]=user_poke["HP"]
                            amount=2
                        else:
                            user_poke["Current_HP"]+=20
                            amount=2
                    else:
                        amount=2

                # If the user chose a pokeball, check to see if they captured the enemy and reduce pokeballs by 1
                elif choice_item=="pokeball":
                    if poke_balls>0:
                        chance=random.randint(1,enemy_poke["HP"])
                        poke_balls-=1
                        capture=False

                        # Before capture, ensure that they do not have more than the max pokemon (4)
                        for i in range (len(all_user_poke)):
                            if all_user_poke[i]=="":

                                # If a random selected number (max is enemy max hp) is higher than the enemy's current HP, capture is sccessful
                                if chance >= enemy_poke["Current_HP"] and not capture:
                                    all_user_poke[i]=dict(enemy_poke)
                                    user_poke_name[i]=all_user_poke[i]["Name"]
                                    pygame.time.wait(2000)
                                    battle=False
                                    option1=False
                                    option2=False
                                    option3=False
                                    instructions=""
                                    capture=True
                                    amount=0
                                    choice_item=""
                                    combat_music.stop()
                                    stat_reset(user_poke,enemy_poke)

                                # If capture fails continue battle
                                else:
                                    amount=2

                            # If user has max pokemon, continue battle
                            else:
                                amount=2
                    else:
                        amount=2

                # Select enemy attack
                selection=random.randint(1,4)

            # Animate the enemy attack
            elif amount==2:
                enemy_attack=enemy_poke["Move"+str(selection)]
                enemy_attack_dam=enemy_poke["Move" +str(selection)+ "_Dam"]
                enemy_type=enemy_poke["Move" +str(selection)+ "_Type"]
                attack_animation_type=enemy_poke["Move" +str(selection)+"_Animation_Type"]
                animation_list=enemy_poke["Move"+str(selection)+"_Animations"]
                attack_sound=enemy_poke["Move"+str(selection)+"_Sound"]
                if enemy_type!="Special" and enemy_type!="Physical":
                    attack_stat=enemy_poke["Move" +str(selection)+ "_Stat"]
                animating=True
                assailant="enemy"

            # Calculate the enemy's damage output
            elif amount==3:
                pygame.time.wait(1500)
                if enemy_type=="Special":
                    enemy_dam=int(round(((2*enemy_poke["Level"]/5.0+2)*enemy_attack_dam*enemy_poke["Sp. Attack"]/(float(user_poke["Sp. Defence"]+1)*3.2)/5.0+1)))
                    user_poke["Current_HP"]-=enemy_dam
                elif enemy_type=="Physical":
                    enemy_dam=int(round(((2*enemy_poke["Level"]/5.0+2)*enemy_attack_dam*enemy_poke["Attack"]/(float(user_poke["Defence"]+1)*3.2)/5.0+1)))
                    user_poke["Current_HP"]-=enemy_dam
                elif enemy_type=="Stat_Increase":
                    enemy_poke[attack_stat]+=enemy_attack_dam
                elif enemy_type=="Stat_Decrease":
                    user_poke[attack_stat]-=enemy_attack_dam
                    if user_poke[attack_stat]<0:
                        user_poke[attack_stat]=0

                 # Check to see if the user's pokemon is dead
                if user_poke["Current_HP"]<=0:
                    switch=""

                    # Check to see if there is another living pokemon
                    for i in range(len(all_user_poke)):
                        if all_user_poke[i]!="":
                            if all_user_poke[i]["Current_HP"]>=1:
                                switch=all_user_poke[i]

                    # If there is another living pokemon, switch to it
                    if switch !="":
                        user_poke=switch
                        instructions=battle_words
                        option1=False
                        option2=False
                        option3=False
                        amount=0

                    # If there are no other living pokemon, the user is defeated and brought to the scoreboard
                    else:
                        combat_music.stop()
                        scoreboard=True
                        defeat=True

                # If the user is alive, continue the battle
                else:
                    amount=0
                    instructions=battle_words
                    attack_animation_type=""
                    attack_type=""
                    attack_sound=""
                    animation_list=[]
                    assailant=""

                # Reset chosen item values
                choice_item=""




    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    #Check to see if user is on the intro screen
    if intro:

        # Display the background
        screen.blit(poke_back,[0,0])
        screen.blit(intro_title,[0,0])
        for i in range(4):

            # Display the buttons and change colour when moused over
            if i!=colour_active:
                rect(WHITE,[425,200+i*125,200,80],0)
            else:
                rect(RED,[425,200+i*125,200,80],0)
            if i>=1 and i<=2:
                screen.blit(buttons[i],[460,230+i*125])
            else:
                screen.blit(buttons[i],[500,230+i*125])

    # Check to see if the user is on the naming screen
    elif name_screen:
        screen.fill(SALMON)

        # Display the user's typed name with instructions and a text box
        printing_name=font.render(user_name,True,BLACK)
        rect(BLACK,[5,5,1040,200],10)
        rect(BEIGE,[5,5,1040,200],0)
        screen.blit(printing_name,[500,150])
        screen.blit(inform_name,[315,50])

        # Display some game images to fill screen
        screen.blit(still_down,[80,80])
        screen.blit(still_up,[910,80])
        screen.blit(charmander["enemy_sprite"],[125,425])
        screen.blit(bulbasaur["enemy_sprite"],[425,425])
        screen.blit(squirtle["enemy_sprite"],[725,425])

        # Display some key instructions in a textbox
        rect(BLACK,[5,590,1040,150],10)
        rect(WHITE,[5,590,1040,150],0)
        screen.blit(back,[50,650])
        screen.blit(cont,[660,650])
        screen.blit(backspace_key,[190,610])
        screen.blit(enter_key,[800,600])

        # If the user is attempting to make a name with more than five letters, display an error message
        if bad_name:
            rect(BLACK,[5,300,1040,100],10)
            rect(BEIGE,[5,300,1040,100],0)
            screen.blit(bad_name_text,[283,340])

    # Verify the user is on the tutorial screen
    elif tutorial:
        screen.fill(WHITE)

        # Display changing instructions on text box
        textBox(tutorial_read)

        # Display additional images
        screen.blit(professor,[450,100])
        screen.blit(professor_poke,[300,300])

    # Verify the user is on the scoreboard screen
    elif scoreboard:
        if single==1:

            # Dislay the screen title and background
            screen.blit(score_back,[0,0])
            screen.blit(score_text,[50,0])

            # Display high scores
            for i in range(10):
                wording=new_score_list[i]
                play_score=font.render(wording,True,BLACK)
                screen.blit(play_score,[300,140+i*50])

        # Display button that allows user to return to main menu
        rect(WHITE,[250,655,200,60],0)
        if pos_x>=250 and pos_x<=450 and pos_y>=655 and pos_y<=715:
            rect(GREEN,[250,655,200,60],0)
        else:
            rect(WHITE,[250,655,200,60],0)
        screen.blit(return_choice,[325,675])

    # Verify the user is in combat
    elif battle:

        #Get the position of themouse
        pos = pygame.mouse.get_pos()
        pos_x=pos[0]
        pos_y=pos[1]

        screen.fill(FLOOR)

        # When no animations occur, display battle instructions
        if not animating:
            textBox(instructions)

        #Display battle zones
        ellipse(TREE_BACK1,[50,340,300,125],0)
        ellipse(TREE_BACK1,[700,100,300,125],0)

        # Display user pokemon
        screen.blit(user_poke["friendly_sprite"],[100,250])

        # Display user pokemon info bar (includes HP and EXP)
        rect(WHITE,[750,320,300,150],0)
        rect(BLACK,[750,320,300,150],3)
        good_bar=font.render(user_poke["Name"]+" "*5+"Level: "+str(user_poke["Level"]),True,BLACK)
        screen.blit(good_bar,[775,335])
        rect(WHITE,[800,380,210,20],0)
        rect(GREEN,[800,380,float(user_poke["Current_HP"])/user_poke["HP"]*210,20],0)
        rect(BLACK,[800,380,210,20],3)
        user_health=font.render("HP: "+ str(user_poke["Current_HP"]) + " / " + str(user_poke["HP"]),True,BLACK)
        screen.blit(user_health,[895,410])
        user_xp=font.render("Exp:",True,BLACK)
        screen.blit(user_xp,[730,467])
        rect(WHITE,[780,470,270,15],0)
        rect(EXP_BLUE,[780,470,float(user_poke["Experience"])/125*270,15],0)
        rect(BLACK,[780,470,270,15],3)

        # Display enemy pokemon
        screen.blit(enemy_poke["enemy_sprite"],[760,35])

        # Displa enemy pokemon's info bar (includes HP)
        rect(WHITE,[0,30,300,150],0)
        rect(BLACK,[0,30,300,150],3)
        bad_bar=font.render(enemy_poke["Name"]+" "*5+"Level: "+str(enemy_poke["Level"]),True,BLACK)
        screen.blit(bad_bar,[25,46])
        rect(WHITE,[50,90,210,20],0)
        rect(GREEN,[50,90,float(enemy_poke["Current_HP"])/enemy_poke["HP"]*210,20],0)
        rect(BLACK,[50,90,210,20],3)
        enemy_health=font.render("HP: "+ str(enemy_poke["Current_HP"]) + " / " + str(enemy_poke["HP"]),True,BLACK)
        screen.blit(enemy_health,[145,120])

        # Check if additional text needs to be displayed, if so, display
        if additional_text:
            textBox(add_text)
            additional_text=False
            add_text=""
            one_time=True

            # If the user pokemon levels up, play the animation and sound
            if user_poke["Experience"]>=125:
                screen.blit(level_up_img,[115,275])
                channel3.play(level_sound)

        # Verify no animations are occurring
        elif not animating:

            # If the user is in combat, put a box around any option they mouse over
            if not fled:
                if instructions!=battle_words:
                    screen.blit(return_choice,[490,695])
                    if pos_x>=350 and pos_x <= 570 and pos_y>=690 and pos_y<=720:
                        rect(BLACK,[350,690,320,30],3)
                if pos_x>=27 and pos_x <= 524 and pos_y>=590 and pos_y<=637:
                    rect(BLACK,[27,590,497,47],3)
                elif pos_x>=525 and pos_x <= 1025 and pos_y>=590 and pos_y<=637:
                    rect(BLACK,[525,590,498,47],3)
                elif pos_x>=525 and pos_x <= 1025 and pos_y>=638 and pos_y<=685:
                    rect(BLACK,[525,638,498,47],3)
                elif pos_x>=27 and pos_x <= 524 and pos_y>=638 and pos_y<=685:
                    rect(BLACK,[27,638,498,47],3)

        # Verify animations are occurring
        else:

            # Check which pokemon is attacking and check the type of attack, also displaying a statement regarding it
            if assailant=="friendly":
                if attack_type=="Heal":
                    additional_info=str(user_poke["Name"])+" was healed."
                elif attack_type=="Catch":
                    additional_info="You try to catch the enemy "+str(enemy_poke["Name"])
                elif attack_type=="Stat_Increase":
                    additional_info=str(user_poke["Name"])+" \'s "+str(attack_stat.lower())+" increased!"
                elif attack_type=="Stat_Decrease":
                    additional_info="Enemy "+str(enemy_poke["Name"])+" \'s "+str(attack_stat.lower())+" decreased!"
                else:
                    additional_info="Enemy "+str(enemy_poke["Name"])+" took damage."
                if attack_type!="Heal" and attack_type!="Catch":
                    instructions=font.render(str(user_poke["Name"]) + " used " +str(attack) +"! " + additional_info,True,BLACK)
                else:
                    instructions=font.render(additional_info,True,BLACK)
            else:
                if enemy_type=="Stat_Increase":
                    additional_info="Enemy "+str(enemy_poke["Name"])+" \'s "+str(attack_stat.lower())+" increased!"
                elif enemy_type=="Stat_Decrease":
                    additional_info=str(user_poke["Name"])+" \'s "+str(attack_stat.lower())+" decreased!"
                else:
                    additional_info=str(user_poke["Name"])+" took damage."
                instructions=font.render("Enemy "+str(enemy_poke["Name"]) + " used " +str(enemy_attack) +"! " + additional_info,True,BLACK)
            textBox_Sing(instructions)

            #Determine if the attack is a moving attack and follow to it's target while swapping images
            if attack_animation_type=="Follow":
                counter+=4
                if counter<550:
                    if counter==4:
                        channel3.play(attack_sound,-1)
                    elif counter>=540:
                        channel3.stop()
                    if counter%60==0 or counter==4:
                        animation=animation_list[2]
                    elif counter%60==20:
                        animation=animation_list[1]
                    elif counter%60==40:
                        animation=animation_list[0]

                    # Determine the start and end point based on the attacker
                    if assailant=="friendly":
                        screen.blit(animation,[205+counter,305-counter*0.5])
                    elif assailant=="enemy":
                        screen.blit(animation,[755-counter,45+counter*0.5])

                # Reset variables once the animation is complete
                else:
                    counter=0
                    animating=False
                    if amount==0:
                        amount=1
                    elif amount==2:
                        amount=3

                    instructions=[blank,blank]

            # Determine that the attack is stationary and swap images to animate it
            elif attack_animation_type=="Self" or attack_animation_type=="Front" or attack_animation_type=="Enemy":
                counter+=1
                if counter<150:
                    if counter==1:
                        channel3.play(attack_sound,-1)
                    elif counter>=148:
                        channel3.stop()
                    if counter%30==0 or counter==1:
                        animation=animation_list[0]
                    elif counter%30==10:
                        animation=animation_list[1]
                    elif counter%30==20:
                        animation=animation_list[2]

                    # Determine the start and end point based on the attacker and target
                    if assailant=="friendly":
                        if attack_animation_type=="Self":
                            screen.blit(animation,[115,275])
                        elif attack_animation_type=="Enemy":
                            screen.blit(animation,[765,50])
                        else:
                            screen.blit(animation,[210,275])
                    elif assailant=="enemy":
                        if attack_animation_type=="Self":
                            screen.blit(animation,[765,50])
                        elif attack_animation_type=="Enemy":
                            screen.blit(animation,[115,275])
                        else:
                            screen.blit(animation,[750,50])

                # Reset variables once the animation is complete
                else:
                    counter=0
                    animating=False
                    if amount==0:
                        amount=1
                    elif amount==2:
                        amount=3

                    instructions=[blank,blank]

    # Verify the user is in the over world
    elif not battle:
        screen.fill(FLOOR)

        # --- Drawing code should go here

        # Draw in the trees
        addTree(move_x,move_y)

        # Draw in the buildings
        screen.blit(poke_heal,[move_x+170,move_y+140])
        screen.blit(poke_buy,[move_x+720,move_y+140])
        for i in range(2):
            screen.blit(poke_house,[move_x+165+550*i,move_y+430])

        # Draw in the tall grass
        addGrass(move_x+520,move_y-320)

        # Draw in the player's character
        screen.blit(character,[447,325])

        # If instructions are visible, box the one the user mouses over
        if visible:
            textBox_Sing(instructions)
            if pos_x>=490 and pos_x <= 620 and pos_y>=630 and pos_y<=677:
                rect(BLACK,[490,630,130,47],3)
            elif pos_x>=635 and pos_x <= 765 and pos_y>=630 and pos_y<=677:
                rect(BLACK,[635,630,130,47],3)
            if instructions==instruction_1:
                screen.blit(return_choice,[490,695])
                if pos_x>=462 and pos_x <= 572 and pos_y>=695 and pos_y<=720:
                    rect(BLACK,[462,695,110,25],3)

        # Display all pokemon stats of user
        if stat_screen:
            stat_check(all_user_poke)

        # Verify the user is in tall grass
        if move_x>-177 and move_x<-72 and move_y>381 and move_y<690 and (original_x!=move_x or original_y!=move_y):

            # Whever the user moves, theyhave a 1% chance to intitate a battle
            change=random.randint(1,100)
            if change==2:

                # Choose a random enemy and for every ten points the user has, increase the level of the enemy pokemon
                if score>=10*(enemy_list[0]["Level"]-4):
                    for i in range (len(enemy_list)):
                        enemy_list[i]=level_up(enemy_list[i])
                overworld_music.stop()
                enemy_num=random.randint(0,2)
                enemy_poke=enemy_list[enemy_num]
                battle=True
                instructions=battle_words

        # Check for movement to only allow battle on movement
        original_x=move_x
        original_y=move_y

        # Constantly display score and gold in upper left corner
        rect(WHITE,[0,0,150,56],0)
        game_score=font.render("Score: "+str(score),True,BLACK)
        screen.blit(game_score,[5,5])
        game_gold=font.render("Gold: "+str(gold),True,BLACK)
        screen.blit(game_gold,[5,30])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
