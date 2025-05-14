# Test the use of the Model Context Protocol
## Notes
- AWS Bedrock Requires the environment variables From the AWS SSO Page be set in the CLI
- The OpenAI Interface was tested using the openweb-UI API bridge (the `.env` file needs to be setup with `OPENAI_API_KEY` set)
- The results using the Ollama self-hosted models were poor (the model had difficulty identifying tool usage). Only tested llama3.2:1b-instruct-q4_K_S and llama3-8b.