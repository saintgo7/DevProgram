package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type JWT struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var jwts = []{name}{}

func getAllJWTs(c *gin.Context) {
    c.JSON(http.StatusOK, jwts)
}

func getJWTByID(c *gin.Context) {
    id := c.Param("id")
    // Find JWT by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "JWT"})
}

func createJWT(c *gin.Context) {
    var newJWT JWT
    if err := c.BindJSON(&newJWT); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    jwts = append(jwts, newJWT)
    c.JSON(http.StatusCreated, newJWT)
}

func updateJWT(c *gin.Context) {
    id := c.Param("id")
    var updatedJWT JWT
    if err := c.BindJSON(&updatedJWT); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedJWT)
}

func deleteJWT(c *gin.Context) {
    id := c.Param("id")
    // Delete JWT
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/jwt", getAllJWTs)
        api.GET("/jwt/:id", getJWTByID)
        api.POST("/jwt", createJWT)
        api.PUT("/jwt/:id", updateJWT)
        api.DELETE("/jwt/:id", deleteJWT)
    }

    r.Run(":8080")
}
