package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Join struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var joins = []{name}{}

func getAllJoins(c *gin.Context) {
    c.JSON(http.StatusOK, joins)
}

func getJoinByID(c *gin.Context) {
    id := c.Param("id")
    // Find Join by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Join"})
}

func createJoin(c *gin.Context) {
    var newJoin Join
    if err := c.BindJSON(&newJoin); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    joins = append(joins, newJoin)
    c.JSON(http.StatusCreated, newJoin)
}

func updateJoin(c *gin.Context) {
    id := c.Param("id")
    var updatedJoin Join
    if err := c.BindJSON(&updatedJoin); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedJoin)
}

func deleteJoin(c *gin.Context) {
    id := c.Param("id")
    // Delete Join
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/join", getAllJoins)
        api.GET("/join/:id", getJoinByID)
        api.POST("/join", createJoin)
        api.PUT("/join/:id", updateJoin)
        api.DELETE("/join/:id", deleteJoin)
    }

    r.Run(":8080")
}
