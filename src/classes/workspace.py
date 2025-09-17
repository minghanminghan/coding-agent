from typing import Optional
from github.Issue import Issue
from classes.plan import Plan
from todo import Todo

class Workspace():
    def __init__(self, issue: Issue, path: str, plan: Plan):
        self.issue = issue      # link to Github Issue
        self.path = path        # path to cloned repo
        self.plan = plan        # high-level plan for addressing the issue
        self.todo = Todo()      # workspace todo
