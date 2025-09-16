from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from github import Issue as PyGithubIssue

# TODO: make this a child of PyGithubIssue that contains fixes, notes, etc
@dataclass
class Issue:
    """Represents a GitHub issue to be processed."""
    id: int
    title: str
    description: str
    labels: List[str]

    def is_bug(self) -> bool:
        """Check if this issue is a bug report."""
        return "bug" in self.labels

    def is_feature(self) -> bool:
        """Check if this issue is a feature request."""
        return "enhancement" in self.labels or "feature" in self.labels