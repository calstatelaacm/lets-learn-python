class Fighter:
	def __init__(self, name, hp, moves):
		self.name = name
		self.hp = hp
		self.moves = moves

def attack(attacker, defender):
	print("Which attack do you want " + attacker.name + " to do?")
	print("Enter 1 for " + attacker.moves[0]["name"])
	print("Enter 2 for " + attacker.moves[1]["name"])
	attack = int(input("Please enter here: ")) - 1
	defender.hp -= attacker.moves[attack]["power"]
	print("------------------------------")
	print(attacker.name + " used " + attacker.moves[attack]["name"] + " and did " + str(attacker.moves[attack]["power"]) + " damage!")

sonicsMoves = [
	{'name': "Spin Dash", 'power': 8},
	{'name': "Homing Attack", 'power': 9}
	]
	
johnSnowsMoves = [
	{'name': "Know Nothing", 'power': 5},
	{'name': "Call Ghost", 'power': 12}
	]

sonic = Fighter("Sonic", 42, sonicsMoves)
johnSnow = Fighter("John Snow", 99, johnSnowsMoves)

# print(sonic.moves[1]["name"])
sonicsTurn = True

while sonic.hp > 0 and johnSnow.hp > 0:
	print("==============================")
	if sonicsTurn:
		attack(sonic, johnSnow)
	else:
		attack(johnSnow, sonic)
		
	print("John Snow has " + str(johnSnow.hp) + " hp")
	print("Sonic has " + str(sonic.hp) + " hp")
	# sonic.hp = -10
	
	sonicsTurn = not sonicsTurn

if sonic.hp < 1:
	print("John Snow WINS!")
else:
	print("Sonic Demolished John Snow")
