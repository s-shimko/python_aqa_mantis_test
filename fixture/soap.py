from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        return self.convert_projects_to_model(client.service.mc_projects_get_user_accessible('administrator', 'root'))

    def convert_projects_to_model(self, soap_projects):
        def convert(project):
            return Project(id=project['id'], name=project['name'], description=project['description'])
        return list(map(convert, soap_projects))
