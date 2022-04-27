#! /usr/bin/env python

""" 
SIMPLE REACTION TIMES OF IPSILATERAL AND CONTRALATERAL HAND TO LATERALIZED VISUAL STIMUL

"""
#import random

# TARGET STIMULUS = Square, presented for 32ms

# Facteurs: Side of target (Nasal or Temporal), (Angle from fixation cross (5°, 20°, 35°)), Hand used (Left or Right)


# Total number of trials for each sesson = 360, 60 trials with each of the six retinal points tested; Half of these trials were with the right hand, half with the left hand.

# Delays: 
#Ancipatory (anything less than is discarded): 5° = 180ms / 20° = 190ms / 35° = 200ms
#Limits of delay (anything more than is discarded): 5° = 320ms / 20° = 350ms / 35° = 380ms
# On garde les delais de 35°? 
# Temps entre les essais: variation entre 1 et 2 sc


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

# # Colors are triplets containint RGB values
# # (see <https://www.rapidtables.com/web/color/RGB_Color.html>
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (127, 127, 127)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)


# Version expyriment 

import expyriment
from expyriment import design, control, stimuli

exp = expyriment.design.Experiment(name="S_R_T") 
expyriment.control.initialize(exp)

instructions_RH = expyriment.stimuli.TextLine(text="Lorsque vous voyez le carré apparaître, répondez AVEC VOTRE MAIN DROITE en appuyant sur la touche M. Appuyez sur n'importe quelle touche quand vous êtes prêt.e à commencer.")
instructions_LH = expyriment.stimuli.TextLine(text="Lorsque vous voyez le carré apparaître, répondez AVEC VOTRE MAIN GAUCHE en appuyant sur la touche Q. Appuyez sur n'importe quelle touche quand vous êtes prêt.e à commencer.")

stim_left = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), position=(10, 10)) # Position left à determiner 
stim_right = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), position=(100, 100)) # Position right à determiner 

#expyriment.control.start() # Not sure where to put this exactly


exp.data_variable_names = ["Block", "Trial", "Key", "RT"]
# Randomiser ordre passage Block 1 et Block 2 en fonction numéro pair ou impair participant

# Block main droite:
block_RH = expyriment.design.Block(name="Block Right Hand")
# Changer la key de réponse
instructions_RH.present()
exp.keyboard.wait()
## Apparition random trial one ou trial two
trial_left = expyriment.design.Trial()
stim_left.preload()
trial_left.add_stimulus(stim_left)


trial_right = expyriment.design.Trial()
stim_right.preload()
trial_right.add_stimulus(stim_right)

block_RH.add_trial(trial_right)
block_RH.add_trial(trial_left)
exp.add_block(block_RH)

# Block main gauche:
block_LH = expyriment.design.Block(name="Block Left Hand")
# Changer la key de réponse
instructions_LH.present()
exp.keyboard.wait()
# Apparition random trial one ou trial two
trial_left = expyriment.design.Trial()
stim_left.preload()
trial_left.add_stimulus(stim_left)

trial_right = expyriment.design.Trial()
stim_right.preload()
trial_right.add_stimulus(stim_right)

block_LH.add_trial(trial_right)
block_LH.add_trial(trial_left)
exp.add_block(block_RH)


for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([expyriment.misc.constants.K_q,
                                     expyriment.misc.constants.K_m])
        exp.data.add([block.name, trial.id, key, rt])


expyriment.control.end()

#Block left + instructions left
#Block right + instructions right

# if numero du sujet pair, afficher instructions droite, et block 1 ; if numero sujet impair, afficher instruction gauche 

# Block 1: boucle 30 essais droit, boucle 30 essais gauche
# Block 2: boucle 30 essais droit, boucle 30 essais gauche




# Définir un certain temps pendant lequel j'attends une réponse du sujet, et au delà duquel la réponse du sujet n'est pas enregistrée


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
