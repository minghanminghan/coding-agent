import subprocess
import shutil
import os
from . import logger, ROOT_DIR

class RepoManager:
    def __init__(self, repo_url: str, issue_id: int):
        self.repo_url = repo_url
        self.issue_id = issue_id
        self.branch_name = f'agent/issue-{self.issue_id}'
        repo_name = repo_url.rstrip('/').split('/')[-1]
        self.local_path = os.path.join(ROOT_DIR, 'tmp', f'{repo_name}_{self.issue_id}')


    def setup_workspace(self):
        # create local dir
        subprocess.run(['git', 'clone', self.repo_url, self.local_path], check=True)
        logger.info(f'Cloned repository to {self.local_path}')
        
        # create feature branch
        subprocess.run(['git', 'checkout', '-b', self.branch_name], cwd=self.local_path, check=True)
        logger.info(f'Created new branch {self.branch_name}')


    def commit_changes(self, commit_message: str):
        # Add all changes
        subprocess.run(['git', 'add', '.'], cwd=self.local_path, check=True)

        # Check if there are changes to commit
        result = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=self.local_path)
        if result.returncode == 0:
            logger.info('No changes to commit')
            return False

        # Commit changes
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=self.local_path, check=True)
        logger.info(f'Committed changes with message: {commit_message}')
        return True
    

    def push_changes(self):
        subprocess.run(['git', 'push', 'origin', self.branch_name], cwd=self.local_path, check=True)
        logger.info(f'Pushed changes to remote branch {self.branch_name}')
    

    def cleanup_workspace(self):
        if not os.path.exists(self.local_path):
            logger.info(f'Workspace {self.local_path} does not exist, nothing to clean')
            return

        try:
            # Change out of the directory if we're in it
            if os.getcwd().startswith(self.local_path):
                os.chdir(ROOT_DIR)

            shutil.rmtree(self.local_path)
            logger.info(f'Cleaned up local workspace at {self.local_path}')
        except Exception as e:
            logger.error(f'Failed to cleanup workspace {self.local_path}: {e}')
            # Try force cleanup on Windows
            if os.name == 'nt':
                subprocess.run(['rmdir', '/S', '/Q', self.local_path], shell=True)


if __name__ == "__main__":
    # Example usage
    repo_url = 'https://github.com/minghanminghan/stock-trader'
    issue_id = 1
    manager = RepoManager(repo_url, issue_id)
    
    try:
        manager.setup_workspace()
        # Here you would make changes to the codebase...

        # Create a test file to demonstrate changes
        test_file = os.path.join(manager.local_path, 'tmp.txt')
        with open(test_file, 'w') as f:
            f.write('Test content from agent')

        # Only push if there were changes to commit
        if manager.commit_changes("Automated commit message"):
            manager.push_changes()
        else:
            logger.info("No changes to push")
    finally:
        manager.cleanup_workspace()