from random import choice


def random_name_generator(first, second, x):
    """
        Generates random names.
        Arguments:
         - list of first names
         - list of last names
         - number of random names
    """
    names = []
    for i in range(x):
        names.append("{0} {1}".format(choice(first), choice(second)))
    return set(names)


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
names = random_name_generator(first_names, last_names, 5)
print('\n'.join(names))



# 
# [Running] python -u "c:\Users\bryan\Downloads\PY\python-scripts-master\scripts\13_random_name_generator.py"
# Tyler Taylor
# Mike Jones
# Mike Smith
# Drew Taylor
# Tyler Smith
# 
# [Done] exited with code=0 in 0.134 seconds
