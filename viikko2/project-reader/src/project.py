class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, proj_license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.proj_license = proj_license
        self.authors = authors

        

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):

        authorstring = ""
        depstring = ""
        devdepstring = ""

        for author in self.authors:
            authorstring += "- " + author + f"\n"

        for dep in self.dependencies:
            depstring += "- " + dep + f"\n"

        for devdep in self.dev_dependencies:
            devdepstring += "- " + devdep + f"\n"

        
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.proj_license or '-'}"
            f"\n"
            f"\nAuthors:"
            f"\n{authorstring}"
            f"\nDependencies:"
            f"\n{depstring}"
            f"\nDevelopment dependencies:"
            f"\n{devdepstring}"
        )
