import random
from model.project import Project

def test_add_project(app):
    app.project.manage()
    old_projects = app.soap.get_projects()
    if len(old_projects) == 0:
        name = "project" + str(random.randrange(1000))
        app.project.create(Project(name=name, description='test_description'))
        new_projects = app.soap.get_projects()
        assert len(old_projects) + 1 == len(new_projects)
        assert sorted(new_projects, key=Project.id_or_max) == sorted(app.soap.get_projects(), key=Project.id_or_max)
        print("Project successfully added")
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.soap.get_projects()
    assert len(old_projects) - 1 == len(new_projects)
    # old_projects_removed = old_projects.remove(project)
    # assert sorted(old_projects_removed, key=Project.id_or_max) == sorted(app.project.get_projects_list(), key=Project.id_or_max)
