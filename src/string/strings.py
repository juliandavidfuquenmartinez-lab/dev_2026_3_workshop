class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = texto.replace(" ", "").lower()

        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        resultado = ""

        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]

        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0

        for caracter in texto:
            if caracter in vocales:
                contador += 1

        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouAEIOUyY"
        contador = 0

        for caracter in texto:
            if caracter.isalpha() and caracter not in vocales:
                contador += 1

        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1_limpio = texto1.replace(" ", "").lower()
        texto2_limpio = texto2.replace(" ", "").lower()

        return sorted(texto1_limpio) == sorted(texto2_limpio)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = ""
        inicio_palabra = True

        for caracter in texto:
            if caracter == " ":
                resultado += caracter
                inicio_palabra = True
            elif inicio_palabra:
                resultado += caracter.upper()
                inicio_palabra = False
            else:
                resultado += caracter

        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = ""
        espacio_anterior = False

        for caracter in texto:
            if caracter == " ":
                if not espacio_anterior:
                    resultado += caracter
                espacio_anterior = True
            else:
                resultado += caracter
                espacio_anterior = False

        return resultado
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if texto == "":
            return False

        inicio = 0

        if texto[0] == "-":
            if len(texto) == 1:
                return False
            inicio = 1

        for i in range(inicio, len(texto)):
            if texto[i] < "0" or texto[i] > "9":
                return False

        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""

        for caracter in texto:
            if "a" <= caracter <= "z":
                nueva_posicion = (ord(caracter) - ord("a") + desplazamiento) % 26
                resultado += chr(ord("a") + nueva_posicion)
            elif "A" <= caracter <= "Z":
                nueva_posicion = (ord(caracter) - ord("A") + desplazamiento) % 26
                resultado += chr(ord("A") + nueva_posicion)
            else:
                resultado += caracter

        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []

        if subcadena == "":
            return posiciones

        for i in range(len(texto) - len(subcadena) + 1):
            coincide = True

            for j in range(len(subcadena)):
                if texto[i + j] != subcadena[j]:
                    coincide = False
                    break

            if coincide:
                posiciones.append(i)

        return posiciones