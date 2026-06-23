class GestionarStock:

    def listar(self, repo_stock):
        return repo_stock.listar()

    def actualizar_cantidad(self, repo_stock, id_insumo, cantidad):

        insumo = repo_stock.obtener_por_id(id_insumo)

        if not insumo:
            raise Exception("Insumo no existe")

        nueva_cantidad = insumo["cantidad_actual"] + cantidad

        if nueva_cantidad < 0:
            raise Exception("Stock no puede ser negativo")

        insumo["cantidad_actual"] = nueva_cantidad

        return repo_stock.actualizar(insumo)