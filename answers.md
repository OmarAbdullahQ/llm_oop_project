# OOP Project Questions & Answers Name: Omar Abdullah Al Qahtani

## 1. What is the difference between a class and an object?
**Answer:** A class is a blueprint. An object is an instance created from that class.

## 2. Why did we use LanguageModel as an abstract class?
**Answer:** To make sure every model implements the `generate_response()` method.

## 3. What is the purpose of `super()`?
**Answer:** To call the parent class constructor or methods.

## 4. What is the difference between inheritance and composition?
**Answer:** Inheritance means **is-a** relationship. Composition means **has-a** relationship.

## 5. What is the difference between composition and aggregation?
**Answer:** Composition means the objects depend on each other. Aggregation means they can exist independently.

## 6. Where does polymorphism appear in the project?
**Answer:** When `GPTModel` and `LlamaModel` override `generate_response()`.

## 7. What is the difference between a class attribute and an instance attribute?
**Answer:** A class attribute is shared by all objects. An instance attribute belongs to one object.

## 8. Why did we use `@property`?
**Answer:** To control access to private attributes.

## 9. When should we use a static method?
**Answer:** When the method does not use instance or class data.

## 10. When should we use a class method?
**Answer:** When the method works with class attributes.

## 11. Why did we override `generate_response()`?
**Answer:** So each model can have its own response behavior.

## 12. What is the purpose of `__str__` and `__repr__`?
**Answer:** `__str__` is for a user-friendly display. `__repr__` is for a developer-friendly representation.

## 13. Why did we create a custom exception?
**Answer:** To handle invalid prompts clearly.

## 14. What problem does `ModelManager` solve?
**Answer:** It manages multiple language models in one place.

## 15. How could this project be connected to a real API later?
**Answer:** By replacing the fake responses with real API requests, such as the OpenAI API.
