# Lets play!

def HillHouse():
    door = raw_input("Knock. Door open or close >")

    if door in ['open', 'Open', 'OPEN']:
        path = raw_input("Left or Right? > ")

        if path in ['left', 'LEFT', 'Left']:
            print
            dead("Monster Attack")
        elif path in ['right', 'Right', 'RIGHT']:
            print
            dead("You exited the building. Game Over.")

    elif door in ['close','Close', 'CLOSE']:
        print
        print "Walk away! Safe."
        print
        exit(0)

    else:
        print
        print "I do not understand. Please try again."
        print
        HillHouse()


def DarkForest():
    eyes = raw_input("Eyes open or closed: > ")

    if eyes in ['open', 'Open', 'OPEN']:
        print
        dead("Green eyed monster attacked.")
    elif eyes in ['closed', 'Closed', 'CLOSED']:
        print
        path = raw_input("Choose Path, Left or Right > ")

        if path in ['left', 'LEFT', 'Left']:
            print
            print "You have reached the river. You are stranded."
            print "Build a bridge or you are dead."
            print
            bridg = raw_input ("Did you build a bridge - Yes or No ?")
            print
            bridge(bridg)
        elif path in ['right', 'Right', 'RIGHT']:
            print
            dead("You fell off a mountain.")


def bridge(bridg):
    if bridg in ['yes', 'Yes', 'YES']:
        print
        print
        print "Checking if there is a path... "
        print
        print "Please Wait."
        print
        print "You are safe. Walk away!"
        print
        exit(0)
    else:
        print
        print "You are stranded! Try again later."
        exit(0)


def Night():
    choose = raw_input("HillHouse or Forest: > ")

    if choose in ['hillhouse','HillHouse','HILLHOUSE']:
        print
        HillHouse()
    elif choose in ['forest','FOREST','Forest']:
        print
        DarkForest()
    else:
        print
        print "Incorrect Input. Exiting game."
        exit(0)


def Day():
    HillHouse()


def dead(why):
    print
    print "You are dead!", why
    exit(0)


def start():
    print
    print "Do you want Daylight or Moonlight?"
    light = raw_input("> ")
    print

    if light in ['daylight', 'DAYLIGHT', 'Daylight']:
        print
        Day()
    elif light in ['moonlight', 'MOONLIGHT', 'Moonlight']:
        print
        Night()
    else:
        print
        print "Incorrect input. Exiting game."
        exit(0)


# Main Program
start()
