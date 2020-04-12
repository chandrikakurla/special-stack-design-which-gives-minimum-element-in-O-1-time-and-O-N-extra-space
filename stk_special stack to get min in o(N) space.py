class Special_Stack:
    def __init__(self):
        #original stack 
        self.stack=[]
        #imaginary stack to get min element in O(1) time 
        self.img_stack=[]
        self.top=-1
    def peek(self,stack):
        if self.top==-1:
            print("stack underflow")
            return
        return self.stack[self.top]
    def push(self,data):
        if self.top==-1:
            min=data
            self.top+=1
            self.stack.append(data)
            self.img_stack.append(data)
            return
        if(data<min):
            min=data
            self.top+=1
            self.stack.append(data)
            self.img_stack.append(data)
            return
        if(data>min):
            self.top+=1
            self.stack.append(data)
            self.img_stack.append(min)
            return
    def pop(self):
        if self.top==-1:
            print("stack underflow")
            return
        if(self.peek()==min):
            self.img_stack.pop()
            self.top-=1
            min=self.peek(img_stack)
            return self.stack.pop()
        self.img_stack.pop()
        self.top-=1
        return self.stack.pop()
    def getMin(self):
        if self.top==-1:
            print("stack underflow")
            return
        return min
if __name__=="__main__":
    stacks=Special_Stack()
    stacks.push(8)
    stacks.push(10)
    stacks.push(6)
    stacks.push(3)
    stacks.push(7)   
    print(stacks.getMin())     