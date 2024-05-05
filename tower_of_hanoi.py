def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    source = input("Enter the name of the source peg: ")
    target = input("Enter the name of the target peg: ")
    auxiliary = input("Enter the name of the auxiliary peg: ")
    tower_of_hanoi(n, source, target, auxiliary)

'''def tower_of_hanoi_iterative(n, source, target, auxiliary):
    if n == 0:
        return
    
    stack = [(n, source, target, auxiliary)]
    
    while stack:
        disks, source, target, auxiliary = stack.pop()
        
        if disks == 1:
            print(f"Move disk from {source} to {target}")
        else:
            # Push the moves for the smaller disks onto the stack
            stack.append((disks - 1, auxiliary, target, source))
            stack.append((1, source, target, auxiliary))
            stack.append((disks - 1, source, auxiliary, target))

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    source = input("Enter the name of the source peg: ")
    target = input("Enter the name of the target peg: ")
    auxiliary = input("Enter the name of the auxiliary peg: ")
    tower_of_hanoi_iterative(n, source, target, auxiliary)
'''
