class GenerarAlertas:

    def ejecutar(self, repo_stock, repo_animal):

        alertas = []

        # alertas de stock bajo
        insumos = repo_stock.listar()

        for i in insumos:
            if i["cantidad_actual"] <= i["umbral_minimo"]:
                alertas.append({
                    "tipo": "stock",
                    "mensaje": f"Stock bajo: {i['nombre']}"
                })

        # alertas sanitarias simples
        animales = repo_animal.listar()

        for a in animales:
            if a.estado_sanitario == "critico":
                alertas.append({
                    "tipo": "sanitario",
                    "mensaje": f"Animal crítico: {a.codigo_identificacion}"
                })

        return alertas