######### START screen1 #########
def func(x):
	x = x + 1
	return (x)

print (func(10))

# counting to ten and printing out the result for each loop
def count():
	for c in range(0,11):
		print (c)
count()

######### END screen1 #########

def ceasar(inp,s):
	res = ""
	for i in range(len(inp)):
		c = inp[i]
		if (c.islower()):
			 res += chr((ord(c) + s - 97) % 26 + 97)
		else:
			 res += chr((ord(c) + s-65) % 26 + 65)
	return res

result = ceasar('ABCDE', 2) #printing ciphered string with ceasar

def gen_key_vigenere(string, key):
		key = list(key)
		if len(string) == len(key):
				return key
		else:
				for i in range(len(string) -len(key)):
						key.append(key[i % len(key)])
		return "".join(key)
		 
def vigenere(string, key):
		result = []
		for i in range(len(string)):
				x = (ord(string[i]) + ord(key[i])) % 26
				x += 0x41
				result.append(chr(x))
		return "".join(result)

string = "MYSTRING"
keyword = "keywd"
key = gen_key_vigenere(string, keyword)
result = vigenere(string,key)
print(result) #printing ciphered string with vigenere


######### END screen2 #########



def hash(plaintext):
		res = 0
		for i in range(len(plaintext)):
			res += ord(plaintext[i])
		return (res)

result= hash("ABCDEF")
print ("hash of ABDCDEF is ",result) # printing hash result

######### END screen3 #########

def hash2(plaintext):
		res = 0
		for i in range(len(plaintext)):
			res += (ord(plaintext[i]) * (i+1))
		return (res)

result= hash("ABCDEF")
print ("hash of ABDCDEF is ",result) # printing hash2 result

######### END screen4 #########


import string
def rollover(integ, base):
	base_len = len(base)
	while integ > base_len:
		integ = integ - base_len
	return integ


def charToNum(st, alpha):
	st = st.upper()
	res = []
	for c in st:
		if c in alpha:
			res.append(alpha.index(c) + 1)
	return res


def numbers_to_characters(numbersList, alpha):
	st = ''
	for i in numbersList:
		c = alpha[i - 1]
		st = st + c
	return st


def chomp(st, max_len, alpha):
	while len(st) < max_len:
		st = st + alpha
		st = st + alpha
	st = charToNum(st, alpha)
	cut_st = st[max_len:]
	new_st = st[:max_len]
	index = 0
	while True:
		if (index > max_len - 1) or (index > len(cut_st) - 1):
			cut_st = cut_st[index:]
			index = 0
			if len(cut_st) < 1:
				break
		new_st[index] = rollover(new_st[index] + cut_st[index], alpha)
		index += 1
	return numbers_to_characters(new_st, alpha)


def character_map(a, b, index):
	x = pow(a,2) + b + index * 2 
	return x


def cipher(st, alpha):
	num_string = charToNum(st, alpha)
	index = 0
	mapped = character_map(num_string[0], num_string[-1], index)
	num_string[0] = rollover(mapped, alpha)
	for i in num_string[1:]:
		prev_chaar = num_string[index]
		i = character_map(i, prev_chaar, index)
		i = rollover(i, alpha)
		index += 1
		num_string[index] = i
		mapped = character_map(num_string[0], num_string[-1], index)
	first_character = rollover(mapped, alpha)
	num_string[0] = first_character
	return numbers_to_characters(num_string, alpha)


def hash3(message):
	alpha = string.ascii_uppercase+string.digits
	message = chomp(message, 21, alpha)
	hash_count = 0
	digest = cipher(message, alpha)
	while hash_count < 10:
		digest = cipher(digest, alpha)
		hash_count += 1
	return digest

result = hash3("ABCDEFG")
print (result) # printing hash3 result


######### END screen5 #########


from datetime import datetime

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
			self.index = index
			self.timestamp = timestamp
			self.data = data
			self.previous_hash = previous_hash
			self.block_hash = self.block_hash()

	def block_hash(self):
			inp = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
			return hash(inp)

def next_block(last_block):
		ind = last_block.index + 1
		timestamp = datetime.now()
		dataString = "Block number " + str(ind)
		current_hash = last_block.block_hash
		return Block(ind, timestamp, dataString, current_hash)

blockchain = [Block(0, datetime.now(), "first Block", "0")]
previous_block = blockchain[0]

for block in range(0, 20):
		new_block = next_block(previous_block)
		blockchain.append(new_block)
		previous_block = new_block
		block_message = f"Added block {new_block.index}"
		print (block_message)
		print (f"new.block_hash: {new_block.block_hash}")

######### END screen6 #########