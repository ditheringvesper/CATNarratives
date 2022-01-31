# a narrative generator (from the path)

import random
import textwrap

direction = ['over there', 'there', 'further', 'to the left', 'to the right', 'backwards', 'up', 'back', 'down', 'clockwise', 'upstairs','through']
site = ['main street', 'stone-paved road', 'marble wall', 'slope', 'big garden', 'station', 'forest', 'city', 'lake', 'starting point', 'park', 'museum', 'turnstile', 'tunnel', 'staircase','hill']
time = ['now', 'for a moment', 'every ten minutes', 'an hour later', 'a couple of years later', 'sometimes', 'one second','two seconds','three seconds']
pverb = ['waited', 'ran', 'looked', 'stopped', 'turned', 'went', 'followed', 'remembered', 'closed', 'passed', 'covered','walked', 'sat','watched']
verb = ['wait', 'run', 'look', 'stop', 'turn', 'go', 'follow', 'remember', 'close', 'pass', 'cover','walk', 'sit','watch']

adj = ['visible', 'dark', 'luxuriant', 'outbound', 'blue', 'green', 'grey', 'red', 'silver', 'tall', 'short','narrowing','swelling', 'damped-out','crowded']
obj = ['rain', 'smell of alcohol and grease', 'path', 'steps', 'leaves', 'sunlight', 'color', 'window', 'glow', 'weeds', 'ticket','bench']
environment = ['']

emotion = ['lovely','intense pain','going to pass out','difficult','terrible','embarrassed']
dialogue = ['what happened?','can you see it?','oh...','what does it want?','no.','can you still see it?','Do you remember what it was?','everything is gone.',"it's ok.",'would it be ok?']
 # dialogues are full sentences
subject = ['you','we','I']
prep = random.sample(["was", "were"], k=2)




def subaction():
    subact = random.choice(subject)
    subact += " " + random.choice(pverb) + " " + random.choice(direction) + "."
    return subact.capitalize()

def feeling():
    e = random.choice(emotion)
    emo = '- ' + '"' + e.capitalize() + "." + '"'
    return emo

def dial():
    dia1 = '- ' + '"' + random.choice(dialogue).capitalize() + '"'
    dia2 = '- ' + '"' + random.choice(dialogue).capitalize() + '"'
    return dia1
    return dia2


def imperative():
    v = '- ' + '"' + random.choice(verb).capitalize() + " " + random.choice(direction) + "." + '"'
    return v


def timespan():
    t = random.choice(verb)
    t += ","+" " + random.choice(time) + " -"
    return t.capitalize()


def spaceL():
    sL = "The " + random.choice(site) + " " + "was" + " " + random.choice(adj) + ";"
    return sL

def spaceS():
    objs = random.choice(obj)
    if objs == 'weeds' or 'steps' or 'leaves':
        sS = "The " + objs + " " + prep[1] + " " + random.choice(adj) + "."
    else: 
        sS = "The " + objs + " " + prep[0] + " " + random.choice(adj) + "."
    return sS

part_count = 1
for repeat in range(part_count):
    line_count = 10 #random.randrange(3, 10)
    print(' ')
    for i in range(line_count):
        if i == 0:
            print(dial())
            print(dial())
        elif i == line_count - 1:
            print(' ')
        elif i == line_count - 2:
            print(subaction())
            print(imperative())
        elif i == line_count - 3:
            print(feeling())
        elif i == line_count - 4:
            print(subaction())
        else:
            # print(' ')
            print(dial())
    
    print(' ')
    print(subaction())
    print(imperative())

    print(' ')
    print(spaceL())
    print(spaceS())
    print(' ')
