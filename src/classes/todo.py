import enum
from typing import Optional, Literal, Union, Callable


class TaskStatus(enum.Enum):
    PENDING = 0
    IN_PROGRESS = 1
    DONE = 2


class Task:
    def __init__(self, title, validate: Callable, description: Optional[str], status: TaskStatus=TaskStatus.PENDING):
        self.title: str = title
        # call validation function after the task is done to check if it is done correctly
        self.validate = validate
        self.description: Optional[str] = description
        self.status: TaskStatus = status


class Todo:
    def __init__(self, tasks: list[Task]=[]):
        self.tasks = tasks
        self.current_task_index = -1
        self.current_task = None
        for i, task in enumerate(tasks):
            if task.status != TaskStatus.DONE:
                self.current_task = task
                self.current_task_index = i
                break

    def add_task(self, task: Task):
        self.tasks.append(task)


    def update_current_task_status(self, status: Union[Literal[TaskStatus.DONE], Literal[TaskStatus.IN_PROGRESS]]):
        if self.current_task:
            self.current_task.status = status
        
        if status == TaskStatus.DONE:
            self.current_task_index += 1
            if self.current_task_index < len(self.tasks):
                self.current_task = self.tasks[self.current_task_index]


    def get_current_task(self) -> Optional[Task]:
        return self.current_task


    def get_all_tasks(self) -> list[Task]:
        return self.tasks
    
    def is_finished(self) -> bool:
        return all(task.status == TaskStatus.DONE for task in self.tasks)