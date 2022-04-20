#! /usr/bin/env python

""" 
SIMPLE REACTION TIMES OF IPSILATERAL AND CONTRALATERAL HAND TO LATERALIZED VISUAL STIMUL

"""
#import random

# TARGET STIMULUS = Square, presented for 32ms

# 3 sessions
# Within each session, 3 parts; 1 angle per part 
# Randomisation: "Whether the stimulus would appear in the right or left field and whether the right or left hand would be used first, was decided on a random basis for each part of the session.""

# Within each part, 2 subparts (One where stimulus appears on one side, and the other where the stimulus appears on the other side; same visual angle)
# Within each subpart, 4 blocks: 1st and 4th with one hand, 2cnd and 3rd with the other hand
# Within each block, 15 trials

# Facteurs: Side of target (Nasal or Temporal), Angle from fixation cross (5°, 20°, 35°), Hand used (Left or Right)

# Utiliser block de expyriment et add trials

# Total number of trials for each sesson = 360, 60 trials with each of the six retinal points tested; Half of these trials were with the right hand, half with the left hand.


# Delays: 
#Ancipatory (anything less than is discarded): 5° = 180ms / 20° = 190ms / 35° = 200ms
#Limits of delay (anything more than is discarded): 5° = 320ms / 20° = 350ms / 35° = 380ms
# To be determined by Part: On which side the stimulus will appear first, which hand is used first (both randomized)
# To be determined by Block: Side, Angle, Delays (anticipatory and limit), 

#Coordinates for left, 5 degrees:
#We consider a square triangle A, B, C. A = Participant, B = target, C = fixation cross. 
#We consider that the participant is 40 cm away from the screen, and thus (AB)=40cm, (AC)= 40cm. 
#We want the angle of B to be equal to 5°.
# Therefore, we use trigonometry: sin 5° = BC/40
# 40*sin 5° = 40*sin(0.087 --> angle in radians) = 40*0.0872 = 3.488cm.
#Pixel to cm conversion? 
#Here, our target has to be 3.488cm to the left of the fixation cross.

"""""""""""""""""""""""----------------------"""""""""""""""""""""""


# I. Afficher carré

#Version pygame

# import pygame

# # Colors are triplets containint RGB values
# # (see <https://www.rapidtables.com/web/color/RGB_Color.html>
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (127, 127, 127)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# #  create the window
# W, H = 1000, 1000  # Size of the graphic window
# # Note that (0,0) is at the *upper* left hand corner of the screen.
# center_x = W // 2
# center_y = H // 2

# pygame.init()
# screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
# pygame.display.set_caption('square')

# screen.fill(GRAY)  # fill it with white

# # # Draw a rectangle at the center of the screen (in the backbuffer)
# width, height = 100, 100  # dimensions of the rectangle in pixels
# left_x = center_x - width // 2  # x coordinate of topleft corner
# top_y = center_y - height // 2  # y coordinate of topleft corner

# pygame.draw.rect(screen, WHITE, (left_x, top_y, width, height))

# pygame.display.flip()  # display the backbuffer on the screen


# # Wait until the window is closed
# quit_button_pressed = False
# while not quit_button_pressed:
#     pygame.time.wait(10)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit_button_pressed = True

# pygame.quit()


# Version expyriment 

import expyriment
from expyriment import design, control, stimuli


exp = expyriment.design.Experiment(name="S_R_T") expyriment.control.initialize(exp)

expyriment.control.start(exp)

expyriment.control.end()

stim = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), line_width=None, corner_rounding=None, corner_anti_aliasing=None, position=None) stim.preload()

stim.present()

expyriment.control.start(exp)

expyriment.control.end()



# Faire plusieurs (10) trials avec TR enregistrés; définir un certain temps pendant lequel j'attends une réponse du sujet, et au delà duquel la réponse du sujet n'est pas enregistrée


# S'affichent à droit et à gauche 


# Réponse congruente et incongruente







#Square design


# #Target: square patch of light one square degree in area

# # Draw a rectangle at the center of the screen (in the backbuffer)
# width, height = 100, 100  # dimensions of the rectangle in pixels

#Coordinates for left, 5 degrees:
#We consider a square triangle A, B, C. A = Participant, B = target, C = fixation cross. 
#We consider that the participant is 40 cm away from the screen, and thus (AB)=40cm, (AC)= 40cm. 
#We want the angle of B to be equal to 5°.
# Therefore, we use trigonometry: sin 5° = BC/40
# 40*sin 5° = 40*sin(0.087 --> angle in radians) = 40*0.0872 = 3.488cm.
#Pixel to cm conversion? 
#Here, our target has to be 3.488cm to the left of the fixation cross. 


# left_x = center_x - width // 2  # x coordinate of topleft corner
# top_y = center_y - height // 2  # y coordinate of topleft corner

#pygame.draw.rect(screen, WHITE, (left_x, top_y, width, height))

# pygame.display.flip()  # display the backbuffer on the screen

# Comment obtenir hauteur de l'écran? 
#Afficher le rectangle à gauche et à droite
# Ensuite, afficher plus ou moins éloigné 








### Order of the following parts is randomized ###

# Part 1: 5° angle
#First block: 4*15 trials on Side A
# Answer: 1rst and 4rth trial parts: Hand A / 2nd and 3rd trial parts: Hand B; afficher à l'écran quelle main doit être utilisée
# Delays: Ancipatory (anything less than is discarded): 5° = 180ms / Limits of delay (anything more than is discarded): 5° = 320ms 

#Second block: 4*15 trials on Side B
# Answer: 1rst and 4rth trial parts: Hand B / 2nd and 3rd trial parts: Hand A
# Delays: Ancipatory (anything less than is discarded): 5° = 180ms / Limits of delay (anything more than is discarded): 5° = 320ms 



# Part 2: 20° angle




# Part 3: 35° angle 

# angle = (5, 20, 35)
# target_side = ('R', 'L')
# response_side_sequence = ((('R', 'L', 'L', 'R'), ('R', 'L', 'L', 'R')), 
#                           (('L', 'R', 'R', 'L'), ('L', 'R', 'R', 'L')))
# for a in angle: 
#     for rs in response_side_sequence[0]:
#         for s in target_side: 
        
#             print(a, s, rs)





# N_TRIALS = 50 
# MIN_WAIT_TIME = 1000
# MAX_WAIT_TIME = 2000
# MAX_RESPONSE_DELAY = 2000

# exp = design.Experiment(name="Visual Detection", text_size=40)
# control.set_develop_mode(on=True)
# control.initialize(exp)

# target = stimuli.FixCross(size=(50, 50), line_width=4)
# blankscreen = stimuli.BlankScreen()
# instructions = stimuli.TextScreen("Instructions",
#     f"""From time to time, a cross will appear at the center of screen.

#     Your task is to press a key as quickly as possible when you see it (We measure your reaction-time).

#     There will be {N_TRIALS} trials in total.

#     Press the space bar to start.""")







# exp.add_data_variable_names(['trial', 'wait', 'respkey', 'RT'])

# control.start(skip_ready_screen=True)
# #instructions.present()
# #exp.keyboard.wait()

# for i_trial in range(N_TRIALS):
#     blankscreen.present()
#     waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
#     exp.clock.wait(waiting_time)
#     target.present()
#     key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
#     exp.data.add([i_trial, waiting_time, key, rt])

# control.end()
