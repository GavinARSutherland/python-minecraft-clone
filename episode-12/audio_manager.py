#!/usr/bin/env python3
#Gavin Sutherland
#May 3, 2022 [2022/05/03]
#Audio manager
#audio_manager.py

'''Manages and plays the audio files for minecraft'''

import os
import pyglet

class Audio_Manager(object):
    def __init__(self):

        self.music = {}
        self.sfx = {}

        for music_file in os.listdir('audio/music'):
            self.music[str(music_file)] = f"audio/music/{music_file}"

        for sfx_file in os.listdir('audio/sfx'):
            self.sfx[str(sfx_file)] = f"audio/sfx/{sfx_file}"

    def play_sound(self, sound):
        sfx = sound
        if sfx[-4:-1] != '.ogg':
            sfx += '.ogg'
        
        pyglet.media.load(self.sfx[sfx]).play()
