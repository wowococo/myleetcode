/*
多线程循环打印 123

题目描述
启动 3 个线程，
线程 1 无限循环打印 1、
线程 2 无限循环打印 2、
线程 3 无限循环打印 3，
要求按 123123....顺序循环打印
*/

// 使用 Channel（最地道的 Go 语言写法）

// 利用三个无缓冲的 channel 来传递“执行令牌”。只有接收到 channel 里的信号，
// goroutine 才会执行打印，打印完再通过下一个 channel 把信号传递出去。

package main

import (
	"fmt"
	"time"
)

func main1() {
	// 创建三个无缓冲 channel
	// struct{}{} 不占用内存，常用于纯信号传递
	ch1 := make(chan struct{})
	ch2 := make(chan struct{})
	ch3 := make(chan struct{})

	go func() {
		for {
			<-ch1                              // 阻塞等待 ch1 接收信号
			time.Sleep(500 * time.Millisecond) // 休眠以便观察控制台输出, 这个先跑一次再加
			fmt.Print("1")
			ch2 <- struct{}{} //打印完毕后，向 ch2 发送信号
		}
	}()

	go func() {
		for {
			<-ch2 // 阻塞等待 ch2 接收信号
			fmt.Print("2")
			ch3 <- struct{}{} // 打印完毕后，向 ch3 发送信号
		}
	}()

	go func() {
		for {
			<-ch3 // 阻塞等待 ch3 接收信号
			fmt.Print("3")
			ch1 <- struct{}{} // 打印完毕后，向 ch1 发送信号，开启下一轮循环
		}
	}()

	// 发送初始信号给ch1, 启动整个打印链条
	ch1 <- struct{}{}

	// 使用空的 select 阻塞主 goroutine，防止程序退出
	select {}
}

func main_answer() {
	// 创建三个无缓冲 channel
	// struct{}{} 不占用内存，常用于纯信号传递
	ch1 := make(chan struct{})
	ch2 := make(chan struct{})
	ch3 := make(chan struct{})

	// 启动 goroutine 1
	go func() {
		for {
			<-ch1                              // 阻塞等待 ch1 接收信号
			time.Sleep(time.Millisecond * 500) // 休眠以便观察控制台输出

			fmt.Print("1")
			// time.Sleep(time.Millisecond * 500) // 休眠以便观察控制台输出
			ch2 <- struct{}{} // 打印完毕后，向 ch2 发送信号
		}
	}()

	// 启动 goroutine 2
	go func() {
		for {
			<-ch2 // 阻塞等待 ch2 接收信号
			fmt.Print("2")
			ch3 <- struct{}{} // 打印完毕后，向 ch3 发送信号
		}
	}()

	// 启动 goroutine 3
	go func() {
		for {
			<-ch3 // 阻塞等待 ch3 接收信号
			fmt.Print("3")
			ch1 <- struct{}{} // 打印完毕后，向 ch1 发送信号，开启下一轮循环
		}
	}()

	// 发送初始信号给 ch1，启动整个打印链条
	ch1 <- struct{}{}

	// 使用空的 select 阻塞主 goroutine，防止程序退出
	// 因为题目要求是无限循环
	select {}
}
