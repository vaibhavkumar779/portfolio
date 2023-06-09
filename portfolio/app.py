import os
import csv
import datetime
import psutil
import logging
from flask import Flask, render_template, request
from dotenv import load_dotenv

# app = Flask(__name__, template_folder='portfolio/templates')
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO)


# Define the path to the data directory
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')

# Define the path to the report CSV file
REPORT_FILE = os.path.join(DATA_DIR, 'report_data.csv')

# Define the path to the feedback CSV file
FEEDBACK_FILE = os.path.join(DATA_DIR, 'feedback.csv')

# Function to save visitor feedback
def save_feedback(name, email, feedback, ip_address):
    with open(FEEDBACK_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, feedback, ip_address])


# Function to read data from a file
def read_file(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as file:
        return file.read()

# Function to get the total number of visitors
def get_total_visitors():
    try:
        with open(REPORT_FILE, 'r') as file:
            reader = csv.reader(file)
            return sum(1 for _ in reader) - 1  # Subtract 1 to exclude the header row
    except FileNotFoundError:
        return 0

# Function to get the list of all visitors
def get_visitors():
    visitors = []
    try:
        with open(FEEDBACK_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                visitors.append({
                    'ip_address': row[0],
                    'mac_address': row[1],
                    'visit_time': row[2],
                    'time_spent': row[3],
                    'visited_page': row[4]
                })
    except FileNotFoundError:
        pass
    return visitors

# Function to get the list of all visitors
def get_visitors_feedback():
    visitors_feedbacks = []
    try:
        with open(FEEDBACK_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                visitors_feedbacks.append({
                    'name': row[0],
                    'email': row[1],
                    'feedback': row[2],
                    'ip_address':row[3]
                })
    except FileNotFoundError:
        pass
    return visitors_feedbacks

# Function to get the MAC address
def get_mac_address():
    try:
        # Get the MAC address of the first network interface
        mac_address = ':'.join(['{:02X}'.format((psutil.net_if_addresses()[interface][0].address.split(':'))[i])
                                for interface in psutil.net_if_addresses() if interface != 'lo'
                                for i in range(6)])
        return mac_address
    except:
        return 'Unknown'

# Function to calculate time spent
def calculate_time_spent(start_time):
    end_time = datetime.datetime.now()
    time_spent = end_time - start_time
    return str(time_spent)

#Directly Save Visitors Data
with open(REPORT_FILE, 'a', newline='') as file:
    ip_address = request.remote_addr
    mac_address = get_mac_address()
    visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time_spent = calculate_time_spent(app.start_time)
    visited_page = request.url
    writer = csv.writer(file)
    writer.writerow([ip_address,mac_address,visit_time,time_spent,visited_page])


# Route for the portfolio page
@app.route('/')
def portfolio():
    try:
        resume_data = read_file('resume.txt')
        journey_data = read_file('journey.txt')
        return render_template('portfolio.html', resume_data=resume_data, journey_data=journey_data)
    except Exception as e:
        logging.exception('Error occurred while rendering portfolio page: %s', str(e))
        return 'An error occurred. Please try again later.', 500

# Route for submitting and seeing feedback
@app.route('/feedback', methods=['POST', "GET"])
def submit_feedback():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            feedback = request.form.get('feedback')
            ip_address = request.remote_addr
            mac_address = get_mac_address()
            visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time_spent = calculate_time_spent(app.start_time)
            visited_page = request.url

            save_feedback(name, email, feedback, ip_address, mac_address, visit_time, time_spent, visited_page)
            return 'Thank you for your feedback!'
        except Exception as e:
            logging.exception('Error occurred while submitting feedback: %s', str(e))
            return 'An error occurred. Please try again later.', 500
    elif request.method == "GET":
        try:
            total_visitors = get_total_visitors()
            visitors_feedbacks = get_visitors_feedback()
            return render_template('feedback.html', total_visitors=total_visitors, visitors_feedbacks=visitors_feedbacks)
        except Exception as e:
            logging.exception('Error occurred while rendering feedback page: %s', str(e))
            return 'An error occurred. Please try again later.', 500

# Route for the report page
@app.route('/report')
def report():
    try:
        total_visitors = get_total_visitors()
        visitors = get_visitors()
        return render_template('report.html', total_visitors=total_visitors, visitors=visitors)
    except Exception as e:
        logging.exception('Error occurred while rendering reports page: %s', str(e))
        return 'An error occurred. Please try again later.', 500


if __name__ == '__main__':
    app.start_time = datetime.datetime.now()
    app.run(host='0.0.0.0', port=5000, debug=True)