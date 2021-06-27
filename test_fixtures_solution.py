import pytest

#Implement the fixture that has module scope
@pytest.fixture(scope='module')
def resource_1_setup(request):
    print('\nSetup for resource 1 called')

    def resource_1_teardown():
        print('\nTeardown for resource 1 called')

    # An alternative option for executing teardown code is to make use of the addfinaliz        er method of the request-context object to register finalization functions.
    # Source - https://docs.pytest.org/en/latest/fixture.html
    request.addfinalizer(resource_1_teardown)

def test_1_using_resource_1(resource_1_setup):
    print('Test 1 uses resource 1')

def test_2_not_using_resource_1():
    print('\n Test 2 does not need Resource 1')
