from src.config import configuration
from src.components.inference_eps import InferenceEps


class InferenceEpsPipeline:
    def __init__(self):
        self.config = configuration.ConfigurationManager()
        self.inference_config = self.config.get_inference_config()
        self.inference_eps = InferenceEps(self.inference_config)
    
    
    def ebd_ep(self, query):
        ebd = self.inference_eps.get_vector_ebd(query)
        return ebd

    def vs_ep(self, vector):
        data = self.inference_eps.vector_search(vector)
        return data        
