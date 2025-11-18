package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Appointment struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var appointments = []{name}{}

func getAllAppointments(c *gin.Context) {
    c.JSON(http.StatusOK, appointments)
}

func getAppointmentByID(c *gin.Context) {
    id := c.Param("id")
    // Find Appointment by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Appointment"})
}

func createAppointment(c *gin.Context) {
    var newAppointment Appointment
    if err := c.BindJSON(&newAppointment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    appointments = append(appointments, newAppointment)
    c.JSON(http.StatusCreated, newAppointment)
}

func updateAppointment(c *gin.Context) {
    id := c.Param("id")
    var updatedAppointment Appointment
    if err := c.BindJSON(&updatedAppointment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAppointment)
}

func deleteAppointment(c *gin.Context) {
    id := c.Param("id")
    // Delete Appointment
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/appointment", getAllAppointments)
        api.GET("/appointment/:id", getAppointmentByID)
        api.POST("/appointment", createAppointment)
        api.PUT("/appointment/:id", updateAppointment)
        api.DELETE("/appointment/:id", deleteAppointment)
    }

    r.Run(":8080")
}
