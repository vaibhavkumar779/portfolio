# Setting Up Flask Application as a Service

This guide will walk you through the steps to create a service file for running a Flask application continuously using systemd. This allows the application to start on system boot and run in the background.

## Prerequisites

- Flask application code
- Basic knowledge of the Linux command line
- `systemd` installed on your Linux distribution

## Steps

1. **Create a service file:**

   - Open a terminal.
   - Navigate to the `/etc/systemd/system/` directory.
   - Create a new service file with a `.service` extension, for example, `portfolio.service`.
   - Open the service file using a text editor.

2. **Define the service configuration:**

   - Add the following content to the service file:

     ```ini
     [Unit]
     Description=Portfolio Flask Application
     After=network.target

     [Service]
     User=<username>
     WorkingDirectory=/path/to/portfolio
     ExecStart=/path/to/venv/bin/python /path/to/portfolio/app.py
     Restart=always

     [Install]
     WantedBy=multi-user.target
     ```

     Make sure to replace `<username>` with your username and `/path/to/portfolio` with the actual path to your portfolio project directory.

3. **Save and close the service file.**

4. **Start the service:**

   - In the terminal, run the following command to start the service:

     ```shell
     sudo systemctl start portfolio
     ```

   - The Flask application will start running and will be accessible at the specified host and port (e.g., `http://localhost:5000`).

5. **Enable the service to run on system startup:**

   - Run the following command to enable the service:

     ```shell
     sudo systemctl enable portfolio
     ```

   - The service will now start automatically whenever the system boots.

6. **Verify the service status:**

   - To check the status of the service, run the following command:

     ```shell
     sudo systemctl status portfolio
     ```

   - You should see the status of the service, indicating whether it is running or not.

That's it! You have successfully set up your Flask application as a service using systemd. The application will now run continuously in the background and start on system boot.
