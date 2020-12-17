# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:53:11 2020

@author: Ramon
"""

import datetime
import hashlib
import json
from flask import flask, jsonify

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        