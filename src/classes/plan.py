from dataclasses import dataclass
from enum import Enum

class IssueType(Enum):
    BUG = "bug"
    FEATURE = "feature"
    DOCUMENTATION = "documentation"
    REFACTOR = "refactor"
    TEST = "test"

@dataclass
class Plan:
    '''
    High-level plan for addressing a Github issue.
    Used to provide guidance to translate the issue into Tasks.
    '''
    type: IssueType
    description: str
    proposed_steps: list[str]