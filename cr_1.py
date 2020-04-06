from todoist.api import TodoistAPI
api = TodoistAPI('d9deec7ba39852d370168e80ebb66e4b60d927df')
api.sync()
#print(api.state['projects'])
# project1 = api.projects.add('Project1')
""" api.commit()
print(project1) """
project1 = api.projects.add('Project1')
task1 = api.items.add('Task1', project_id=project1['id'])
task2 = api.items.add('Task2', project_id=project1['id'])
api.commit()

#print(api.state['projects'])
# project1 = api.projects.add('Project1')

