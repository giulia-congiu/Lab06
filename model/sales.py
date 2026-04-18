from dataclasses import dataclass
from datetime import date


@dataclass
class Sales:
    Retailer_code: int
    Product_number: int
    Date: date
    Quantity: int
    Unit_sale_price: float

    def __post_init__(self):
        self.ricavo = self.Unit_sale_price * self.Quantity

    def __eq__(self, other):
        return (self.Retailer_code == other.Retailer_code and
                self.Product_number == other.Product_number and
                self.Date == other.Date)

    def __hash__(self):
        return hash((self.Retailer_code, self.Product_number, self.Date))

    def __str__(self):
        return (f"Data: {self.Date}; Ricavo: {self.ricavo:.2f}; "
                f"Retailer: {self.Retailer_code}; Product: {self.Product_number}")