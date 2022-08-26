from statistics import mode
from xml.parsers.expat import model
from abstract_deployer import AbstractDeployer
import shutil
import os

from request_v2 import RequestV2


class NFSDeployer(AbstractDeployer):
    def __init__(self):
        self.destpath = "destmodels"

    def deploy(self, modelData: RequestV2):

        try:

            files = os.listdir(modelData.model_path)
            print(files)

            shutil.copy(
                f"{modelData.model_path}/{modelData.model_name}",
                f"{self.destpath}/{modelData.model_name}",
            )

            return f"{self.destpath}/{modelData.model_name}"

        except Exception as ex:
            raise ex
