import datetime
import json
import hashlib
from flask import Flask, jsonify

class Blockchain:
	def __init__(self):
		self.chain = []
		self.create_blockchain(proof=1, previous_hash='0')
