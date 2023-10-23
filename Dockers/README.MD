# Dockerized Web Application with Ubuntu and Nginx

This project demonstrates how to create a Docker container with Ubuntu and Nginx to host a simple web application.

## Prerequisites

- Docker installed on your Windows machine.
- Basic knowledge of Docker.

## Setup

To set up the Docker container using Ubuntu and Nginx on your Windows machine, you have two options: using the Windows Subsystem for Linux (WSL) or using Windows Docker Desktop.

### Using Windows Subsystem for Linux (WSL)

1. **Install WSL**:

   - Open PowerShell as an administrator.
   - Run the following command to enable the WSL feature:
     ```powershell
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     ```

   - Install a Linux distribution (e.g., Ubuntu) from the Microsoft Store. You can search for "Ubuntu" and install it.

2. **Configure WSL**:

   - After installation, launch the Ubuntu distribution.
   - Follow the setup instructions, including creating a user and setting a password.

3. **Install Docker**:

   - In the WSL Ubuntu terminal, run the following commands to install Docker:
     ```bash
     sudo apt update
     sudo apt install docker.io
     ```

4. **Set Up the Docker Container**:

   - Now, you can follow the previous guide starting from "Create a Dockerfile" and complete the setup steps.

### Using Windows Docker Desktop

1. **Install Docker Desktop**:

   - Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop).

2. **Open Docker Desktop**:

   - Once installed, open Docker Desktop.

3. **Configure WSL 2 Backend (Optional)**:

   - Docker Desktop can use WSL 2 as a backend to improve performance. You can configure this by going to Docker Desktop settings and enabling WSL 2 integration.

4. **Create a Dockerfile and HTML File**:

   - Create a `Dockerfile` and an `index.html` file as described in the guide above.

5. **Build and Run the Docker Container**:

   - Use PowerShell to navigate to the directory containing your Dockerfile and HTML file.
   - Build the Docker image:
     ```powershell
     docker build -t web-app .
     ```
   - Run the Docker container:
     ```powershell
     docker run -d -p 80:80 web-app
     ```

6. **Access the Web Application**:

   - Open a web browser on your Windows machine and go to [http://localhost](http://localhost) to access the web application.
