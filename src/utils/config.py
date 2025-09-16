from github import Github, Auth
import os
from dotenv import dotenv_values
env = dotenv_values()


if "GITHUB_TOKEN" not in env:
    raise ValueError("GITHUB_TOKEN not found in environment variables")

auth = Auth.Token(env.get("GITHUB_TOKEN") or '')
g = Github(auth=auth) # exported

ROOT_DIR = os.getcwd()