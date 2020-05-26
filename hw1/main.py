from typing import NamedTuple, Tuple, List


class State(NamedTuple):
    """
    State representing the river's state at a given point
    origin_state: (missionaries, cultists) at origin side
    target_state: (missionaries, cultists) at target side
    boat_location: bool; T for Target, F for Origin
    """
    origin_state: Tuple[int, int]
    target_state: Tuple[int, int]
    boat_location: bool
    attached_states: List['State'] = []


# hand create state space diagram
start_state = State((3, 3), (0, 0), False)

n11 = State((2,2), (1,1), True)
n12 = State((3,2), (0,1), True)
n13 = State((3,1), (0,2), True)

n21 = State((3,2), (0,1), False)
n31 = State((3,0), (0,3), True)
n41 = State((3,1), (0,2), False)
n51 = State((1,1), (2,2), True)
n61 = State((2,2), (1,1), False)
n71 = State((0,2), (3,1), True)
n81 = State((0,3), (3,0), False)
n91 = State((0,1), (3,2), True)

n101 = State((0,2), (3,1), False)
n102 = State((0,1), (3,2), False)
n103 = State((1,1), (2,2), False)
goal_state = State((0, 0), (3, 3), True)

start_state.attached_states = [n11, n12, n13]

n11.attached_states = [start_state, n21]
n12.attached_states = [start_state]
n13.attached_states = [start_state, n21]

n21.attached_states = [n11, n13, n31]
n31.attached_states = [n21, n41]
n41.attached_states = [n31, n51]
n51.attached_states = [n41, n61]
n61.attached_states = [n51, n71]
n71.attached_states = [n61, n81]
n81.attached_states = [n71, n91]
n91.attached_states = [n81, n101, n103]

n101.attached_states = [n91, goal_state]
n102.attached_states = [goal_state]
n103.attached_states = [n91, goal_state]

goal_state.attached_states = [n101, n102, n103]


def breadth_first_search():
    pass


def astar_search():
    pass


if __name__ == "__main__":
    print(f"")
