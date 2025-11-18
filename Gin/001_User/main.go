package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type User struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var users = []{name}{}

func getAllUsers(c *gin.Context) {
    c.JSON(http.StatusOK, users)
}

func getUserByID(c *gin.Context) {
    id := c.Param("id")
    // Find User by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "User"})
}

func createUser(c *gin.Context) {
    var newUser User
    if err := c.BindJSON(&newUser); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    users = append(users, newUser)
    c.JSON(http.StatusCreated, newUser)
}

func updateUser(c *gin.Context) {
    id := c.Param("id")
    var updatedUser User
    if err := c.BindJSON(&updatedUser); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedUser)
}

func deleteUser(c *gin.Context) {
    id := c.Param("id")
    // Delete User
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/user", getAllUsers)
        api.GET("/user/:id", getUserByID)
        api.POST("/user", createUser)
        api.PUT("/user/:id", updateUser)
        api.DELETE("/user/:id", deleteUser)
    }

    r.Run(":8080")
}
