from behave import given, when, then
# from apps.charliauth.tests.factories.user import UserFactory


@when('I visit login page')
def visit(context, url):
    # save response in context for next step
    context.response = context.test.client.get(url)

@then('I should see Django administration')
def visit(context, text):
    # compare with response from ``when`` step
    response = context.response
    context.test.assertContains(response, text)

