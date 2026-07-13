from PricingPlan import PricingPlan
from LanguageModel import GPTModel, LlamaModel
from ModelManager import ModelManager
from Conversation import Conversation
from Exceptions import InvalidPromptError

# Pricing Plan
pricing = PricingPlan(
    plan_name="Standard",
    price_per_1000_tokens=0.02
)

# Models
gpt = GPTModel(
    model_name="GPT-Model",
    provider="OpenAI",
    max_tokens=4096,
    temperature=0.7,
    api_key="secret-key",
    pricing_plan=pricing
)

llama = LlamaModel(
    model_name="Llama-Model",
    provider="Local",
    max_tokens=8192,
    temperature=0.5,
    model_path="/models/llama",
    quantization="4-bit",
    pricing_plan=pricing
)

# Model Manager
manager = ModelManager()
manager.add_model(gpt)
manager.add_model(llama)

print("Available Models:")
manager.list_models()

# Select Model
selected_model = manager.select_model("OpenAI", 3000)

if selected_model:
    print("\nSelected Model:")
    print(selected_model)

# Conversation
conversation = Conversation(
    conversation_id=1,
    model=gpt
)

# Test Prompts
prompts = [
    "Explain object-oriented programming.",
    "What is Python?",
    "Explain inheritance.",
    "",
    "    "
]

# Run Test
for prompt in prompts:
    try:
        conversation.send_message(prompt)
    except InvalidPromptError as error:
        print(error)

print("\nConversation History:")
conversation.display_history()