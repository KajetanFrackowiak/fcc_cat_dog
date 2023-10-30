# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, own_history=["R"], counter=[0],
  play_order=[{ "RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0,
  }]):

counter[0] += 1
ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}

# Abby
if (counter[0]) <= 1000:
last_two = "".join(own_history[-2:])
if len(last_two) == 2:
play_order[0][last_two] += 1

potential_plays = [
own_history[-1] + "R",
own_history[-1] + "P",
own_history[-1] + "S",
]

sub_order = {
k: play_order[0][k]
for k in potential_plays if k in play_order[0]
}

prediction = max(sub_order, key=sub_order.get)[-1:]

own_history += ideal_response[prediction]
return own_history[-1]

#Kris
if (counter[0]) <= 2000:
own_history += ideal_response[own_history[-1]]
return own_history[-1]

#mrugesh
if (counter[0]) <= 3000:
last_ten = own_history[-10:]
most_frequent = ""

most_frequent = max(set(last_ten), key=last_ten.count)

if most_frequent == '':
  most_frequent = "P"

own_history += ideal_response[most_frequent]
return own_history[-1]

#quincy
if (counter[0]) <= 4000:
choices = ["P", "P", "S", "S", "R"]
return (choices[counter[0] % len(choices)])