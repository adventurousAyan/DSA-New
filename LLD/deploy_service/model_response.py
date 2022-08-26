class ModelResponse:
    def __init__(self):

        self._model_name = ""
        self._client_id = ""
        self._product_name = ""
        self._model_deploy_url = ""

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
    def model_deploy_url(self):
        """Project getter

        Returns:
            str: model_deploy_url
        """
        return self._model_deploy_url

    @model_deploy_url.setter
    def model_deploy_url(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of model_deploy_url
        """
        self._model_deploy_url = value
