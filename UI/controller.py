import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillddAnno(self):
        for anno in self._model.getAnno():
            self._view.ddAnno.options.append(
              ft.dropdown.Option(anno))

    def fillddBrand(self):
        pass

    def fillddRetailer(self):
        pass

    def handlePrintTopV(self, e):
        pass

    def handlePrintAnalizzaV(self, e):
        pass


