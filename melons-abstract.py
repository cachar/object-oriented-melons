class AbstractMelonOrder(object):
    """Abstract class to handle domestic and international orders."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True





class DomesticMelonOrder(AbstractMelonOrder):
    """A concrete subclass of AbstractMelonOrder. Handles domestic orders."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes"""

        self.order_type = "domestic"
        self.tax = 0.08




class InternationalMelonOrder(AbstractMelonOrder):
    """A concrete subclass of AbstractMelonOrder. Handles international orders."""

    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""


        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code