/////////// CLI

///////// COMMON PACKAGES
"fmt":
	fmt.Prinln("Hello %s", world) // Println("hello ", world)
"time":
	time.Now()
"math"
	math.rand.Intn(10)
	math.Sqrt(7)
"runtime":
	rutime.GOOS
"net/http"

//////// EXPORTS and IMPORTS
package main
import (
	"fmt"
	"math/rand"
)

math.Pi // Pi starts with capital letter = export

////////// BASICS
bool string int uint byte rune float32 float uintptr 64 complex64 complex128 int8-64 uint8-64 // TYPES
fmt.Printf("Type %T, value %v", a, a) // Print type %T value %v
var x int = int(3.5) // CAST

const Pi = 3.14
var a int, b, c bool // declare and type
var a, b = 1, false
i, j := 1,2 // declare and assign

var p *int // POINTERS
p := &i //points to address i
j = *p  // j copies the value on pointer p, which is same as i

func add(x int, y int) int { return x + y }
func add(x, y int) int {...}
funct swap(x, y string) (string, string){ return y, x }
a, b := swap("hello", "world")

func split(sum int) (x, y int){ // x, y = named return, same as def inside split
	x = sum * 2
	y = sum - x
	return //naked return
}

func withDefer(){
	defer fmt.Println("world") // push execution to stack at end of scope, LIFO
	fmt.Println("hello") // prints hello world
}

f := func(x, y int) int {...}
func composedFunc(sum int, f func(int, int) int) int {...}

for i := 0; i < 10; i++ { sum += i} // FOR
for sum < 10 {} // WHILE
for {} // INFINITE
for i, v := range mySlice {} // ITERATE on SLICE
for _, v := range mySlice {}

if x < 10 {} else {}
if v := math.Pow(x, n); v < lim {return v} // v scooped until end if

switch os := runtime.GOOS; os {
case "darwin":
	fmt.Println("bla")
default:
	fmt.Println("blo")
}

switch { // SWITCH without condition, for long if's chains
case t.Hour() < 12:
case t.Hour() < 17:
default:
}

type Vertex struct { // STRUCTS, CLASSES
	X int
	Y int
}

func (v Vertex) Sum() float64{ // ADD method to class
	return v.X + v.Y
}

func (v *Vertex) Modify() {
	v.X = 5
}

type MyFloat float64
funct (f MyFloat) Abs() float64 {...}

type Abser interface{ // if a type have Abs(), then it's an Abser
	Abs() float64
}

var I interface{} // to handle values of unknown type, old any type
s, ok := iname.(string) // type assertion, name is a string interface

switch v := i.(type){
case S:
default:
}

v1 := Vertex{1, 2}
v2 := Vertex{Y:1}
v3 := Vertex{}
p  := &Vertext{1, 2}
p.X // instead of (*p).X, shortcut on the lang

var names [10] string // ARRAY of 10 strings
names[0] = "Max"
primes := [4]int {2, 3, 5, 7} // CAN'T RESIZE ARRAYS
var s []int = primes[1:3] // slice of [1:3) -> 3, 5
r := []bool{true, false, false} // r[:] r[0:]

len(s) //num of elements in the slice
cap(s) // num of elements in primes counting from primes[1], max size allocated

mySlice := make([]int, 1, 5) // len 1, cap 5
func append(s []T, vs ...T) []T // append to the end of the slice
s = append(s, 2, 3, 4)

var myMap[string]Vertex
myOtherMap = make(map[string]Vertext)
myMap["Uruguay"] = Vertext{1, -1}

var mapLiteral = map[string]Vertext{
	"Uwuguay": Vertex{1, 1},
	"Uruguay": Vertext{-1, 1},
}

delete(mapLiteral, "Uwuguay")
elem, ok := m["Uruguay"] // Vertext{-1, 1}, true

//////////// GENERICS
func Index[T comparable](s []T, x T) int // T is a GENERIC, comparable == and !=
type List[T any] struct {
	next *List[T]
	val T
}

/////////// GO ROUTINES: lightweight thread managed by the runtime
go f(x, y, z) // goroutines shared same address space/ syncronize memory access
f(x, y, z) // x, y, z evaluated in current goroutine, f executed in new goroutine

