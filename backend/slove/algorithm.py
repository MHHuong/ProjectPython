from .time.week import Week
from .time import *
from .time.day import convert_time
from .time.task import Task
from .node import Node
import heapq
from collections import deque

class Problem:
    def __init__(self, schedule_data=[], tasks_to_schedule=[]):
        self.week = Week()
        self.tasks_to_schedule = tasks_to_schedule
        self.load_tasks(schedule_data)

    def load_tasks(self, schedule_data):
        for schedule in schedule_data:
            day = schedule["day"]
            task = schedule["task"]
            start = convert_time(schedule["start"])
            end = convert_time(schedule["end"])

            self.week.days[day].add_task(Task(task, start, end))

def getSolution(week):
    return week.get_info()

def bfs(problem):
    start_node = Node(parent=None, week=problem.week,
                      tasks_to_schedule=problem.tasks_to_schedule)

    frontier = deque([start_node])
    explored = set()

    while len(frontier) > 0:
        node = frontier.popleft()
        explored.add(tuple(node.week.get_info().items()))

        if node.goal_test():
            return getSolution(node.week)

        for child in node.expand():
            child_info = tuple(child.week.get_info().items())
            if child_info not in explored and child not in frontier:
                frontier.append(child)

    return None  # Failure

def astar(problem):
    start_node = Node(parent=None, week=problem.week,
                      tasks_to_schedule=problem.tasks_to_schedule)

    frontier = [(start_node.f, start_node)]
    explored = set()

    while len(frontier) > 0:
        _, node = heapq.heappop(frontier)
        explored.add(tuple(node.week.get_info().items()))

        if node.goal_test():
            return getSolution(node.week)

        for child in node.expand():
            child_info = tuple(child.week.get_info().items())
            if child_info not in explored:
                heapq.heappush(frontier, (child.f, child))
                explored.add(child_info)

    return None
