"""Exception for the access_management module"""

class AccessManagementException(Exception):
    """excepcion personalizada para Access Management"""
    
    def __init__(self, message):
        """constructor"""
        #message es el mensaje personalizado
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """Getter de mensaje"""
        return self.__message

    @message.setter
    def message(self, value):
        """Setter de message"""
        self.__message = value
