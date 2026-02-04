import numpy as np


class PuzzleState:
    def __init__(self, state):
        if len(state) != 16:
            raise ValueError("State must have 16 numbers")
        self.state = tuple(state)

    def Find_Blank(self):
        idx = self.state.index(0)
        return divmod(idx, 4)

    def is_goal(self, goal):
        return self.state == goal.state

    def get_neighbors(self):
        neighbors = []
        idx = self.state.index(0)
        row, col = divmod(idx, 4)
        moves = []

        if row > 0: moves.append((-1, 0))
        if row < 3: moves.append((1, 0))
        if col > 0: moves.append((0, -1))
        if col < 3: moves.append((0, 1))

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            new_idx = new_row * 4 + new_col

            new_state = list(self.state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(PuzzleState(new_state))

        return neighbors

    def __repr__(self):
        rows = [self.state[i:i + 4] for i in range(0, 16, 4)]
        return "\n".join(str(row) for row in rows)


class DFSSolver:
    def __init__(self, start_state, goal_state):
        self.start = start_state
        self.goal = goal_state

    def solve(self, max_depth=200):
        stack = [(self.start, [self.start])]
        visited = set()
        while stack:
            state, path = stack.pop()
            if state.state in visited:
                continue
            visited.add(state.state)
            if state.state == self.goal.state:
                return path
            if len(path) <= max_depth:
                for neighbor in state.get_neighbors():
                    if neighbor.state not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return None


class Input:
    def get_user_input():
        print("Enter 16 numbers: ")
        values = []
        for i in range(16):
            num = int(input(f"Enter number {i + 1}: "))
            values.append(num)
        return PuzzleState(values)


class Output:
    def display_solution(path):
        if not path:
            print("No solution found")
            return
        print(f"solution found in {len(path) - 1} moves:")
        for step, state in enumerate(path):
            print(f"Step{step}:")
            print(state)
            print("-" * 20)
