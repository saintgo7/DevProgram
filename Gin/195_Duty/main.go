package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Duty struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var dutys = []{name}{}

func getAllDutys(c *gin.Context) {
    c.JSON(http.StatusOK, dutys)
}

func getDutyByID(c *gin.Context) {
    id := c.Param("id")
    // Find Duty by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Duty"})
}

func createDuty(c *gin.Context) {
    var newDuty Duty
    if err := c.BindJSON(&newDuty); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    dutys = append(dutys, newDuty)
    c.JSON(http.StatusCreated, newDuty)
}

func updateDuty(c *gin.Context) {
    id := c.Param("id")
    var updatedDuty Duty
    if err := c.BindJSON(&updatedDuty); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDuty)
}

func deleteDuty(c *gin.Context) {
    id := c.Param("id")
    // Delete Duty
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/duty", getAllDutys)
        api.GET("/duty/:id", getDutyByID)
        api.POST("/duty", createDuty)
        api.PUT("/duty/:id", updateDuty)
        api.DELETE("/duty/:id", deleteDuty)
    }

    r.Run(":8080")
}
