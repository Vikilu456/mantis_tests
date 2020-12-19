from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects")
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_project()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed")
        wd.find_element_by_link_text("Proceed").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_manage_project()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_elements_by_xpath("//*[contains(text(), 'Are you sure you want to delete this project and all attached issue reports?')]")
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

