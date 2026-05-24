from mcp.server.fastmcp import FastMCP
import httpx

# Create your MCP server
mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    
    # Step 1: Get coordinates of the city
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    
    async with httpx.AsyncClient() as client:
        geo_response = await client.get(geocoding_url)
        geo_data = geo_response.json()
        
        if not geo_data.get("results"):
            return f"City '{city}' not found!"
        
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        name = location["name"]
        country = location["country"]
        
        # Step 2: Get weather using coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weathercode,windspeed_10m,relative_humidity_2m"
        
        weather_response = await client.get(weather_url)
        weather_data = weather_response.json()
        
        current = weather_data["current"]
        temp = current["temperature_2m"]
        wind = current["windspeed_10m"]
        humidity = current["relative_humidity_2m"]
        
        return f"""
🌍 Weather in {name}, {country}:
🌡️  Temperature: {temp}°C
💨 Wind Speed: {wind} km/h
💧 Humidity: {humidity}%
        """

if __name__ == "__main__":
    mcp.run()