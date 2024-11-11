from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        kontsa = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        info = kontsa.get('tool', {}).get('poetry', {})

        name = info.get('name')
        desc = info.get('description')
        deps = list(info.get('dependencies', {}).keys())
        devdeps = list(info.get('group', {}).get('dev', {}).get('dependencies').keys())
        proj_license = info.get('license')
        authors = info.get('authors')

        return Project(name, desc, deps, devdeps, proj_license, authors)
