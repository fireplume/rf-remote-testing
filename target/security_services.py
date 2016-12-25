from robot.libraries.BuiltIn import BuiltIn

class security_services:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def security_a(self):
        return "security_a called!"

    def get_keyword_names(self):
        return ["security_a"]

    def get_keyword_documentation(self, name):
        if name == "security_a":
            return "Dumb security_a test function."

