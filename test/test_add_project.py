import random
from model.project import Project

def test_delete_random_project(app):
    old_projects = app.soap.get_projects()
    app.project.manage()
    name = "project" + str(random.randrange(1000))
    app.project.create(Project(name=name, description='test_description'))
    new_projects = app.soap.get_projects()
    assert len(old_projects) + 1 == len(new_projects)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.soap.get_projects(), key=Project.id_or_max)
    print("Project successfully added")