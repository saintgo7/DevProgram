package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Coupon struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var coupons = []{name}{}

func getAllCoupons(c *gin.Context) {
    c.JSON(http.StatusOK, coupons)
}

func getCouponByID(c *gin.Context) {
    id := c.Param("id")
    // Find Coupon by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Coupon"})
}

func createCoupon(c *gin.Context) {
    var newCoupon Coupon
    if err := c.BindJSON(&newCoupon); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    coupons = append(coupons, newCoupon)
    c.JSON(http.StatusCreated, newCoupon)
}

func updateCoupon(c *gin.Context) {
    id := c.Param("id")
    var updatedCoupon Coupon
    if err := c.BindJSON(&updatedCoupon); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCoupon)
}

func deleteCoupon(c *gin.Context) {
    id := c.Param("id")
    // Delete Coupon
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/coupon", getAllCoupons)
        api.GET("/coupon/:id", getCouponByID)
        api.POST("/coupon", createCoupon)
        api.PUT("/coupon/:id", updateCoupon)
        api.DELETE("/coupon/:id", deleteCoupon)
    }

    r.Run(":8080")
}
