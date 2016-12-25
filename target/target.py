from robot.libraries.BuiltIn import BuiltIn

class target:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def set_property(self, someproperty, value):
        return "Property %s set to %s" % (someproperty, value)

    def target_op_pass_or_fail(self, flag):
        if flag:
            return "target_op_pass_or_fail succeeded!"
        else:
            raise Exception("target_op_pass_or_fail... failed!")

    def get_keyword_names(self):
        return ['set_property', 'target_op_pass_or_fail']

    def get_keyword_documentation(self, name):
        if name == "set_property":
            return "Dumb set property to requested value keyword."
        elif name == "target_op_pass_or_fail":
            return "Controllable keyword which pass or fail depending on boolean argument.\
Pass False argument to cause test to fail."

