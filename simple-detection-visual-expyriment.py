#! /usr/bin/env python
# Time-stamp: <2021-11-16 15:36:47 christophe@pallier.org>
""" 
SIMPLE REACTION TIMES OF IPSILATERAL AND CONTRALATERAL HAND TO LATERALIZED VISUAL STIMUL

"""


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

"""""""""""""""""""""""----------------------"""""""""""""""""""""""


import random
# from expyriment import design, control, stimuli

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

angle = (5, 20, 35)
target_side = ('R', 'L')
response_side_sequence = ((('R', 'L', 'L', 'R'), ('R', 'L', 'L', 'R')), 
                          (('L', 'R', 'R', 'L'), ('L', 'R', 'R', 'L')))
for a in angle: 
    for rs in response_side_sequence[0]:
        for s in target_side: 
        
            print(a, s, rs)





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


# #Target: square patch of light one square degree in area

# # Draw a rectangle at the center of the screen (in the backbuffer)
# width, height = 100, 100  # dimensions of the rectangle in pixels
# left_x = center_x - width // 2  # x coordinate of topleft corner
# top_y = center_y - height // 2  # y coordinate of topleft corner
# pygame.draw.rect(screen, BLUE, (left_x, top_y, width, height))

# pygame.display.flip()  # display the backbuffer on the screen




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
