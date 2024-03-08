import ape
import pytest

@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def alice(accounts):
    return accounts[1]

@pytest.fixture
def attacker(accounts):
    return accounts[2]

@pytest.fixture
def vaulty(owner, project):
    return owner.deploy(project.Vaulty)

def test_vault(vaulty, alice, attacker):
    ### YOUR SOLUTION
    # HERE!
    ### END SOLUTION

    # Alice deposits
    vaulty.deposit(sender=alice, value=15 * 10**18)

    ### YOUR SOLUTION
    # HERE!
    ### END SOLUTION

    # Vaulty is empty 😭
    assert(vaulty.balance == 0)
