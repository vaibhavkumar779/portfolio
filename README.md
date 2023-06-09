# Flask Portfolio Website

This is a Flask-based portfolio website that allows visitors to view a portfolio, submit feedback, and generate a report of all visitor feedback.

* Note: At present the port is 5000.

## Features

- Display a portfolio page with resume information and a journey section.
- Accept visitor feedback through a form.
- Store visitor feedback in a CSV file.
- Provide a report page to view all visitor feedback.
- Count the total number of visitors.
- Retrieve visitor data including name, email, feedback, IP address, MAC address, visit time, time spent, and visited page.
- Implement styling using CSS to differentiate sections.
- Optimize the Flask application for production.

## Folder Structure

The folder structure of the project is as follows:

```shell
portfolio/
├── data
│   ├── feedback.csv
│   ├── journey.txt
│   ├── report_data.csv
│   └── resume.txt
├── LICENSE
├── logs
│   └── app.log
├── portfolio
│   ├── app.py
│   ├── __init__.py
│   ├── static
│   │   └── css
│   │       └── style.css
│   └── templates
│       ├── feedback.html
│       ├── portfolio.html
│       └── report.html
├── Procfile
├── README.md
├── requirements.txt
├── SetUpFlaskService.md
├── setup.py
├── test.ini
├── tests
│   ├── __init__.py
│   └── test_app.py
└── .env
```

- The `app.py` file contains the Flask application code and routes.
- The `static` folder holds static assets like CSS files.
- The `templates` folder contains HTML templates for the portfolio and report pages.
- The `reports` folder stores the generated report CSV file.
- The `data` folder includes data files such as feedback, resume, and journey text files.
- The `logs` folder is used for application logs.
- The `requirements.txt` file lists the required Python packages.
- The `Procfile` file specifies the command to run the application on a production server.
- The `.env` file is used for environment variables. Not here on github as .gitignore not allows only content was FLASK_DEBUG=development
- The `README.md` file provides information about the project.
- The `setup.py` file is used for packaging the application.

### structure redifined

```shell
   1. data/ (Directory):
        feedback.csv: Contains feedback data.
        journey.txt: Contains journey information.
        report_data.csv: Contains data for generating reports.
        resume.txt: Contains resume content.

   2. LICENSE:
        The license file for the project.

   3. logs/ (Directory):
        app.log: Log file for application logs.

   4. portfolio/ (Directory):
        app.py: Flask application code.
        init.py: Initialization file for the portfolio package.
        static/ (Directory): Directory for static files.
            css/ (Directory): Directory for CSS files.
                style.css: CSS file for styling the web pages.
        templates/ (Directory): Directory for HTML templates.
            feedback.html: HTML template for the feedback page.
            portfolio.html: HTML template for the portfolio page.
            report.html: HTML template for the report page.

   5. Procfile:
        Specifies the commands that are executed by the app on startup.

   6. README.md:
        Readme file containing project information and instructions.

   7. requirements.txt:
        Contains the list of required Python packages for the project.

   8. SetUpFlaskService.md:
        Instructions for setting up the Flask service.

   9. setup.py:
        Setup file for the project.

   10. test.ini:
        Configuration file for running tests.

   11. tests/ (Directory):
        init.py: Initialization file for the tests package.
        test_app.py: Test file for testing the Flask application.
```

## Installation and Usage

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```shell
   cd portfolio
   ```

3. Create and activate a virtual environment (optional):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the application:

   ```shell
   flask run
   ```
  
   The portfolio website will be accessible at <http://localhost:5000>.

6. Visit the portfolio page in your browser and explore the website.

7. To view the report, go to the /report route.

## Deployment

To deploy the Flask application, you can follow these steps:

1. Install a production WSGI server such as Gunicorn:

   ```shell
   pip install gunicorn
   ```

2. Use the provided gunicorn file to run the application:

   ```shell
   ./gunicorn
   ```

   The website will be available at `http://localhost:8000` or the specified host and port.

## Credits

This Flask portfolio website is developed by [Vaibhav Kumar](vaibhav.kr.779@gmail.com)

## Dependencies

The project uses several dependencies, which are listed in the `requirements.txt` file. Install them using the command `pip install -r requirements.txt`.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
