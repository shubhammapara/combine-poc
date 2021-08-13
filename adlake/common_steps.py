from behave import *

use_step_matcher("re")


@then("User logs in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
