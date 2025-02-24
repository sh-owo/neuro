import asyncio
from logs.logger import get_logger
from AI.LM.mainLM import chat_mainlm


def main():
    logger = get_logger(__name__, log_file="agent", debug=True)
    logger.info("Starting agent...")
    while True:
        query = input("User: ")
        if query == "exit":
            break
        response = chat_mainlm(query)
        logger.info(f"Agent: {response}")
        print(f"Agent: {response}")


if __name__ == "__main__":
    main()