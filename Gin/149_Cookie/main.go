package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Cookie struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var cookies = []{name}{}

func getAllCookies(c *gin.Context) {
    c.JSON(http.StatusOK, cookies)
}

func getCookieByID(c *gin.Context) {
    id := c.Param("id")
    // Find Cookie by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Cookie"})
}

func createCookie(c *gin.Context) {
    var newCookie Cookie
    if err := c.BindJSON(&newCookie); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    cookies = append(cookies, newCookie)
    c.JSON(http.StatusCreated, newCookie)
}

func updateCookie(c *gin.Context) {
    id := c.Param("id")
    var updatedCookie Cookie
    if err := c.BindJSON(&updatedCookie); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCookie)
}

func deleteCookie(c *gin.Context) {
    id := c.Param("id")
    // Delete Cookie
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/cookie", getAllCookies)
        api.GET("/cookie/:id", getCookieByID)
        api.POST("/cookie", createCookie)
        api.PUT("/cookie/:id", updateCookie)
        api.DELETE("/cookie/:id", deleteCookie)
    }

    r.Run(":8080")
}
