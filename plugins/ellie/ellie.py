import random
import time

import eliza

crontable = []
outputs = []

def process_message(data):
	# Sleep for a bit before replying; you'll seem more real this way
	time.sleep(random.randint(0,9) *.2)
	outputs.append([data['channel'], "{}".format(eliza.respond(data['text'])) ])