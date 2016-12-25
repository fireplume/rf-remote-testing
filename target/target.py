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
