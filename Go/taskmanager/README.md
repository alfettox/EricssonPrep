# Task Manager Application in Go

## Project Description

This project is a command-line Task Manager Application written in the Go programming language. It allows users to manage their tasks efficiently. Tasks are represented by a structure that includes an ID, description, completion status, and optional due date. Users can add new tasks, list existing tasks, mark tasks as complete, and delete tasks.

## Project Structure

The project is organized in a single directory structure for simplicity. Here's an overview of the main components:

- `main.go`: This is the main entry point of the application where we interact with users and handle user input.
- `task.go`: This file defines the `Task` struct and contains related functions for tasks.
- User interface and interaction are handled directly within `main.go`.

## Task Struct

The `Task` struct is used to represent tasks in the application. It includes the following fields:

- `ID`: A unique identifier for each task.
- `Description`: A text description of the task.
- `Completed`: A boolean flag indicating whether the task is completed.
- `DueDate`: An optional field for specifying the due date of the task.

## Application Features

### 1. Add Task

To add a task, the user is prompted to enter a task description. The application automatically generates a unique ID for the task.

### 2. List Tasks

Users can list all existing tasks. Tasks are displayed along with their IDs, descriptions, due dates (if provided), and completion status.

### 3. Mark as Complete

Users can mark tasks as complete by specifying the task's ID. The application updates the completion status accordingly.

### 4. Delete Task

To delete a task, users provide the ID of the task they want to remove from the list. The application removes the task from the list.

### 5. Exit

The application can be terminated gracefully using the "Exit" option.

## Running the Application

To run the application, you'll need to have Go installed on your machine. Follow these steps:

1. Clone the repository to your local machine.

2. Open your terminal and navigate to the project directory.

3. Run the following command to start the application:

   ```shell
   go run main.go
You will be presented with a menu to interact with the Task Manager.
Conclusion
This Task Manager Application is a simple but functional example of a command-line application written in Go. It provides basic task management features and serves as a foundation for more complex applications.

