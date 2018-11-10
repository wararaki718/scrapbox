package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

type SAMPLE struct {
	id   int
	name string
}

func main() {
	connStr := "user=root password=password host=127.0.0.1 sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}

	rows, err := db.Query(`select * from samples`)
	if err != nil {
		log.Fatal(err)
	}
	// fmt.Print(rows)
	var sample SAMPLE
	for rows.Next() {
		rows.Scan(&sample.id, &sample.name)
		fmt.Print(sample)
	}

	defer db.Close()
}
