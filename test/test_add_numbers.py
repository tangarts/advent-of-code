from numtools.sample import NumTools

def test_add_numbers():

    list_of_numbers = [2,5,7]

    assert NumTools.add_numbers(list_of_numbers) == 14


def test_three_numbers():

    assert NumTools.add_numbers([1,2,3]) == 6