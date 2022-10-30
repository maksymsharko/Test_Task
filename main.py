from clockify_api_client.client import ClockifyAPIClient
from clockify_api_client.models.user import User
from clockify_api_client.models.project import Project
from clockify_api_client.models.task import Task
from collections import ChainMap

API_URL = 'api.clockify.me'
API_KEY = "YTEzMWFiNTctYjVkMS00Mjg3LTgwNGMtZGI0NTUxNTg0NjJm"

usr = User(API_KEY, API_URL)
client = ClockifyAPIClient().build(API_KEY, API_URL)
proj = Project(API_KEY, API_URL)
task = Task(API_KEY, API_URL)

workspace = dict(ChainMap(*client.workspaces.get_workspaces()))
workspace_id = workspace.get("id")

user = usr.get(url="https://api.clockify.me/api/v1/user")
user_all = usr.get(url="https://api.clockify.me/api/v1//workspaces/{}/users".format(workspace_id))

project = dict(ChainMap(*proj.get(url="https://api.clockify.me/api/v1/workspaces/{}/projects".format(workspace_id))))
project_id = project.get("id")

tasks = dict(ChainMap(*task.get(url="https://api.clockify.me/api/v1/workspaces/{}/projects/{}/tasks".format(
    workspace_id, project_id
))))

print("Workspace:", workspace, "Projects:", project, "Current User:", user, "Users:", user_all, "Tasks:", tasks,
      sep='\n')