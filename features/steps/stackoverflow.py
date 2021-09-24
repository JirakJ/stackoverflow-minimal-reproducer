from behave import *

use_step_matcher("re")

def assertEquals(var1, var2):
    if var1 == var2:
        print("Parsed argument is same as input")
        return True
    else:
        print("Parsed input is different than expected value")
        return False

@then("Just test of arg")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    userdata = context.config.userdata
    print("Not expected: {}".format(userdata["triggeredBy"]))
    assert assertEquals(userdata["triggeredBy"], '"Test')

@then("Just test of expected arg")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    userdata = context.config.userdata
    print("Expected: {}".format(userdata["triggeredBy"]))
    assert assertEquals(userdata["triggeredBy"], 'Test Name')