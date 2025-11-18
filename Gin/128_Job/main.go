package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Job struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var jobs = []{name}{}

func getAllJobs(c *gin.Context) {
    c.JSON(http.StatusOK, jobs)
}

func getJobByID(c *gin.Context) {
    id := c.Param("id")
    // Find Job by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Job"})
}

func createJob(c *gin.Context) {
    var newJob Job
    if err := c.BindJSON(&newJob); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    jobs = append(jobs, newJob)
    c.JSON(http.StatusCreated, newJob)
}

func updateJob(c *gin.Context) {
    id := c.Param("id")
    var updatedJob Job
    if err := c.BindJSON(&updatedJob); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedJob)
}

func deleteJob(c *gin.Context) {
    id := c.Param("id")
    // Delete Job
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/job", getAllJobs)
        api.GET("/job/:id", getJobByID)
        api.POST("/job", createJob)
        api.PUT("/job/:id", updateJob)
        api.DELETE("/job/:id", deleteJob)
    }

    r.Run(":8080")
}
