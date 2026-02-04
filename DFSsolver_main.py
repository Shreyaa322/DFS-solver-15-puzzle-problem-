from DFSsolver import PuzzleState, DFSSolver, Input, Output

if __name__ == "__main__":
    start = Input.get_user_input()

    goal_list = [1, 2, 3, 4,
                 5, 6, 7, 8,
                 9, 10, 11, 12,
                 13, 14, 15, 0]

    goal = PuzzleState(goal_list)
    solver = DFSSolver(start, goal)
    path = solver.solve(max_depth=200)
    Output.display_solution(path)


