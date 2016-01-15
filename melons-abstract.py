class AbstractMelonOrder(object):
    """Abstract class to handle domestic and international orders."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price."""

        flat_fee = 3
        base_price = 5
        total = 0

        # To increase price for Christmas melons:
        if self.species == "christmas" or self.species == "Christmas":
            base_price *= 1.5


        total = (1 + self.tax) * self.qty * base_price            

        # To add flat fee: 
        if self.order_type == "international" and self.qty < 10:
            total += flat_fee

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """A concrete subclass of AbstractMelonOrder that handles
    US government order."""

    pass
    # self.tax = 0
    # self.passed_inspection = False
    # def inspection(self)



class DomesticMelonOrder(AbstractMelonOrder):
    """A concrete subclass of AbstractMelonOrder. Handles domestic orders."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes"""

        return super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)




class InternationalMelonOrder(AbstractMelonOrder):
    """A concrete subclass of AbstractMelonOrder. Handles international orders."""


    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""

        self.country_code = country_code

        return super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

