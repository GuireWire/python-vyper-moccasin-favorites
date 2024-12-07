# from script.deploy import deploy_favorites
import pytest

# @pytest.fixture(scope="session")
# def favorites_contract():
#     favorites_contract = deploy_favorites()
#     return deploy_favorites()

# The above was moved into a conftest.py for a more professional look

def test_starting_values(favorites_contract):
    # favorites_contract = deploy_favorites()
    
    assert favorites_contract.retrieve() == 77

def test_can_change_values(favorites_contract):
    # Arrange - Arrange all the stuff we need to set up in order to run the test
    # favorites_contract = deploy_favorites()
    # Act - We call the function and store the number as 42
    favorites_contract.store(42)
    # Assert - We assert if the value was updated
    assert favorites_contract.retrieve() == 42

def test_can_add_people(favorites_contract):
    # Arrange
    new_person = "Tom"
    favorite_number = 16
    # favorites_contract = deploy_favorites()
    
    # Act
    favorites_contract.add_person(new_person, favorite_number)

    # Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)

def test_add_six_persons(favorites_contract):
    # Arrange
    new_person = "Tom"
    favorite_number = 16
    
    # Act: Add 5 persons, the 6th should fail
    for i in range(5):
        favorites_contract.add_person(new_person, favorite_number)
        favorite_number += 1
    
    # Assert: The contract should not let you add more than 5 people
    with pytest.raises(Exception):  # Expecting an error when adding the 6th person
        favorites_contract.add_person(new_person, favorite_number)
    
    # Assert: Check the list of people is still at size 5
    for i in range(5):
        person = favorites_contract.list_of_people(i)  # Providing the index as an argument
        assert person[0] == (favorite_number - 5 + i)  # Check favorite_number
        assert person[1] == new_person  # Check name