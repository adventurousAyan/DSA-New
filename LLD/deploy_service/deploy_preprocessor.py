from deploy_response import DeployResponse
from request_v2 import RequestV2
from model_response import ModelResponse
from nfs_deployer import NFSDeployer


class DeploymentPreprocessor:
    def __init__(self, parsed_list):
        self.parsed_list = parsed_list

    def validate(self, modeldata: RequestV2):
        if modeldata.client_id == "":
            return False

        if modeldata.product_name == "":
            return False

        if modeldata.model_path_type not in ["NFS", "ObjectStore", "Registry"]:
            return False

        else:
            return True

    def deploy(self):
        res = DeployResponse()
        modelreslist = []
        try:
            for modeldata in self.parsed_list:
                if not self.validate(modeldata):
                    res.status = "FAIL"
                    res.message = "Validation failed"
                    res.model_res = modelreslist
                    return res
                else:

                    if modeldata.model_path_type == "NFS":
                        storage_manager = NFSDeployer()
                        url = storage_manager.deploy(modeldata)
                        modelRes = ModelResponse()
                        modelRes.client_id = modeldata.client_id
                        modelRes.product_name = modeldata.product_name
                        modelRes.model_name = modeldata.model_name
                        modelRes.model_deploy_url = url
                        modelreslist.append(modelRes)

                res.model_res = modelreslist
                res.message = "Deployed successfully"
                res.status = "SUCCESS"

            return res
        except Exception as ex:
            res.message = str(ex)
            res.status = "FAIL"
            return res
