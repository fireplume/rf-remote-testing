from robot.libraries.BuiltIn import BuiltIn

# You may want to divide the implementation in several classes
class _common_a(object):
    def feature_a(self):
        return "feature_a called!"

class _common_b(object):
    def feature_b(self):
        return "feature_b called!"

# By inheriting all of them in a one main class, you'll only need to
# import this one.
class common_services(_common_a, _common_b):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        super(common_services, self).__init__()

    def common(self):
        return "common called!"

    def get_keyword_names(self):
        return ['common', 'feature_a', 'feature_b']

    def get_keyword_documentation(self, name):
        if name == "common":
            return "Dumb common library keyword"
        elif name == "feature_a":
            return "Dumb base class library keyword"
        elif name == "feature_b":
            return "Dumb base class library keyword"
