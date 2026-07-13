from abc import ABC, abstractmethod
from Tokenizer import Tokenizer
from PricingPlan import PricingPlan
from Exceptions import InvalidPromptError


class LanguageModel(ABC):
    total_models = 0

    @classmethod
    def get_total_models(cls):
        return cls.total_models

    def __init__(self, model_name,provider,max_tokens,temperature,pricing_plan):
        self.model_name = model_name
        self.provider = provider
        self.max_tokens = max_tokens
        self.__temperature = temperature
        LanguageModel.total_models+= 1
        self.tokenizer = Tokenizer()
        self.pricing_plan = pricing_plan
        self.__is_active = True



    @abstractmethod
    def generate_response(self,prompt):
        pass

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if self.validate_temperature(value) == True:
            self.__temperature = value
        else:
            print("the value must be between 0 and 2 stuped")

    def display_info(self):
        print("Model info as follows")
        print("Model name: ",self.model_name)
        print("The provider is: ", self.provider)
        print("The maximum tokens is: ", self.max_tokens)
        print("The temprature is: ", self.temperature)

    @staticmethod
    def validate_temperature(number):
        if number <= 2 and number >= 0:
            return True
        else:
            return False
        
    def calculate_request_cost(self,prompt):
        token_count = self.tokenizer.count_tokens(prompt)
        cost = self.pricing_plan.calculate_cost(token_count)
        print("Number of tokens:", token_count)
        print("The cost is: ",cost)

    def __str__(self):
        return f"{self.model_name} by {self.provider}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(model_name='{self.model_name}', provider='{self.provider}')"


    def __len__(self):
        return self.max_tokens
    

    def __eq__(self, other):
        return (
        self.model_name == other.model_name
        and self.provider == other.provider
        )
    
    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        self.__is_active = value
    

class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class GPTModel(LanguageModel,LoggingMixin):
    def __init__(self,model_name,provider,max_tokens,temperature,api_key,pricing_plan):
        super().__init__(model_name,provider,max_tokens,temperature,pricing_plan)
        self.api_key = api_key

    def generate_response(self, prompt):
        if not isinstance(prompt, str):
            raise InvalidPromptError("Prompt must be a string.")
        
        if prompt.strip() == "":
            raise InvalidPromptError("Prompt cannot be empty.")

        self.log(f"Sending request to {self.model_name}")
        self.calculate_request_cost(prompt)

        return "GPT API response to: " + prompt
    
    

    

class LlamaModel(LanguageModel,LoggingMixin):
    def __init__(self,model_name,provider,max_tokens,temperature,model_path,quantization,pricing_plan):
        super().__init__(model_name,provider,max_tokens,temperature,pricing_plan)
        self.model_path = model_path
        self.quantization = quantization

    def generate_response(self, prompt):
        if not isinstance(prompt, str):
            raise InvalidPromptError("Prompt must be a string.")
        
        if prompt.strip() == "":
            raise InvalidPromptError("Prompt cannot be empty.")

        self.log(f"Sending request to {self.model_name}")
        self.calculate_request_cost(prompt)

        return "Llama API response to: " + prompt
    
    
    

if __name__ == "__main__":
    

 pricing = PricingPlan("Standard", 0.02)
 gpt = GPTModel("GPT", "OpenAI",5,1.5,"jjjfjj88574",pricing)
 llama = LlamaModel("Llama", "Meta",505,1.2, "data/models", "4 bit",pricing)
 
 models = [gpt,llama]
 
 for model in models:
     print(model.generate_response("What is the computer made of"))
 
 try:
     print(gpt.generate_response(""))
 except InvalidPromptError as error:
     print(error)