from model.project import Project
import re

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.fill_forms(project)
        if wd.find_element_by_link_text(project.name).text != project.name:
            raise ValueError("Project wasn't added")

    def delete(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_xpath(".//input[@value='Delete Project']").click()
        wd.find_element_by_xpath(".//input[@value='Delete Project']").click()

    def manage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_forms(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath(".//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath(".//input[@value='Add Project']").click()

    def get_projects_list(self):
        wd = self.app.wd
        projects = wd.find_elements_by_xpath("(.//tbody)[3]/tr[contains(@class,'row')]")
        del projects[0]
        self.project_cache = []
        for p in projects:
            id_text = p.find_element_by_xpath(".//td/a").get_attribute("href")
            id = re.search("=(\d+)$", id_text).group(1)
            name = p.find_element_by_xpath(".//td/a").text
            description = p.find_element_by_xpath("(.//td)[5]").text
            self.project_cache.append(Project(id=id, name=name, description=description))
        return list(self.project_cache)





