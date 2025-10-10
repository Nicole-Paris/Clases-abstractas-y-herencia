def calcular_descuento( tipo : str , precio : float) -> float:
    if tipo == "navidad":
        return precio * 0.90
    elif tipo == "cliente frecuente":
        return precio * 0.80
    elif tipo == "descuento unico":
        return precio * 0.70
    
print(calcular_descuento("descuento unico", 100))
print(calcular_descuento("cliente frecuente", 100))
print(calcular_descuento("navidad", 100))