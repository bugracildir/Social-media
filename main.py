import sys
f = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
f3 = open("output.txt", "w")
dict = {}  # DICTIONARY FOR FRIENDSHIPS
list = []  # LIST FOR COMMANDS

# TAKING COMMANDS AND ADDING THEM TO LIST
for b in f2:
    b = b.strip()
    if b.endswith("\n"):
        list.append(b[:-1])
    else:
        list.append(b)

# DICTIONARY CREATION
for i in f:
    i = i.strip()
    person, friends = i.split(":")
    if friends.endswith("\n"):
        friends = friends[:-1]
    dict[person] = friends.split(" ")

for a in list:  # THIS LIST HAVE OUR COMMANDS

    # ADD NEW USER COMMANDS
    if a.startswith("ANU"):
        if a[4:] in dict.keys():
            f3.write("ERROR: Wrong input type! for 'ANU’! -- This user already exists !!\n")
        else:
            dict[a[4:]] = []
            f3.write("User '{}' has been added to the social network successfully\n".format(a[4:]))

    # DELETE EXISTING USER COMMANDS
    if a.startswith("DEU"):
        if a[4:] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'DEU'!--There is no user named '{}' !!\n".format(a[4:]))
        else:
            dict.pop(a[4:])
            for b in dict:
                if a[4:] in dict[b]:
                    dict[b].remove(a[4:])
            f3.write("User '{}' and his/her all relations have been deleted successfully\n".format(a[4:]))

    # ADD NEW FRIEND COMMANDS
    if a.startswith("ANF"):
        c = a.split()
        if c[1] not in dict.keys() and c[2] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{0}' and '{1}' found!\n".format(c[1], c[2]))
        elif c[2] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' found!!\n".format(c[2]))
        elif c[1] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' found!!\n".format(c[1]))
        elif c[2] in dict[c[1]]:
            f3.write("ERROR: A relation between '{0}' and '{1}' already exists!!\n".format(c[1], c[2]))
        else:
            dict[c[1]].append(c[2])
            dict[c[2]].append(c[1])
            f3.write("Relation between {0} and {1} has been added successfully\n".format(c[1], c[2]))

    # DELETE EXISTING FRIEND COMMANDS
    if a.startswith("DEF"):
        d = a.split()
        if d[1] not in dict.keys() and d[2] not in dict.keys():
            f3.write(
                "ERROR: Wrong input type! for 'DEF'! -- No user named '{0}' and '{1}' found!!\n".format(d[1], d[2]))
        elif d[2] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' found!!\n".format(d[2]))
        elif d[1] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' found!!\n".format(d[1]))
        elif d[2] not in dict[d[1]]:
            f3.write("ERROR: No relation between '{0}' and '{1}' found!!\n".format(d[1], d[2]))
        else:
            dict[d[1]].remove(d[2])
            dict[d[2]].remove(d[1])
            f3.write("Relation between '{0}' and '{1}' has been deleted successfully”\n".format(d[1], d[2]))

    # COUNT FRIEND COMMANDS
    if a.startswith("CF"):
        e = a.split()
        if e[1] in dict.keys():
            z = len(dict[e[1]])
            f3.write("User '{0}' has {1} friends\n".format(e[1], str(z)))
        elif e[1] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'CF'! -- No user named '{}' found!\n".format(e[1]))

    # FIND POSSIBLE FRIEND COMMANDS
    if a.startswith("FPF"):
        g = a.split()
        list1 = []
        if g[1] not in dict.keys():
            f3.write("ERROR: Wrong input type! for 'FPF'! -- No user named '{}' found!\n".format(g[1]))
        elif int(g[2]) > 3 or int(g[2]) < 1:
            f3.write("ERROR: Maximum distance is out of range!!\n")
        elif g[1] in dict.keys() and g[2] == str(2):
            x = set()
            for z in dict[g[1]]:
                for b in dict[z]:
                    x.add(b)
                    x.add(z)
                if g[1] in x:
                    x.remove(g[1])
            f3.write("User '{0}' has {1} possible friends when maximum distance is 2\n".format(g[1], len(x)))
            f3.write("These possible friends: {")
            f3.write(str(sorted(x))[1:-1])
            f3.write("}\n")
        elif g[1] in dict.keys() and g[2] == str(1):
            x = set()
            for z in dict[g[1]]:
                x.add(z)
            f3.write("User '{0}' has {1} possible friends when maximum distance is 1\n".format(g[1], len(x)))
            f3.write("These possible friends: {")
            f3.write(str(sorted(x))[1:-1])
            f3.write("}\n")
        elif g[1] in dict.keys() and g[2] == str(3):
            x = set()
            for z in dict[g[1]]:
                for b in dict[z]:
                    for c in dict[b]:
                        x.add(c)
                        x.add(b)
                        x.add(z)
                    if g[1] in x:
                        x.remove(g[1])
            f3.write("User '{0}' has {1} possible friends when maximum distance is 3\n".format(g[1], len(x)))
            f3.write("These possible friends: {")
            f3.write(str(sorted(x))[1:-1])
            f3.write("}\n")

    # SUGGEST FRIEND COMMANDS
    if a.startswith("SF"):
        h = a.split()
        list4 = []
        list5 = []
        if h[1] not in dict.keys():
            f3.write("Error: Wrong input type! for 'SF'!--No user named '{}' found!! \n".format(h[1]))
        elif h[2] > str(3) or h[2] < str(2):
            f3.write("Error: Mutually Degree cannot be less than 1 or greater than 4  \n")
        elif h[2] == str(2) or h[2] == str(3):
            f3.write("Suggestion List for '{0}' (when MD is {1}):\n".format(h[1], h[2]))
            for z in dict[h[1]]:
                for b in dict[z]:
                    if b != h[1]:
                        list4.append(b)
                    list4.sort()
            if h[2] == str(2):
                for t in range(3):
                    for v in list4:
                        b = list4.count(v)
                        if b == 2:
                            f3.write("'{0}' has 2 mutual friends with '{1}'\n".format(h[1], v))
                            list5.append(v)
                            list4.remove(v)
                            list4.remove(v)

            for t in range(3):
                for v in list4:
                    b = list4.count(v)
                    if b == 3:
                        f3.write("'{0}' has 3 mutual friends with '{1}'\n".format(h[1], v))
                        list5.append(v)
                        list4.remove(v)
                        list4.remove(v)
                        list4.remove(v)
            f3.write("The suggested friends for '{}':".format(h[1]))
            f3.write(str(sorted(list5))[1:-1])
            f3.write("\n")