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
        return self.colour


with open("day07-1.txt") as f:
    colours = {}
    nums = {}
    for line in f:
        node, children = line.strip().split(" contain ")
        node = " ".join(node.split(" ")[:2])
        numbers = None
        if "no other bags" in children:
            children = None
        else:
            numbers = [int(x.strip().split(" ")[0]) for x in children.split(",")]
            children = [" ".join(x.strip().split(" ")[1:3]) for x in children.split(",")]
        if node not in colours.keys():
            colours[node] = Node(node)
        if children:
            for child, num in zip(children, numbers):
                if child not in colours.keys():
                    colours[child] = Node(child)
                colours[child].add_parent(colours[node])
                colours[node].add_child(colours[child])
                nums[f"{node}->{child}"] = num

def get_children_bags(node):
    if len(node.children) > 0:
        total = 0
        for c in node.children:
            total += nums[f"{node}->{c}"] * get_children_bags(c)
        return total + 1
    else:
        return 1

print(get_children_bags(colours["shiny gold"]) - 1)