package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type OAuth struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var oauths = []{name}{}

func getAllOAuths(c *gin.Context) {
    c.JSON(http.StatusOK, oauths)
}

func getOAuthByID(c *gin.Context) {
    id := c.Param("id")
    // Find OAuth by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "OAuth"})
}

func createOAuth(c *gin.Context) {
    var newOAuth OAuth
    if err := c.BindJSON(&newOAuth); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    oauths = append(oauths, newOAuth)
    c.JSON(http.StatusCreated, newOAuth)
}

func updateOAuth(c *gin.Context) {
    id := c.Param("id")
    var updatedOAuth OAuth
    if err := c.BindJSON(&updatedOAuth); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedOAuth)
}

func deleteOAuth(c *gin.Context) {
    id := c.Param("id")
    // Delete OAuth
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/oauth", getAllOAuths)
        api.GET("/oauth/:id", getOAuthByID)
        api.POST("/oauth", createOAuth)
        api.PUT("/oauth/:id", updateOAuth)
        api.DELETE("/oauth/:id", deleteOAuth)
    }

    r.Run(":8080")
}
