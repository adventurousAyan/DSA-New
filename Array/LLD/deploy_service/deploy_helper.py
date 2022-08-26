from deploy_preprocessor import DeploymentPreprocessor
from request_v2 import RequestV2


class DeployHelper:
    def __init__(self, model_data):
        self.model_data = model_data
        self.parsed_list = []

    def deploy_model(self):

        self.parse(self.model_data)
        self.preprocessor = DeploymentPreprocessor(self.parsed_list)
        return self.preprocessor.deploy()

    def parse(self, model_data_list):
        for model_data in model_data_list:
            req = RequestV2()
            req.client_id = model_data.get("client_id", "")
            req.model_name = model_data.get("model_name", "")
            req.model_path = model_data.get("model_path", "")
            req.model_path_type = model_data.get("model_path_type", "")
            req.model_type = model_data.get("model_type", "")
            req.product_name = model_data.get("product_name", "")
            self.parsed_list.append(req)
