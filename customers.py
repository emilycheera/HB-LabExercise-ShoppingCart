"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {}, {}, {}>".format(self.first_name, self.last_name,
                                               self.email)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customer names.

    Dictionary will be {email: Customer(...)}
    """

    customers_by_email = {}

    with open(filepath) as file:
        for line in file:
            (first_name, last_name, email, password) = line.strip().split("|")
            
            customers_by_email[email] = Customer(first_name,
                                                 last_name,
                                                 email,
                                                 password)

    return customers_by_email


def get_by_email(customer_email):
    """Return a customer, given his or her email address."""

    # This relies on access to the global dictionary `customers_by_email`

    return customers_by_email.get(customer_email)


customers_by_email = read_customers_from_file("customers.txt")
