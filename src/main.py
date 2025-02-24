import asyncio
from logs.logger import setup_logger


async def main():
    logger = await setup_logger(__name__, log_file="agent")
    logger.info("Starting agent...")
    logger.warning("ahhhhhh")
    logger.debug("debugging")
    logger.error("error")

if __name__ == "__main__":
    asyncio.run(main())