func say(s: string){
	time.Sleep(100 * time.Millisecond)
	fmt.Println(s)
}

func main(){
	go say("world")
	say("hello")
}

/////////// CHANNELS: used to sync goroutines without explicit locks
ch := make(chan int) // create channel
ch <- v // send value v to channel ch
v := <- ch // receive on v the contents of the channel v

func sum(s []int, c chan int){
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // send sum to the channel c
}

func main(){
	s := []int{1, 2, 3, 4, 5}

	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	a, b := <- c, <- c
	a + b
}

make(chan int, 3) // buffered channel, fails if <- when buffer is full
close(ch) // close the channel to do not receive more values, test with v, ok := <-ch

select { // SELECT lets you wait on multiple goroutines but choose the first that resolves
case msg := <-ch:
	fmt.Println("received", msg)
case <-time.After(2 * time.Second):
	fmt.Println("Timeout!")
}

// Mutex: data structure for mutual exclusion: one routine can access a variable a time to avoid conflics
import ("sync" "time")

type SafeCounter struct {
	mu sync.Mutex
	v map[string]int
}

func (c *SafeCounter) Inc(key string){
	c.mu.Lock()
	c.v[key]++  // a single goroutine can access the map at a time
	c.mu.Unlock()
}

func (c *SafeCounter) Value(key string) int {
	c.mu.Lock()
	defer c.mu.Unlock() // Lock so we wait for the other to finish access
	return c.v[key]
}

func main(){
	c := SafeCounter{v: make(map[string]int)}
	for i:=0; i< 100; i++{ go c.Inc("somekey")}

	time.Sleetp(time.Second)
	fmt.Println(c.Value("somekey"))
}

/// UNIT TEST AND TESTING

func F(){} // TestF
type T struct {} // TestT
func (T) M()  {} // TestT_M

import "testing"  //use testing.T struct

funct TestF(t *testing.T){
	t.Log() // similar to Println
	t.Fail()
	t.FailNow()
	t.Error()
	t.Fatal()
	t.Skip()
	t.Cleanup(func() {
		t.Log()
	})
}

/// GRPG

/// CONTEXT


/// PACKAGE MANAGERS


/// MICROSERVICES


/// DEPLOYMENT


/// ORMs: SQLc
1-Create schema.sql file with normal tables

2-Create operations on query.sql
-- name: GetAuthor :one
SELECT * FROM authors WHERE id = $1 LIMIT 1;

-- name: ListAuthors :many
SELECT * FROM authors ORDER BY name;

-- name: CreateAuthor :one
INSERT INTO authors (name, bio) VALUES ($1, $2) RETURNING *;

-- name: UpdateAuthor :exec
UPDATE authors SET name = $2, bio = $3 WHERE id = $1;

-- name: DeleteAuthor :exec
DELETE FROM authors WHERE id = $1;

3-Call $sqlc generate

4-Code
import (
	"database/sql"
	_ "github.com/lib/pq"
)
func main(){
	connectionStr := "postgres://user:pass@localhost:5432/dbname?sslmode=disable"
	db, err := sql.Open("postgres", connectionStr)
	if err != nil { log.Fatal(err)}

	defer db.Close()

	ctx := context.Background()
	queries := products.New(db)
}

// COMPOSITION vs INHERITANCE

type Alive struct {}
type Walkable struct {}

type Duck struct {
	a Alive
	w Walkable
}

d := Duck{}



// READERS: https://cs.opensource.google/search?q=Read%5C(%5Cw%2B%5Cs%5C%5B%5C%5Dbyte%5C)&ss=go%2Fgo
import "io"

r := strings.NewReader("Hello reader")
b := make([]byte, 8)
for {
	n, err := r.Read(b)
	fmt.Printf("n = %v err = %v b = %v \n", n, err, b)
	fmt.Printf("b[:n] = %q \n", b[:n])
	if err == io.EOF { break}
}
// IMAGES:
import "image"

func main(){
	m := image.NewRGBA(image.React(0, 0, 100, 100))
	fmt.Println(m.Bounds())
	fmt.Prinln(m.At(0, 0).RGBA())
}


////////// MAIN STRUCTURE



func main(){}


fmt.Prinln("Hello %s", world)
f
