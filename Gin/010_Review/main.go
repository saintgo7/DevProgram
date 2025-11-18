package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Review struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var reviews = []{name}{}

func getAllReviews(c *gin.Context) {
    c.JSON(http.StatusOK, reviews)
}

func getReviewByID(c *gin.Context) {
    id := c.Param("id")
    // Find Review by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Review"})
}

func createReview(c *gin.Context) {
    var newReview Review
    if err := c.BindJSON(&newReview); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    reviews = append(reviews, newReview)
    c.JSON(http.StatusCreated, newReview)
}

func updateReview(c *gin.Context) {
    id := c.Param("id")
    var updatedReview Review
    if err := c.BindJSON(&updatedReview); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedReview)
}

func deleteReview(c *gin.Context) {
    id := c.Param("id")
    // Delete Review
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/review", getAllReviews)
        api.GET("/review/:id", getReviewByID)
        api.POST("/review", createReview)
        api.PUT("/review/:id", updateReview)
        api.DELETE("/review/:id", deleteReview)
    }

    r.Run(":8080")
}
