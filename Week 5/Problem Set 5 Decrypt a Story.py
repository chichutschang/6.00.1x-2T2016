# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:20:39 2016

@author: chi-chu tschang
"""

def decrypt_story():
    
    story = get_story_string()
        
    return CiphertextMessage(story).decrypt_message()

print(decrypt_story())