# Key Definitions and AI Concepts

## Frontier Model

Refers to a **state-of-the-art** model at the cutting edge of technology, essentially, one of the most advanced and powerful models available, ahead of typical models in terms of capabilities, architecture, or training data.

**Key points**

- Built using cutting-edge techniques, new architectures, or massive training datasets.

- Perform multiple types of tasks like language, vision, multimodal, etc. instead of being specialized.

- Often include the latest advances in safety, alignment, efficiency, and generalization.

**Examples**

- GPT-5 by OpenAI

- Claude by Anthropic


**Applications**

Used in research, new products, or experimental AI applications such as language synthesis, image generation, and complex data analysis. In short, calling a model means using a cutting-edge, advanced AI rather than a standard one.

## Messages and Role

When using OpenAI’s Chat API, inputs are structured as **messages**, which are objects containing a **role** and **content**. This format allows the model to understand context and respond appropriately.

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

# Three Ways to Use Models

There are three main ways to use modern AI models.

## Chat Interfaces

**Chat interfaces**, such as ChatGPT or similar conversational AI tools, provide the simplest way to use a model. 
Users interact with the system directly by typing questions or instructions and receiving responses in real time. 

This approach requires no programming skills and is ideal for everyday tasks like learning, generating ideas, writing content, solving problems, or exploring concepts quickly. 
Everything happens through a user-friendly interface so it is the most accessible entry point for interacting with AI models.

## Cloud APIs

**Cloud APIs** allow to integrate AI models into applications, workflows, or backend systems. 
By sending requests to a cloud-hosted model through an API, programs can process text, images, or other data and receive structured outputs.

This approach is widely used in production environments where automation, scaling, and reliability are important. 
Some libraries like **LangChain** make it easier to build complex AI applications, and managed services such as **Amazon Bedrock**, **Google Vertex**, and **Azure OpenAI** provide powerful infrastructure for deploying AI systems at scale. 
Cloud APIs are the best choice when building AI-driven products or automating large processes.


## Direct Inference

**Direct inference** refers to running models locally on your own hardware instead of using cloud services. 
It can load and execute models using libraries like **HuggingFace** **Transformers**, or run optimized local models through tools like **Ollama**.

This approach offers key advantages such as greater privacy, offline capability, and reduced long-term costs, since everything is processed on the user’s own device. 
However, it may require more technical setup and suitable hardware, especially for larger models. 
It is well suited for secure environments, experimentation, or situations where cloud access is limited or undesirable.