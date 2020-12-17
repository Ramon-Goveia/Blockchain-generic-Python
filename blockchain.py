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

    # Criar novo block e iserir na cadeia
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block        