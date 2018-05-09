import pytest

from source.lib import Customer

class TestCustomer:

    def setup(self):
        print('Setup: \'%s\'' % "TestCustomer")

    def teardown(self):
        print('Teardown: \'%s\'' % "TestCustomer")

    def setup_class(cls):
        print('Setup class: \'%s\'' % cls.__name__)

    def teardown_class(cls):
        print('Teardown class: \'%s\'' % cls.__name__)

    def test_create_customer(self):
        customer = Customer('Joe Doe', 10.0)
        assert customer.balance == 10.0
        assert customer.name == 'Joe Doe'

    def test_set_balance(self):
        customer = Customer('Joe Doe', 10.0)
        customer.set_balance(100.0)
        assert customer.balance == 100.0

    def test_deposit_valid_amount_of_money(self):
        customer = Customer('Joe Doe', 10.0)
        customer.deposit(10.0)
        assert customer.balance == 20.0

    def test_deposit_invalid_amount_of_money(self):
        customer = Customer('Joe Doe', 10.0)
        with pytest.raises(RuntimeError) as e:
            customer.deposit(-1.0)

    def test_withdraw_valid_amount_of_money(self):
        customer = Customer('Joe Doe', 10.0)
        customer.withdraw(5.0)
        assert customer.balance == 5.0

    def test_withdraw_invalid_amount_of_money(self):
        customer = Customer('Joe Doe', 10.0)
        with pytest.raises(RuntimeError) as e:
            customer.withdraw(20.0)
