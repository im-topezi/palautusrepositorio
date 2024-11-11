class Project:
    def __init__(self, name, description, dependencies, dev_dependencies,authors,license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license=license
        self.authors=authors

    def list_maker(self,list):
        string=""
        for d in list:
            string+="\n- "
            string+=d
        return string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense:{self.license}"
            f"\n"
            f"\nAuthors:{self.list_maker(self.authors)}"
            f"\n"
            f"\nDependencies:{self.list_maker(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:{self.list_maker(self.dev_dependencies)}"

            )
