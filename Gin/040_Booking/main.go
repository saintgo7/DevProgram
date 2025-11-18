package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Booking struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var bookings = []{name}{}

func getAllBookings(c *gin.Context) {
    c.JSON(http.StatusOK, bookings)
}

func getBookingByID(c *gin.Context) {
    id := c.Param("id")
    // Find Booking by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Booking"})
}

func createBooking(c *gin.Context) {
    var newBooking Booking
    if err := c.BindJSON(&newBooking); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    bookings = append(bookings, newBooking)
    c.JSON(http.StatusCreated, newBooking)
}

func updateBooking(c *gin.Context) {
    id := c.Param("id")
    var updatedBooking Booking
    if err := c.BindJSON(&updatedBooking); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBooking)
}

func deleteBooking(c *gin.Context) {
    id := c.Param("id")
    // Delete Booking
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/booking", getAllBookings)
        api.GET("/booking/:id", getBookingByID)
        api.POST("/booking", createBooking)
        api.PUT("/booking/:id", updateBooking)
        api.DELETE("/booking/:id", deleteBooking)
    }

    r.Run(":8080")
}
