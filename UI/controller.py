from collections import Counter

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
                ft.dropdown.Option( #per ogni retailer del ciclo si crea un ogetto
                    key=retailer.Retailer_code,#chiave del dizionario
                    text=retailer.Retailer_name, # quello che l'utente vede nel menu a tendina
                    data=retailer, #creo un riferimento in memoria dell'oggetto retailer
                    on_click=self.read_retailer))

    def read_retailer(self, e):
        if e.control.data is None:
            self._retailer = None
        else: self._retailer = e.control.data #control è un attributo dell'oggetto 'e',
        # punta specificamente all'elemento grafico che ha scatenato l'evento.

    def handlePrintTopV(self, e):
        anno = self._view.ddAnno.value
        if anno == "Nessun filtro":
            anno = None
        brand = self._view.ddBrand.value
        if brand == "Nessun filtro":
            brand = None

        retailer = self._view.ddRetailer.value
        if retailer == "Nessun filtro":
            retailer = None
        #retailerCode = self._retailer.Retailer_code if self._retailer else None #seleziono il codice retailer se esiste

        sales = self._model.getSales(anno, brand, retailer)
        if not sales:
            self._view.create_alert("Non ci sono vendite con questi dati")
            self._view.update_page()
            return

        self._view.txt_result.controls.clear()
        for s in sales:
            self._view.txt_result.controls.append(ft.Text(s))
        self._view.update_page()

    def handlePrintAnalizzaV(self, e):
        anno = self._view.ddAnno.value
        if anno == "Nessun filtro":
            anno = None
        brand = self._view.ddBrand.value
        if brand == "Nessun filtro":
            brand = None

        retailer = self._view.ddRetailer.value
        if retailer == "Nessun filtro":
            retailer = None

        sales = self._model.getSalestot(anno, brand, retailer)
        if not sales:
            self._view.create_alert("Non ci sono vendite con questi dati")
            self._view.update_page()
            return

        giro_Daffari= 0
        for s in sales:
            ricavo= int(s.ricavo)
            giro_Daffari += ricavo

        numvend = len(Counter(sales))

        rtCoinvolti = len(Counter(s.Retailer_code for s in sales))
        numProd = len(Counter(s.Product_number for s in sales))

        self._view.txt_result.controls.clear()
        for s in sales:
            self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite:\n"
                                                          f"Giro d'affari: {giro_Daffari}\n"
                                                          f"Numero vendite {numvend}\n"
                                                          f"Numero retailer coinvolti {rtCoinvolti}\n"
                                                          f"Numero prodotti coinvolti {numProd}"))
        self._view.update_page()

