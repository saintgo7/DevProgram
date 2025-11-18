package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Form struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var forms = []{name}{}

func getAllForms(c *gin.Context) {
    c.JSON(http.StatusOK, forms)
}

func getFormByID(c *gin.Context) {
    id := c.Param("id")
    // Find Form by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Form"})
}

func createForm(c *gin.Context) {
    var newForm Form
    if err := c.BindJSON(&newForm); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    forms = append(forms, newForm)
    c.JSON(http.StatusCreated, newForm)
}

func updateForm(c *gin.Context) {
    id := c.Param("id")
    var updatedForm Form
    if err := c.BindJSON(&updatedForm); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedForm)
}

func deleteForm(c *gin.Context) {
    id := c.Param("id")
    // Delete Form
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/form", getAllForms)
        api.GET("/form/:id", getFormByID)
        api.POST("/form", createForm)
        api.PUT("/form/:id", updateForm)
        api.DELETE("/form/:id", deleteForm)
    }

    r.Run(":8080")
}
