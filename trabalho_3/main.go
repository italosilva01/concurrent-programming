package main

import (
	"fmt"
	"sync"
	"time"
)
var waitGroup sync.WaitGroup



func runners(position  int){
	
	if position !=1{
		fmt.Println("Corredor n°",position,"recebe bastão")
	}

	fmt.Println("Corredor n°",position, "está correndo")
	time.Sleep(5*time.Second) 
	
	if position !=4 {
		fmt.Println("Corredor n°",position, "grita para o proximo corredor 🗣")
		
		time.Sleep(1*time.Second) 
		
		fmt.Println("Corredor n°",position,"entrega bastão")
		fmt.Println()
		position +=1 
		waitGroup.Add(1)
		go runners(position)	
	}
	
	waitGroup.Done()

}

 func main() {
	
	
	waitGroup.Add(1)
	go runners(1)		
	

	waitGroup.Wait()
	fmt.Println("A corrida terminou!!!")

 }
