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
        # DOMESTIC ONLY self.order_type = "domestic"
        # self.tax = 0.08

    pass

class InternationalMelonOrder(AbstractMelonOrder):
    """A concrete subclass of AbstractMelonOrder. Handles international orders."""


