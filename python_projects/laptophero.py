# Python program to explain os.kill() method

# importing os and signal module
import os, signal

# Create a child process
# using os.fork() method
pid = os.fork()


# pid greater than 0
# indicates the parent process
if pid :
	

	
	print("\nIn parent process")

	# send signal 'SIGSTOP'
	# to the child process
	# using os.kill() method
	# 'SIGSTOP' signal will
	# cause the process to stop
	os.kill(pid,9)
	
	print("Signal sent, child stopped.")



	info = os.waitpid(pid, os.WSTOPPED)
	# waitpid() method returns a
	# tuple whose first attribute
	# represents child's pid
	# and second attribute
	# represnting child's status indication

	# os.WSTOPSIG() returns the signal number
	# which caused the process to stop
	stopSignal = os.WSTOPSIG(info[1])
	print("Child stopped due to signal no:", stopSignal)
	print("Signal name:", signal.Signals(stopSignal).name)

	
	# send signal 'SIGCONT'
	# to the child process
	# using os.kill() method
	# 'SIGCONT' signal will
	# cause the process to continue
	os.kill(pid, signal.SIGCONT)
	print("\nSignal sent, child continued.")
	
	
else :
	
	print("\nIn child process")
	print("Process ID:", os.getpid())
	print("Hello ! Geeks")
	print("Exiting")
