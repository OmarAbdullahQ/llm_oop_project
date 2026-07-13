class PricingPlan:
    def __init__(self, plan_name, price_per_1000_tokens):
        self.plan_name = plan_name
        self.price_per_1000_tokens = price_per_1000_tokens

    def calculate_cost(self, token_count):
        return (token_count / 1000) * self.price_per_1000_tokens