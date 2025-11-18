package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Audit struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var audits = []{name}{}

func getAllAudits(c *gin.Context) {
    c.JSON(http.StatusOK, audits)
}

func getAuditByID(c *gin.Context) {
    id := c.Param("id")
    // Find Audit by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Audit"})
}

func createAudit(c *gin.Context) {
    var newAudit Audit
    if err := c.BindJSON(&newAudit); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    audits = append(audits, newAudit)
    c.JSON(http.StatusCreated, newAudit)
}

func updateAudit(c *gin.Context) {
    id := c.Param("id")
    var updatedAudit Audit
    if err := c.BindJSON(&updatedAudit); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAudit)
}

func deleteAudit(c *gin.Context) {
    id := c.Param("id")
    // Delete Audit
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/audit", getAllAudits)
        api.GET("/audit/:id", getAuditByID)
        api.POST("/audit", createAudit)
        api.PUT("/audit/:id", updateAudit)
        api.DELETE("/audit/:id", deleteAudit)
    }

    r.Run(":8080")
}
