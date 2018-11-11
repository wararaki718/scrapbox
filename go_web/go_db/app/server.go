package main

import (
	"database/sql"
	"log"
	"net/http"

	_ "github.com/lib/pq"

	"github.com/labstack/echo"
)

type SAMPLE struct {
	id   int
	name string
}

func get_msg() SAMPLE {
	connStr := "user=root password=password host=postgres port=5432 sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	rows, err := db.Query(`select * from samples`)
	if err != nil {
		log.Fatal(err)
	}
	var sample SAMPLE
	for rows.Next() {
		rows.Scan(&sample.id, &sample.name)
		log.Print(sample)
	}
	defer db.Close()

	return sample
}

func main() {
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		var msg = get_msg()
		return c.String(http.StatusOK, msg.name)
	})
	e.Logger.Fatal(e.Start(":1323"))
}
