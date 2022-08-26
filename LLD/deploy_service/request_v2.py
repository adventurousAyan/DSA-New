class RequestV2:
    def __init__(self):

        self._model_name = ""
        self._client_id = ""
        self._product_name = ""
        self._model_path = ""
        self._model_type = ""
        self._model_path_type = ""
        self._model_source_path = ""

    @property
    def model_name(self):
        """Project getter

        Returns:
            str: model_name
        """
        return self._model_name

    @model_name.setter
    def model_name(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of model_name
        """
        self._model_name = value.lower()

    @property
    def client_id(self):
        """Project getter

        Returns:
            str: client_id
        """
        return self._client_id

    @client_id.setter
    def client_id(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of client_id
        """
        self._client_id = value.lower()

    @property
    def product_name(self):
        """Project getter

        Returns:
            str: product_name
        """
        return self._product_name

    @product_name.setter
    def product_name(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of product_name
        """
        self._product_name = value

    @property
    def model_path(self):
        """Project getter

        Returns:
            str: model_path
        """
        return self._model_path

    @model_path.setter
    def model_path(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of model_path
        """
        self._model_path = value

    @property
    def model_type(self):
        """Project getter

        Returns:
            str: model_type
        """
        return self._model_type

    @model_type.setter
    def model_type(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of model_type
        """
        self._model_type = value

    @property
    def model_path_type(self):
        """Project getter

        Returns:
            str: model_path_type
        """
        return self._model_path_type

    @model_path_type.setter
    def model_path_type(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of model_path_type
        """
        self._model_path_type = value

    @property
    def model_source_path(self):
        """Project getter

        Returns:
            str: model_source_path
        """
        return self._model_source_path

    @model_source_path.setter
    def model_source_path(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of model_source_path
        """
        self._model_source_path = value
