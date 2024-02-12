from flask import Flask, render_template, request, redirect, url_for
from weather import WeatherData 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Assuming validation always passes, redirect directly to the dashboard
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        api_code = request.form.get('apicode')
        zip_code = request.form.get('zipcode')
        country_code = request.form.get('countrycode')
        return updates(api_code, zip_code, country_code)

    return render_template('dashboard.html')

def updates(api_code, zip_code, country_code):
    # Instantiate WeatherData with provided values
    weather_data = WeatherData(api_key=api_code, zip_code=zip_code, country_code=country_code)
     # Attempt to get latitude and longitude
    lat_lon_response = weather_data.getLongLat()
    if not lat_lon_response['success']:
            # If getting coordinates fails, display the error message
        return render_template('dashboard.html', error=lat_lon_response['message'])
    
    
    # Fetch the weather data using the obtained coordinates
    weather_response = weather_data.getCurrentWeather()
    if not weather_response['success']:
            # If fetching weather data fails, display the error message
         return render_template('dashboard.html', error=weather_response['message'])

    # Construct a weather dictionary to pass to the template
    weather_info = {
            'main': weather_response['message'].get('main', 'N/A'),
            'description': weather_response['message'].get('description', 'N/A'),
            'icon': weather_response['message'].get('icon', '01d'),  # Default icon code
            'temperature': weather_response['message'].get('temperature', 'N/A')  
        } 
    return render_template('weather_display.html', weather=weather_info)

@app.route('/forgot')
def forgot_password():
    return 'Forgot Password Page'

@app.route('/signup')
def signup():
    return 'Sign Up Page'

if __name__ == '__main__':
    app.run(debug=True)