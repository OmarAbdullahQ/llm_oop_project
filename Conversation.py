class Conversation:
    def __init__(self, conversation_id, model):
        self.conversation_id = conversation_id
        self.model = model
        self.messages = []

    def send_message(self, prompt):
        response = self.model.generate_response(prompt)

        self.messages.append({
            "role": "user",
            "content": prompt
        })

        self.messages.append({
            "role": "assistant",
            "content": response
        })

    def display_history(self):
        for message in self.messages:
            print(f"{message['role']}: {message['content']}")