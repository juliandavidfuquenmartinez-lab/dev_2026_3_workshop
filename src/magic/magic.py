class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
            return None

        a = 0
        b = 1

        for _ in range(n):
            a, b = b, a + b

        return a
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []

        secuencia = []

        for i in range(n):
            secuencia.append(self.fibonacci(i))

        return secuencia
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos = []

        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)

        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n <= 1:
            return False

        suma = 0

        for i in range(1, n):
            if n % i == 0:
                suma += i

        return suma == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo = []

        for i in range(filas):
            fila = [1]

            if i > 0:
                anterior = triangulo[i - 1]

                for j in range(len(anterior) - 1):
                    fila.append(anterior[j] + anterior[j + 1])

                fila.append(1)

            triangulo.append(fila)

        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n < 0:
            return None

        resultado = 1

        for i in range(1, n + 1):
            resultado = resultado * i

        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b != 0:
            a, b = b, a % b

        return abs(a)
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
            return 0

        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        n = abs(n)
        suma = 0

        for digito in str(n):
            suma += int(digito)

        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        if n < 0:
            return False

        digitos = str(n)
        cantidad = len(digitos)
        suma = 0

        for digito in digitos:
            suma += int(digito) ** cantidad

        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)

        suma_magica = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_magica:
                return False

        for columna in range(n):
            suma = 0
            for fila in range(n):
                suma += matriz[fila][columna]

        if suma != suma_magica:
            return False

        suma_diagonal = 0
        for i in range(n):
            suma_diagonal += matriz[i][i]

        if suma_diagonal != suma_magica:
            return False

        suma_diagonal = 0
        for i in range(n):
            suma_diagonal += matriz[i][n - 1 - i]

        if suma_diagonal != suma_magica:
            return False

        return True