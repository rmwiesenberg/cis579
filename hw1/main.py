from typing import NamedTuple, Tuple, List


class Node:
    """
    Node representing the river's state at a given point
    """

    def __init__(
            self,
            origin_state: Tuple[int, int],
            target_state: Tuple[int, int],
            boat_location: bool
    ):
        """
        origin_state: (missionaries, cultists) at origin side
        target_state: (missionaries, cultists) at target side
        boat_location: bool; T for Target, F for Origin
        """

        self.origin_state = origin_state
        self.target_state = target_state
        self.boat_location = boat_location
        self.attached_nodes: List['Node'] = []

    def __repr__(self):
        str_out = (
            f"({self.origin_state[0]}|{self.origin_state[1]}, "
            f"{self.target_state[0]}|{self.target_state[1]}, "
        )
        if self.boat_location:
            str_out += "T"
        else:
            str_out += "O"
        return str_out + ")"


# hand create state space diagram
start_state = Node((3, 3), (0, 0), False)

n11 = Node((2, 2), (1, 1), True)
n12 = Node((3, 2), (0, 1), True)
n13 = Node((3, 1), (0, 2), True)

n21 = Node((3, 2), (0, 1), False)
n31 = Node((3, 0), (0, 3), True)
n41 = Node((3, 1), (0, 2), False)
n51 = Node((1, 1), (2, 2), True)
n61 = Node((2, 2), (1, 1), False)
n71 = Node((0, 2), (3, 1), True)
n81 = Node((0, 3), (3, 0), False)
n91 = Node((0, 1), (3, 2), True)

n101 = Node((0, 2), (3, 1), False)
n102 = Node((0, 1), (3, 2), False)
n103 = Node((1, 1), (2, 2), False)
goal_state = Node((0, 0), (3, 3), True)

start_state.attached_nodes = [n11, n12, n13]

n11.attached_nodes = [start_state, n21]
n12.attached_nodes = [start_state]
n13.attached_nodes = [start_state, n21]

n21.attached_nodes = [n11, n13, n31]
n31.attached_nodes = [n21, n41]
n41.attached_nodes = [n31, n51]
n51.attached_nodes = [n41, n61]
n61.attached_nodes = [n51, n71]
n71.attached_nodes = [n61, n81]
n81.attached_nodes = [n71, n91]
n91.attached_nodes = [n81, n101, n103]

n101.attached_nodes = [n91, goal_state]
n102.attached_nodes = [goal_state]
n103.attached_nodes = [n91, goal_state]

goal_state.attached_nodes = [n101, n102, n103]


def breadth_first_search():
    print("Begin breadth-first")
    visited_nodes = []
    paths_to_check = [[start_state]]

    first_goal_path = None
    while paths_to_check:
        path = paths_to_check.pop(0)
        most_recent_node = path[-1]
        if most_recent_node in visited_nodes:
            continue
        print(f"Checking {most_recent_node}")
        visited_nodes.append(most_recent_node)
        if most_recent_node == goal_state:
            first_goal_path = path
            print(f"Found goal node {most_recent_node}")
            break
        for attached_node in most_recent_node.attached_nodes:
            if attached_node not in visited_nodes:
                paths_to_check.append(path + [attached_node])
    if not first_goal_path:
        print("Did not find goal node")
    else:
        print(f"{len(visited_nodes)} nodes checked")
        print(f"Final path: {first_goal_path}")
    print("End breadth-first")


def depth_first_search():
    print("Begin depth-first")
    visited_nodes = []
    paths_to_check = [[start_state]]

    first_goal_path = None
    while paths_to_check:
        path = paths_to_check.pop()
        most_recent_node = path[-1]
        if most_recent_node in visited_nodes:
            continue
        print(f"Checking {most_recent_node}")
        visited_nodes.append(most_recent_node)
        if most_recent_node == goal_state:
            first_goal_path = path
            print(f"Found goal node {most_recent_node}")
            break
        for attached_node in most_recent_node.attached_nodes:
            if attached_node not in visited_nodes:
                paths_to_check.append(path + [attached_node])
    if not first_goal_path:
        print("Did not find goal node")
    else:
        print(f"{len(visited_nodes)} nodes checked")
        print(f"Final path: {first_goal_path}")
    print("End depth-first")


def astar_search():
    print("Begin A*")

    def h(node: Node) -> float:
        # divided by 2 to provide consistency
        return ((3 - node.target_state[0])
                + (3 - node.target_state[1])) / 2

    visited_nodes = []

    # each path: (path_so_far, accumulated_code)
    paths_to_check = [([start_state], 0)]

    first_goal_path = None
    while paths_to_check:
        path, path_cost = paths_to_check.pop(0)
        most_recent_node = path[-1]
        if most_recent_node in visited_nodes:
            continue
        print(f"Checking {most_recent_node}: "
              f"p = {path_cost}: "
              f"h = {h(most_recent_node)}")
        visited_nodes.append(most_recent_node)
        if most_recent_node == goal_state:
            first_goal_path = path
            print(f"Found goal node {most_recent_node}")
            break
        for attached_node in most_recent_node.attached_nodes:
            if attached_node not in visited_nodes:
                paths_to_check.append((path + [attached_node], path_cost + 1))
        paths_to_check = sorted(
            paths_to_check,
            key=lambda x: x[1] + h(x[0][-1])
        )
    if not first_goal_path:
        print("Did not find goal node")
    else:
        print(f"{len(visited_nodes)} nodes checked")
        print(f"Final path: {first_goal_path}")
    print("End A*")


if __name__ == "__main__":
    breadth_first_search()
    print("----------")
    depth_first_search()
    print("----------")
    astar_search()
