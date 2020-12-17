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

        # Metodo retorna bloco anterior
        def get_previous_block(self):
            return self.chain[-1]
        
        # Metodo proof of work
        def proof_of_work(self, previous_proof):
            new_proof = 1
            check_proof = False
            while check_proof is False:
                hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
                if hash_operation[:4] == '0000':
                    check_proof = True
                else:
                    new_proof += 1
            return new_proof        
            