package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Phone struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var phones = []{name}{}

func getAllPhones(c *gin.Context) {
    c.JSON(http.StatusOK, phones)
}

func getPhoneByID(c *gin.Context) {
    id := c.Param("id")
    // Find Phone by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Phone"})
}

func createPhone(c *gin.Context) {
    var newPhone Phone
    if err := c.BindJSON(&newPhone); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    phones = append(phones, newPhone)
    c.JSON(http.StatusCreated, newPhone)
}

func updatePhone(c *gin.Context) {
    id := c.Param("id")
    var updatedPhone Phone
    if err := c.BindJSON(&updatedPhone); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPhone)
}

func deletePhone(c *gin.Context) {
    id := c.Param("id")
    // Delete Phone
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/phone", getAllPhones)
        api.GET("/phone/:id", getPhoneByID)
        api.POST("/phone", createPhone)
        api.PUT("/phone/:id", updatePhone)
        api.DELETE("/phone/:id", deletePhone)
    }

    r.Run(":8080")
}
