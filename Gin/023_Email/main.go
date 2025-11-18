package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Email struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var emails = []{name}{}

func getAllEmails(c *gin.Context) {
    c.JSON(http.StatusOK, emails)
}

func getEmailByID(c *gin.Context) {
    id := c.Param("id")
    // Find Email by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Email"})
}

func createEmail(c *gin.Context) {
    var newEmail Email
    if err := c.BindJSON(&newEmail); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    emails = append(emails, newEmail)
    c.JSON(http.StatusCreated, newEmail)
}

func updateEmail(c *gin.Context) {
    id := c.Param("id")
    var updatedEmail Email
    if err := c.BindJSON(&updatedEmail); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedEmail)
}

func deleteEmail(c *gin.Context) {
    id := c.Param("id")
    // Delete Email
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/email", getAllEmails)
        api.GET("/email/:id", getEmailByID)
        api.POST("/email", createEmail)
        api.PUT("/email/:id", updateEmail)
        api.DELETE("/email/:id", deleteEmail)
    }

    r.Run(":8080")
}
