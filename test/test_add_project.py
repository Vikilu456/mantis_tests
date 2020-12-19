from model.project import Project
import random

def test_add_project(app, db):
    project = Project(name=("Project %s" % random.randrange(1, 100)), description="description1")
    old_project_list = db.get_project_list()
    app.project.create(project)
    new_project_list = db.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)