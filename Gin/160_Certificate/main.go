package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Certificate struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var certificates = []{name}{}

func getAllCertificates(c *gin.Context) {
    c.JSON(http.StatusOK, certificates)
}

func getCertificateByID(c *gin.Context) {
    id := c.Param("id")
    // Find Certificate by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Certificate"})
}

func createCertificate(c *gin.Context) {
    var newCertificate Certificate
    if err := c.BindJSON(&newCertificate); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    certificates = append(certificates, newCertificate)
    c.JSON(http.StatusCreated, newCertificate)
}

func updateCertificate(c *gin.Context) {
    id := c.Param("id")
    var updatedCertificate Certificate
    if err := c.BindJSON(&updatedCertificate); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCertificate)
}

func deleteCertificate(c *gin.Context) {
    id := c.Param("id")
    // Delete Certificate
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/certificate", getAllCertificates)
        api.GET("/certificate/:id", getCertificateByID)
        api.POST("/certificate", createCertificate)
        api.PUT("/certificate/:id", updateCertificate)
        api.DELETE("/certificate/:id", deleteCertificate)
    }

    r.Run(":8080")
}
