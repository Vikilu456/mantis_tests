from fixture.project import Project
import random


def test_delete_project(app, db):
    if db.count_projects() == 0:
        app.project.create(Project(name=("Project %s" % random.randrange(1, 100)), description="description1"))

    old_project_list = db.get_project_list()
    project = random.choice(old_project_list)
    app.project.delete_project_by_name(project.name)
    new_project_list = db.get_project_list()
    assert len(old_project_list) - 1 == db.count_projects()
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)

