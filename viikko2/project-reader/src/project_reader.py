from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data=toml.loads(content)
        name=data["tool"]["poetry"]["name"]
        desc=data["tool"]["poetry"]["description"]
        lic=data["tool"]["poetry"]["license"]
        auth=data["tool"]["poetry"]["authors"]
        depen=[]
        for i in data["tool"]["poetry"]["dependencies"].keys():
            depen.append(i)
        dev_depen=[]
        for j in data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys():
            dev_depen.append(j)
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depen, dev_depen,auth,lic)


url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml"
reader = ProjectReader(url)
reader.get_project()