class ModelManager:
    def __init__(self):
        self.models = {}

    def add_model(self, model):
        self.models[model.model_name] = model

    def remove_model(self, model_name):
        if model_name in self.models:
            del self.models[model_name]

    def get_model(self, model_name):
        return self.models.get(model_name)

    def list_models(self):
        for model_name in self.models:
            print(model_name)

    def select_model(self, provider, required_tokens):
        for model in self.models.values():
            if (
            model.provider == provider
            and model.max_tokens >= required_tokens
            and model.is_active
        ):
                return model

        return None