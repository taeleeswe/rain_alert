# Weather Alert Application

This Weather Alert Application checks the weather forecast for the next 12 hours and sends an SMS alert if it is going to rain. The application uses the OpenWeather API to get weather data and the Twilio API to send SMS notifications.

## Features
- **Weather Forecast Check**: Retrieves the weather forecast for the next 12 hours.
- **Rain Alert**: Sends an SMS alert if rain is predicted within the next 12 hours.

## How to Use
1. **Set Environment Variables**: Ensure that the required API keys and tokens are set in your environment variables.
2. **Run the Application**: Execute the script to check the weather and send an SMS alert if rain is predicted.

## Installation
### Prerequisites
- Python 3.12
- Requests library
- Twilio library
- OpenWeather API key
- Twilio Account SID and Auth Token

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-alert-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd weather-alert-app
    ```
3. Install the required packages:
    ```sh
    pip install requests twilio
    ```
4. Set up your environment variables:
    - `OWN_API_KEY`: Your OpenWeather API key.
    - `ACCOUNT_SID`: Your Twilio Account SID.
    - `OWN_AUTH_TOKEN`: Your Twilio Auth Token.

    You can set these variables in your terminal or in a `.env` file:
    ```sh
    export OWN_API_KEY="your_openweather_api_key"
    export ACCOUNT_SID="your_twilio_account_sid"
    export OWN_AUTH_TOKEN="your_twilio_auth_token"
    ```

5. Run the application:
    ```sh
    python main.py
    ```
