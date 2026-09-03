class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        if len(numeros) == 0:
            return 0

        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if len(numeros) == 0:
            return 0
        ordenados = sorted(numeros)
        mitad = len(ordenados) // 2
        
        if len(ordenados) % 2 == 0:
            return (ordenados[mitad - 1] + ordenados[mitad]) / 2
        
        return float(ordenados[mitad])
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        if len(numeros) == 0:
            return None

        frecuencias = {}

        for numero in numeros:
            if numero in frecuencias:
                frecuencias[numero] += 1
            else:
                frecuencias[numero] = 1

        moda = numeros[0]
        mayor_frecuencia = frecuencias[moda]

        for numero in numeros:
            if frecuencias[numero] > mayor_frecuencia:
                moda = numero
                mayor_frecuencia = frecuencias[numero]

        return moda
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        if len(numeros) == 0:
            return 0

        promedio = sum(numeros) / len(numeros)

        suma = 0
        for numero in numeros:
            suma += (numero - promedio) ** 2

        varianza = suma / len(numeros)

        return varianza ** 0.5
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        if len(numeros) == 0:
            return 0

        promedio = sum(numeros) / len(numeros)

        suma = 0
        for numero in numeros:
            suma += (numero - promedio) ** 2

        return suma / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        if len(numeros) == 0:
            return 0

        return max(numeros) - min(numeros)