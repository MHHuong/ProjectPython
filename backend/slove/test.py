from algorithm import Problem, bfs, astar

if __name__ == "__main__":
    from algorithm import Problem, bfs, astar
schedule_data = [
    {"day": 0, "task": "Task 1", "start": "8:00", "end": "9:00"},
    {"day": 2, "task": "Task 2", "start": "10:00", "end": "11:00"},
    {"day": 4, "task": "Task 3", "start": "14:00", "end": "15:00"}
]

tasks_to_schedule = [
    ("New Task 1", 60),  
    ("New Task 2", 30),
    ("New Task 3", 90)
]

problem = Problem(schedule_data, tasks_to_schedule)

print("Testing BFS:")
solution_bfs = bfs(problem)
if solution_bfs:
    print("BFS Solution:")
    print(solution_bfs)
else:
    print("No solution found using BFS.")

print("\nTesting A*:")
solution_astar = astar(problem)
if solution_astar:
    print("A* Solution:")
    print(solution_astar)
else:
    print("No solution found using A*.")
