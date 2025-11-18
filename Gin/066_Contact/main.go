package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Contact struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var contacts = []{name}{}

func getAllContacts(c *gin.Context) {
    c.JSON(http.StatusOK, contacts)
}

func getContactByID(c *gin.Context) {
    id := c.Param("id")
    // Find Contact by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Contact"})
}

func createContact(c *gin.Context) {
    var newContact Contact
    if err := c.BindJSON(&newContact); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    contacts = append(contacts, newContact)
    c.JSON(http.StatusCreated, newContact)
}

func updateContact(c *gin.Context) {
    id := c.Param("id")
    var updatedContact Contact
    if err := c.BindJSON(&updatedContact); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedContact)
}

func deleteContact(c *gin.Context) {
    id := c.Param("id")
    // Delete Contact
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/contact", getAllContacts)
        api.GET("/contact/:id", getContactByID)
        api.POST("/contact", createContact)
        api.PUT("/contact/:id", updateContact)
        api.DELETE("/contact/:id", deleteContact)
    }

    r.Run(":8080")
}
