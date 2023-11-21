class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    def __init__(self, mensaje = 'Vacío') -> None:
        self.mensaje = mensaje
        super().__init__(self.mensaje)

