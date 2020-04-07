from todoist.api import TodoistAPI
import pandas as pd

token = 'd9deec7ba39852d370168e80ebb66e4b60d927df' # I made this up
# create a TodoistAPI object with the token, which we store to the api variable
api = TodoistAPI(token)
# Fetches the latest updated data from the server.
api.sync()
# .data attribute retrieves a python dictionary rather than todoist.models.Project

projects = [project.data for project in api.state['projects']] 
# print(projects)
# I can easily create a DataFrame on the 'projects' list of dicts
df_projects = pd.DataFrame(projects)
# print(df_projects.head())

tasks = [task.data for task in api.state['items']]
# print(tasks)
df_tasks = pd.DataFrame(tasks)
print(df_tasks) 
# print(df_tasks['due_date_utc'])