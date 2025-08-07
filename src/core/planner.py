from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itieneary_chains import get_itineary
from loguru import logger


class TravelAgent:
    """
    A travel agent that can plan a day trip to a given city based on user's interests.
    """

    def __init__(self):
        """
        Initialize the travel agent.
        """
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""

        logger.info("TravelAgent initialized...")

    # Getting city from the user.
    def set_city(self, city: str):
        """
        Set the city for the travel agent.
        """
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info(f"City set to {city}")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise e

    # Getting interests from the user.
    def set_interest(self, interests: str):
        """
        Set the interests for the travel agent.
        """
        try:
            self.interests = [i.strip() for i in interests.split(",")]
            self.messages.append(HumanMessage(content=interests))
            logger.info(f"Interests set to {interests}")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise e

    # Generating the itineary for the day trip.
    def create_itineary(self):
        """
        Get the itineary for the travel agent.
        """

        try:
            logger.info(
                f" Generating itineary for {self.city} with interests {self.interests}"
            )
            itineary = get_itineary(self.city, self.interests)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info(f"Itineary generated: {itineary}")
            return itineary

        except Exception as e:
            logger.error(f"Error generating itineary: {e}")
            raise e
