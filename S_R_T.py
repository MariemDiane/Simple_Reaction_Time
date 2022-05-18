#! /usr/bin/env python

""" 
SIMPLE REACTION TIMES OF IPSILATERAL AND CONTRALATERAL HAND TO LATERALIZED VISUAL STIMULI, simplified version

"""


import expyriment
from expyriment import design, control, stimuli
from random import randint

exp = expyriment.design.Experiment(name="S_R_T") 
expyriment.control.initialize(exp)

fixcross = stimuli.FixCross()
fixcross.preload()


# Block right hand (RH):
block_RH = expyriment.design.Block(name="Block Right Hand")
instructions_RH = expyriment.stimuli.TextScreen("Instructions", text="""Lorsque vous voyez le carré apparaître, répondez AVEC VOTRE MAIN DROITE en appuyant sur la touche Espace.
                                                    Appuyez sur n'importe quelle touche quand vous êtes prêt.e à commencer.""")
trial_left = expyriment.design.Trial()
trial_left.set_factor("display_side", "left")
stim_left = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), position=(-200, 0)) # Position left à determiner 
stim_left.preload()
trial_left.add_stimulus(stim_left)
trial_right = expyriment.design.Trial()
trial_right.set_factor("display_side", "right")
stim_right = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), position=(200, 0)) # Position right à determiner 
stim_right.preload()
trial_right.add_stimulus(stim_right)
block_RH.add_trial(trial_right, copies=10)
block_RH.add_trial(trial_left, copies=10)


# Block left hand (LH):
block_LH = expyriment.design.Block(name="Block Left Hand")
instructions_LH = expyriment.stimuli.TextScreen("Instructions", text="""Lorsque vous voyez le carré apparaître, répondez AVEC VOTRE MAIN GAUCHE en appuyant sur la touche Espace. 
                                                    Appuyez sur n'importe quelle touche quand vous êtes prêt.e à commencer.""")
trial_left = expyriment.design.Trial()
trial_left.set_factor("display_side", "left")
stim_left = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), position=(-200, 0)) # Position left à determiner 
stim_left.preload()
trial_left.add_stimulus(stim_left)
trial_right = expyriment.design.Trial()
trial_right.set_factor("display_side", "right")
stim_right = expyriment.stimuli.Rectangle((50, 50), (255, 255, 255), position=(200, 0))
stim_right.preload()
trial_right.add_stimulus(stim_right)
block_LH.add_trial(trial_right, copies=10)
block_LH.add_trial(trial_left, copies=10)
exp.add_block(block_LH)


exp.data_variable_names = ["Block", "Trial", "Key", "RT"]


expyriment.control.start() 

if exp.subject % 2 == 0: 
    exp.add_block(block_RH)
    exp.add_block(block_LH)
    instructions = [instructions_RH, instructions_LH]
    blocks = [block_RH, block_LH]
else: 
    exp.add_block(block_LH)
    exp.add_block(block_RH)
    instructions = [instructions_LH, instructions_RH]

blocks = [block_RH, block_LH]
for iblock in [0, 1]:
    block = blocks[iblock]
    block.shuffle_trials()
    is_right_hand = (block.name == "Block Right Hand")


    instructions[iblock].present()
    exp.keyboard.wait()
    for trial in blocks[iblock].trials:
        fixcross.present()
        exp.clock.wait(randint(1000,2000) - trial.stimuli[0].preload())
        trial.stimuli[0].present()

        key, rt = exp.keyboard.wait()
        display_side = trial.get_factor("display_side")
        exp.data.add([block.name, display_side, rt])


expyriment.control.end()

