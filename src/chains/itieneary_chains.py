from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from src.config.config import config

# Adding the llm using chatGroq

llm = ChatGroq(
    api_key=config.groq_api_key, model_name="llama-3.3-70b-versatile", temperature=0.3
)

# Prompt template for the itinerary chain
itnineary_prompt = ChatPromptTemplate(
    [
        (
            "system",
            "You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary",
        ),
        ("human", "Create a itineary for my day trip"),
    ]
)


# fucntion to get response from the llm.
def get_itineary(city: str, interests: list[str]) -> str:
    """
    Get an itinerary for a day trip to a given city based on user's interests.

    Args:
        city (str): The city to visit.
        interests (list(str)): A list of interests to include in the itinerary.

    Returns:
        str: A brief, bulleted itinerary for the day trip.
    """
    response = llm.invoke(
        itnineary_prompt.format_messages(city=city, interests=", ".join(interests))
    )

    return response.content


print(config.groq_api_key)
