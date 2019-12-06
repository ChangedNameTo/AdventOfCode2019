# f = open('6/test.txt')
# f = open('6/test2.txt')
f = open('6/input.txt')

orbit_map = {}

santa_node = None
you_node = None
class Orbits():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.orbits = 0

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self.name

    def get_orbits(self):
        return self.orbits

    def add_children(self, child):
        self.children.append(child)

    def total_orbits(self, num_parents):
        if not self.children:
            return num_parents
        else:
            total_orbits = num_parents
            num_parents += 1

            for child in self.children:
                total_orbits += child.total_orbits(num_parents)

            return total_orbits

    def print_parents(self, par_arr):
        print_arr = []
        for par in par_arr:
            print_arr.append(par.get_name())

        print(print_arr)

    def get_parents(self):
        curr = self
        parents = []
        while curr.parent:
            parents.append(curr.parent)
            curr = curr.parent

        return parents

    def find_santa(self, santa_node):
        my_parents = self.get_parents()
        santa_parents = santa_node.get_parents()

        common_parent = None
        for parent in my_parents:
            if parent in santa_parents:
                common_parent = parent
                break

        # Trav to parent
        trav_arr = []
        for parent in my_parents:
            trav_arr.append(parent)
            if parent == common_parent:
                break

        for x in range((santa_parents.index(common_parent)-1),-1,-1):
            trav_arr.append(santa_parents[x])

        return len(trav_arr) - 1

    def get_children(self):
        return [x.get_name() for x in self.children]


lines = f.read().splitlines()

for line in lines:
    orbiter = line.split(')')[0]
    orbitee = line.split(')')[1]

    if orbiter not in orbit_map:
        orbit_map[orbiter] = Orbits(orbiter)

    orbiter_obj = orbit_map[orbiter]

    if orbitee not in orbit_map:
        orbit_map[orbitee] = Orbits(orbitee, orbiter_obj)

    orbitee_obj = orbit_map[orbitee]
    if not orbitee_obj.parent:
        orbitee_obj.parent = orbiter_obj

    if orbitee == 'YOU':
        you_node = orbitee_obj

    if orbitee == 'SAN':
        santa_node = orbitee_obj

    orbiter_obj.add_children(orbitee_obj)

root_orbit = orbit_map['COM']
# orbits = root_orbit.total_orbits(0)
# print('======')
# print(orbits)

print(you_node.find_santa(santa_node))