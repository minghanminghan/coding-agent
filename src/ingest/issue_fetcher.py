from ..utils import g


# get all issues from a repo
def fetch_issues(repo_name: str):
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state='open')
    return issues


# get single issue by number
def fetch_issue(repo_name: str, issue_number: int):
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(issue_number)
    return issue


if __name__ == "__main__":
    from pprint import pprint
    repo_name = "minghanminghan/stock-trader"
    issues = fetch_issues(repo_name)
    # for issue in issues:
    #     pprint(issue.raw_data)

    issue = fetch_issue(repo_name, issues[0].number)
    pprint(issue.raw_data)