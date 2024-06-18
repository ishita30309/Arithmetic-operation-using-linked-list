# aritmetic operation in linked list 
class Node:
    def __init__(self,data=0,next=None):
        # initialising the node with data and next pointer
        self.data=data
        self.next=next
    
def append(head, data):
    # appendng new node to the end of the list
    new_node=Node(data)
    # if list is empty then new_node becoms head
    if not head:
        return new_node
    temp=head
    # traversing to the end of the list
    while temp.next:
        temp=temp.next
    temp.next=new_node
    # append to the new node
    return head

# printing linked list   
def print_list(head):
    while head:
        print(head.data,end=" ")
        head=head.next
    print()

def add_two_numbers(n1,n2):
    dummy=Node()
    p=dummy
    carry=0
    
    while n1 or n2 or carry:
        sum=carry
        #  add data from n1
        if n1:
            sum+=n1.data
            n1=n1.next
        if n2:
            # add data from n2
            sum+=n2.data
            n2=n2.next
        carry=sum//10
        # crating new node
        p.next=Node(sum%10)
        p=p.next
    return dummy.next
    
def subtract_two_numbers(n1,n2):
    dummy=Node()
    p=dummy
    borrow=0
    
    while n1 or n2:
        diff=(n1.data if n1 else 0) - (n2.data if n2 else 0) - borrow
        # if the diff is negative then adding 10 to it 
        if diff<0:     
            diff+=10
            borrow=1
        else:
            borrow=0
        # creating new node for the curr digit
        p.next=Node(diff)
        p=p.next
        if n1:
            n1=n1.next
        if n2:
            n2=n2.next
    return dummy.next

def multiply_two_numbers(n1,n2):
    if not n1 or not n2:
        return Node(0)
    #  converting n1 to number
    num1=0
    mul=1
    while n1:
        num1+=n1.data*mul
        mul*=10
        n1=n1.next
    # converting n2 to number
    num2=0
    mul=1
    while n2:
        num2+=n2.data*mul
        mul*=10
        n2=n2.next
        
    product=num1*num2
    
    # converting it to linked list
    dummy=Node()
    p=dummy
    if product==0:
        return Node(0)
    while product>0:
        p.next=Node(product%10)
        product//=10
        p=p.next
    return dummy.next
    
    
    
    
def reverse(head):
    prev=None
    curr=head
    # reversing the direction of the next pointer
    while curr:
        next_temp=urr.next
        curr.next=prev
        prev=curr
        curr=next_temp
    return prev
if __name__=="__main__":
    num1=None
    num2=None
    
    # Number1-> 123 (3->2->1)
    num1=append(num1, 1)
    num1=append(num1, 2)
    num1=append(num1, 3)
    # Number2-> 456 (6->5->4)
    num2=append(num2, 4)
    num2=append(num2, 5)
    num2=append(num2, 6)
    
    print_list(num1)
    print_list(num2)
    
    # Addition
    result_sum=add_two_numbers(num1,num2)
    print("addition")
    print_list(result_sum)
    
    #  subtraction
    result_sub=subtract_two_numbers(num1,num2)
    print("difference")
    print_list(result_sub)
    
    # multiplication
    result_mul=multiply_two_numbers(num1,num2)
    print("multiplication")
    print_list(result_mul)








    
