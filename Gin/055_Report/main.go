package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Report struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var reports = []{name}{}

func getAllReports(c *gin.Context) {
    c.JSON(http.StatusOK, reports)
}

func getReportByID(c *gin.Context) {
    id := c.Param("id")
    // Find Report by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Report"})
}

func createReport(c *gin.Context) {
    var newReport Report
    if err := c.BindJSON(&newReport); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    reports = append(reports, newReport)
    c.JSON(http.StatusCreated, newReport)
}

func updateReport(c *gin.Context) {
    id := c.Param("id")
    var updatedReport Report
    if err := c.BindJSON(&updatedReport); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedReport)
}

func deleteReport(c *gin.Context) {
    id := c.Param("id")
    // Delete Report
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/report", getAllReports)
        api.GET("/report/:id", getReportByID)
        api.POST("/report", createReport)
        api.PUT("/report/:id", updateReport)
        api.DELETE("/report/:id", deleteReport)
    }

    r.Run(":8080")
}
