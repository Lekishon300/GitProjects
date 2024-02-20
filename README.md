## Weather App

## Overview
**The Weather App** is a Flask-based web application that provides current weather conditions using the OpenWeather API. 

It allows users to input a location and receive weather updates.

## Features
The application does the following:

* [✓] User Authentication: Secure login page with email and password fields.
* [✓] Form to enter OpenWeather API key, zip code, and country code.
* [✓] Error handling for incorrect API keys or unavailable weather data.
* [✓] Real-time weather display
* [✓] Weather icons to visually represent current conditions.

## App demo

## File Structure
* 'result.py': Main Flask application script with route definitions.
* 'weather.py': Python class for OpenWeather API interaction.
* 'login.html', 'dashboard.html', 'weather_display.html': HTML pages for the respective app sections.
* 'login.css', 'dashboard.css', 'weather_display.css': Styling for the HTML pages.

## Setup
* Obtain an API key from <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">OpenWeather</a> Obtain an API key
* Install dependencies: Flask.
* Run 'result.py' to start the server.

## Database ER Diagram

All ids are autogenerated

<img src='screenshots/Screenshot (257).png' title='Video Walkthrough' width='700' height='500' alt='Video Walkthrough' />

## Running the Project
To run app locally:

* 1. Clone the repository to your local machine.
* 2. Ensure Java is installed on your system.
* 3. Navigate to the project directory via terminal or command prompt.
* 4. Run the application using java main.App.
* 5. Follow the on-screen instructions to log in, browse products, and manage orders.

## Dependencies
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java Development Kit (JDK)</a>: Required to compile and run the Java application.
* <a href="https://www.oracle.com/mysql/what-is-mysql/" target="_blank">MySQL Database</a>: Utilized for storing and managing customer, product, and order data.
* <a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/" target="_blank">JDBC</a>: Java Database Connectivity for database interactions.
