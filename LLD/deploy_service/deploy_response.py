import json


class DeployResponse:
    def __init__(self):

        self._status = ""
        self._message = ""
        self._model_res = []

    @property
    def status(self):
        """Project getter

        Returns:
            str: status
        """
        return self._status

    @status.setter
    def status(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of status
        """
        self._status = value

    @property
    def message(self):
        """Project getter

        Returns:
            str: message
        """
        return self._message

    @message.setter
    def message(self, value: str):
        """Project setter

        Args:
            value ([type]): Value of message
        """
        self._message = value

    @property
    def model_res(self):
        """Project getter

        Returns:
            str: model_res
        """
        return self._model_res

    @model_res.setter
    def model_res(self, value):
        """Project setter

        Args:
            value ([type]): Value of model_res
        """
        self._model_res = value

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
