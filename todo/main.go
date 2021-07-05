package main

import (
	"log"
	"net/http"
	"text/template"
)
var tpl *template.Template
var err error
var tasks = []string{}
func init(){
	tpl, err = template.ParseFiles("todo.html")
	if err != nil{
		log.Fatal(err)
	}
}
func main() {
	helloHandler := func(w http.ResponseWriter, r *http.Request) {
		if(r.Method == http.MethodPost){
			task := r.FormValue("task")
			tasks = append(tasks, task)
		}
		tpl.ExecuteTemplate(w, "todo.html", tasks)
	}

	http.HandleFunc("/", helloHandler)
    log.Println("Listing for requests at http://localhost:8000")
	log.Fatal(http.ListenAndServe(":8000", nil))
}