import math
import datetime
import pytz
import requests

def calculator_tool(expression: str) -> str:
    """
    Safely evaluate mathematical expressions.
    Args:
        expression: Math expression like "2 + 3 * 4" or "math.sqrt(16)"
    Returns:
        String with the calculation result
    """
    try:
        # Allow only safe math functions
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"


def get_current_time(timezone: str = "UTC") -> str:
    """
    Get current time in specified timezone.
    Args:
        timezone: Timezone string like "UTC", "US/Eastern", "Asia/Tokyo"
    Returns:
        Formatted time string with timezone info
    """
    try:
        tz = pytz.timezone(timezone)
    except Exception:
        return f"Invalid timezone: {timezone}"
    now = datetime.datetime.now(tz)
    return now.strftime(f"%Y-%m-%d %H:%M:%S {timezone}")


def web_search(query: str, num_results: int = 3) -> str:
    """
    Search the web and return top results using DuckDuckGo.
    Args:
        query: Search terms
        num_results: Number of results to return (1-5)
    Returns:
        Formatted string with search results
    """
    try:
        url = "https://api.duckduckgo.com"
        params = {"q": query, "format": "json"}
        response = requests.get(url, params=params)
        data = response.json()
        results = []
        for topic in data.get("RelatedTopics", [])[:num_results]:
            if "Text" in topic and "FirstURL" in topic:
                results.append(f"{topic['Text']} - {topic['FirstURL']}")
        return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"


# Test each tool individually
if __name__ == "__main__":
    print(calculator_tool("2 + 3 * 4"))
    print(get_current_time("Asia/Tokyo"))
    print(web_search("Search for AI"))
