# Key Definitions and AI Concepts

## Frontier Model

Refers to a **state-of-the-art** model at the cutting edge of technology, essentially, one of the most advanced and powerful models available, ahead of typical models in terms of capabilities, architecture, or training data.

**Key points**

- Use cutting-edge techniques, new architectures, or much larger datasets than older models.

- Perform multiple types of tasks like language, vision, multimodal, etc. instead of being specialized.

**Examples**

- GPT-5 by OpenAI

- Claude by Anthropic


**Applications**

Used in research, new products, or experimental AI applications such as language synthesis, image generation, and complex data analysis.

In short, calling a model means it is top-tier, advanced, and at the forefront of AI development, rather than a standard or widely deployed model.

## Messages and Role

When using OpenAI’s Chat API, inputs are structured as messages, which are objects containing a role and content.

Large Language Models like ChatGPT are trained to process requests using a standardized prompt structure to ensure consistency and accuracy in their responses. 

**Roles Summary**

| Role        | Purpose                                                                              | Example Content                                                             |
|-------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `system`    | Instructions for defining task scope, context, model behavior, and response style    | `"You are a helpful AI assistant that explains AI concepts."`               |
| `user`      | Input provided by the user, primary content to respond to                            | `"Explain what a Frontier Model is in simple terms."`                       |
| `assistant` | Model's response, used to maintain conversation context or provide follow-up answers | `"A Frontier Model is a state-of-the-art AI system at the cutting edge..."` |

Clearly defining `system`, `user`, and `assistant` roles ensures the model understands context, maintains conversation flow, and provides accurate, relevant, and context-aware responses.

**Examples**

```python
messages = [
    {"role": "system", "content": "You are a helpful AI assistant that explains AI concepts."},
    {"role": "user", "content": "Explain what a Frontier Model is in simple terms."},
    {"role": "assistant", "content": "A Frontier Model is a state-of-the-art AI system at the cutting edge of technology..."}
]
```


This structure allows to understand the context and respond appropriately, maintaining the conversation flow.