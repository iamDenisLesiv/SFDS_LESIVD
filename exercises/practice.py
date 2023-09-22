from collections import defaultdict, deque

def task_manager(tasks):
    task_dict = defaultdict(deque)
    for task in tasks:
        if task[2]:
            task_dict[task[1]].appendleft(task[0])
        else:
            task_dict[task[1]].append(task[0])
    return task_dict

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))