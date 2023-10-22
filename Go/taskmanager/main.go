package main

import (
	"bufio"
	"fmt"
	"os"
)

type Task struct {
	ID          int
	Description string
	Completed   bool
	DueDate     string
}

var tasks []Task
var lastID int

func main() {
	lastID = 0
	tasks = []Task{}

	for {
		fmt.Println("Task Manager")
		fmt.Println("1. Add Task")
		fmt.Println("2. List Tasks")
		fmt.Println("3. Mark as Complete")
		fmt.Println("4. Delete Task")
		fmt.Println("5. Exit")

		var choice int
		fmt.Print("Select an option: ")
		fmt.Scanln(&choice) // Consume newline character

		switch choice {
		case 1:
			addTask()
		case 2:
			listTasks()
		case 3:
			markAsComplete()
		case 4:
			deleteTask()
		case 5:
			fmt.Println("Goodbye!")
			return
		default:
			fmt.Println("Invalid choice. Please try again.")
		}
	}
}


func addTask() {
	fmt.Print("Enter task description: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	description := scanner.Text()
	lastID++
	task := Task{
		ID:          lastID,
		Description: description,
		Completed:   false,
		DueDate:     "",
	}
	tasks = append(tasks, task)
	fmt.Println("Task added successfully!")
}

func listTasks() {
	if len(tasks) == 0 {
		fmt.Println("No tasks to display.")
		return
	}

	fmt.Println("Tasks:")
	for _, task := range tasks {
		completedStatus := "Incomplete"
		if task.Completed {
			completedStatus = "Complete"
		}
		fmt.Printf("Task %d: %s (Due: %s, Status: %s)\n", task.ID, task.Description, task.DueDate, completedStatus)
	}
}

func markAsComplete() {
	listTasks()
	fmt.Print("Enter the task ID to mark as complete: ")
	var taskID int
	fmt.Scan(&taskID)

	for i, task := range tasks {
		if task.ID == taskID {
			tasks[i].Completed = true
			fmt.Printf("Task %d marked as complete!\n", taskID)
			return
		}
	}

	fmt.Println("Task not found.")
}

func deleteTask() {
	listTasks()
	fmt.Print("Enter the task ID to delete: ")
	var taskID int
	fmt.Scan(&taskID)

	for i, task := range tasks {
		if task.ID == taskID {
			tasks = append(tasks[:i], tasks[i+1:]...)
			fmt.Printf("Task %d deleted!\n", taskID)
			return
		}
	}

	fmt.Println("Task not found.")
}
