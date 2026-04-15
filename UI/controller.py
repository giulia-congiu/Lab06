import flet as ft

from model import retailer


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def fillddAnno(self):
        for anno in self._model.getAnno():
            self._view.ddAnno.options.append(
              ft.dropdown.Option(anno))

    def fillddBrand(self):
        for brand in self._model.getBrand():
            self._view.ddBrand.options.append(
                ft.dropdown.Option(brand))

    def fillddRetailer(self):
        for retailer in self._model.getRetailer():
            self._view.ddRetailer.options.append(
                ft.dropdown.Option(
                    key=retailer.Retailer_code,
                    text=retailer.Retailer_name,
                    data=retailer,
                    on_click=self.read_retailer))

    def read_retailer(self, e):
        self._retailer = e.control.data

    def handlePrintTopV(self, e):
        pass

    def handlePrintAnalizzaV(self, e):
        pass


