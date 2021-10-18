

def print_solved(solutions, answers):
    solved = True
    for i, solution in enumerate(solutions):
        print(solution)
        if solution != answers[i]:
            solved = False
            break

    print("problem solved" if solved else "try again")
