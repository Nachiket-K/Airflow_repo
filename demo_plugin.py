from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
import logging as log
from airflow.utils.decorators import apply_defaults
import os

class NachiketGitOperator(BaseOperator):

    @apply_defaults
    def __init__(self, git_repo_path, *args, **kwargs):

        self.git_repo_path = git_repo_path
        super().__init__(*args, **kwargs)

    def execute(self, context):

        GitRepoPath = self.git_repo__path
	g="git clone "
	z=g+GitRepoPath
	os.system(z)

class DemoPlugin(AirflowPlugin):
    name = "demo_plugin"
    operators = [NachiketGitOperator]
    sensors = []
