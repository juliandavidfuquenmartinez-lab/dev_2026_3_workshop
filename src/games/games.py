class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = ["piedra", "papel", "tijera"]

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "papel" and jugador2 == "piedra") or \
           (jugador1 == "tijera" and jugador2 == "papel"):
            return "jugador1"

        return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"

        if intento > numero_secreto:
            return "muy alto"

        return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        lineas = [
            tablero[0],
            tablero[1],
            tablero[2],
            [tablero[0][0], tablero[1][0], tablero[2][0]],
            [tablero[0][1], tablero[1][1], tablero[2][1]],
            [tablero[0][2], tablero[1][2], tablero[2][2]]
        ]

        for linea in lineas:
            if linea[0] != " " and linea[0] == linea[1] == linea[2]:
                return linea[0]

        tablero_lleno = True

        for fila in tablero:
            for casilla in fila:
                if casilla == " ":
                    tablero_lleno = False

        if tablero_lleno:
            diagonal_principal = [
                tablero[0][0],
                tablero[1][1],
                tablero[2][2]
            ]

            diagonal_secundaria = [
                tablero[0][2],
                tablero[1][1],
                tablero[2][0]
            ]

            if diagonal_principal[0] == diagonal_principal[1] == diagonal_principal[2]:
                return diagonal_principal[0]

            if diagonal_secundaria[0] == diagonal_secundaria[1] == diagonal_secundaria[2]:
                return diagonal_secundaria[0]

            return "empate"

        return "continua"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        random = __import__("random")
        combinacion = []

        for i in range(longitud):   
            posicion = random.randint(0, len(colores_disponibles) - 1)
            combinacion.append(colores_disponibles[posicion])

        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        if desde_fila < 0 or desde_fila > 7 or desde_col < 0 or desde_col > 7:
            return False

        if hasta_fila < 0 or hasta_fila > 7 or hasta_col < 0 or hasta_col > 7:
            return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1

            for columna in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][columna] != " ":
                    return False

        else:
            paso = 1 if hasta_fila > desde_fila else -1

            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        return True