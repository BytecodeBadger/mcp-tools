from langchain_aws import ChatBedrockConverse

llm = ChatBedrockConverse(model_id="amazon.nova-pro-v1:0", region_name="us-east-1")

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)
