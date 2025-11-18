package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Task struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var tasks = []{name}{}

func getAllTasks(c *gin.Context) {
    c.JSON(http.StatusOK, tasks)
}

func getTaskByID(c *gin.Context) {
    id := c.Param("id")
    // Find Task by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Task"})
}

func createTask(c *gin.Context) {
    var newTask Task
    if err := c.BindJSON(&newTask); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    tasks = append(tasks, newTask)
    c.JSON(http.StatusCreated, newTask)
}

func updateTask(c *gin.Context) {
    id := c.Param("id")
    var updatedTask Task
    if err := c.BindJSON(&updatedTask); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTask)
}

func deleteTask(c *gin.Context) {
    id := c.Param("id")
    // Delete Task
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/task", getAllTasks)
        api.GET("/task/:id", getTaskByID)
        api.POST("/task", createTask)
        api.PUT("/task/:id", updateTask)
        api.DELETE("/task/:id", deleteTask)
    }

    r.Run(":8080")
}
