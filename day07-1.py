class Node:
    def __init__(self, colour) -> None:
        self.colour = colour
        self.children = set()
        self.parents = set()

    def add_child(self, child):
        self.children.add(child)

    def add_parent(self, parent):
        self.parents.add(parent)

    def __repr__(self) -> str:
        return (
            self.colour
        )


with open("day07-1.txt") as f:
    colours = {}
    for line in f:
        node, children = line.strip().split(" contain ")
        node = " ".join(node.split(" ")[:2])
        if "no other bags" in children:
            children = None
        else:
            children = [" ".join(x.strip().split(" ")[1:3]) for x in children.split(",")]
        if node not in colours.keys():
            colours[node] = Node(node)
        if children:
            for child in children:
                if child not in colours.keys():
                    colours[child] = Node(child)
                colours[child].add_parent(colours[node])
                colours[node].add_child(colours[child])
        # if "shiny gold" == node:
        #     print(line)
        #     print(colours[node].parents)
        #     print(colours[node].children)

sg = colours["shiny gold"]
total = set()
parents = sg.parents
while len(parents) != 0:
    new_parents = []
    for parent in parents:
        total.add(parent)
        new_parents += parent.parents
    parents = new_parents
print(sg.parents)
print(len(total))
