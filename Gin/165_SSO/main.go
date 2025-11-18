package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type SSO struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var ssos = []{name}{}

func getAllSSOs(c *gin.Context) {
    c.JSON(http.StatusOK, ssos)
}

func getSSOByID(c *gin.Context) {
    id := c.Param("id")
    // Find SSO by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "SSO"})
}

func createSSO(c *gin.Context) {
    var newSSO SSO
    if err := c.BindJSON(&newSSO); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    ssos = append(ssos, newSSO)
    c.JSON(http.StatusCreated, newSSO)
}

func updateSSO(c *gin.Context) {
    id := c.Param("id")
    var updatedSSO SSO
    if err := c.BindJSON(&updatedSSO); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSSO)
}

func deleteSSO(c *gin.Context) {
    id := c.Param("id")
    // Delete SSO
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/sso", getAllSSOs)
        api.GET("/sso/:id", getSSOByID)
        api.POST("/sso", createSSO)
        api.PUT("/sso/:id", updateSSO)
        api.DELETE("/sso/:id", deleteSSO)
    }

    r.Run(":8080")
}
