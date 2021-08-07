class DLNode:
    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.end_of_sorted_list = None
        self.the_claw = None

    def print_forward(self):
        if self.head == None:
            print("No list to print")
        else:
            print("Printing List Forward:")
            runner = self.head
            print_counter=0
            while(runner != None):
                print(runner.value)
                runner = runner.next
                print_counter +=1
                if print_counter > 15:
                    return
        return self

    def print_forward_detailed(self):
        if self.head == None:
            print("No list to print")
        else:
            print("Printing List Forward:")
            runner = self.head
            print_counter=0
            while(runner != None):
                print(runner.value)
                print("\t", runner.previous)
                print("\t",runner)
                print("\t", runner.next)
                runner = runner.next
                print_counter +=1
                if print_counter > 15:
                    return
        return self

    def print_backward(self):
        if self.tail == None:
            print("No list to print")
        else:
            print("Printing List Backward:")
            runner = self.tail
            while(runner != None):
                print(runner.value)
                runner = runner.previous
        return self

    def add_to_front(self, val):
        if self.head == None:
            # print("Empty list detected.  Adding new head, which is also the tail!")
            self.head = DLNode(value = val, previous = None, next = None)
            self.tail = self.head
        else:
            self.head = DLNode(value = val, previous = None, next = self.head)
            self.head.next.previous = self.head
        return self

    def add_to_back(self, val):
        if self.tail == None:
            # print("Empty list detected.  Adding new tail, which is also the head.  Using add_to_front()")
            self.add_to_front(val)
        else:
            self.tail = DLNode(value = val, previous = self.tail, next = None)
            self.tail.previous.next = self.tail
        return self

    def insert_new_node_at(self, val, position):
        if self.head == None:
            print("There is no list to insert into.  Calling add_to_front")
            self.add_to_front(value=val)
        else:
            runner = self.head
            for counter in range(1,position):
                runner = runner.next
            node_to_insert=DLNode(value=val, previous=runner.previous, next=runner)
            if(runner.previous != None):
                runner.previous.next = node_to_insert
            node_to_insert.next.previous = node_to_insert
        return self

    def find_lowest_value(self):
        if self.head == None:
            print("There is no list to sort")
        else:
            runner = self.head
            self.the_claw = self.head
            while(runner != None):
                print("runner.value:", runner.value, "the_claw.value:",self.the_claw.value)
                if runner.value < self.the_claw.value:
                    print("runner.value:",runner.value,"is less than what the_claw is holding:",self.the_claw.value)
                    self.the_claw = runner
                runner = runner.next
            print("Minimum value found:",self.the_claw.value)

    def insertion_sort(self):
        print("*** BEGINNING OF INSERTION SORT ***")
        if self.head == None:
            print("There is no list to sort")
        else:
            self.end_of_sorted_list = self.head
            
            while(self.end_of_sorted_list.next != None):    # Loop until the end of the sorted list is the last item in the list
                
                # Look at the node after EOSL
                if self.end_of_sorted_list.value < self.end_of_sorted_list.next.value:
                    print(self.end_of_sorted_list.value,"is less than",self.end_of_sorted_list.next.value,", moving end_of_sorted_list marker forward")
                    self.end_of_sorted_list = self.end_of_sorted_list.next
                else:
                    print(self.end_of_sorted_list.value,"is greater than",self.end_of_sorted_list.next.value,", time to move a node!")

                    self.the_claw=self.end_of_sorted_list.next
                    print("self.the_claw.value:",self.the_claw.value)

                    #break that node out
                    if self.the_claw.next != None:
                        self.end_of_sorted_list.next = self.the_claw.next
                        self.the_claw.next.previous=self.end_of_sorted_list
                    else:
                        self.end_of_sorted_list.next = None

                    #look back to find where node belongs
                    runner = self.end_of_sorted_list
                    print("Runner starting at:",runner.value,"." , "self.the_claw.value is:", self.the_claw.value)

                    while(runner != None and self.the_claw.value < runner.value):
                        runner = runner.previous
                        # print("Runner value:",runner.value)

                    if runner != None:
                        print("Runner != None")
                        self.the_claw.previous = runner
                        self.the_claw.next = runner.next
                        runner.next.previous = self.the_claw
                        runner.next = self.the_claw
                    else:
                        print("Runner == None")
                        self.the_claw.previous = None
                        self.the_claw.next = self.head
                        self.head.previous = self.the_claw
                        self.head = self.the_claw

                    self.print_forward_detailed()

            self.tail = self.end_of_sorted_list


                    




    

    
        

list = DLList()
# list.add_to_back(11).add_to_back(22).add_to_back(33).add_to_back(99).add_to_back(88).add_to_back(77).add_to_back(66)
# list.add_to_back(11).add_to_back(99).add_to_back(88).add_to_back(22).add_to_back(33).add_to_back(77).add_to_back(66)
# list.add_to_back(5).add_to_back(10).add_to_back(31).add_to_back(20).add_to_back(42).add_to_back(7).add_to_back(35).add_to_back(9).add_to_back(27).add_to_back(97)
# list.add_to_back(275).add_to_back(390).add_to_back(405).add_to_back(360).add_to_back(307).add_to_back(408).add_to_back(550).add_to_back(557).add_to_back(590).add_to_back(475)
# list.add_to_back(36).add_to_back(45).add_to_back(90).add_to_back(87).add_to_back(88).add_to_back(57).add_to_back(64).add_to_back(73).add_to_back(61).add_to_back(99)

list.add_to_back(10).add_to_back(31).add_to_back(20).add_to_back(42).add_to_back(17).add_to_back(35).add_to_back(29).add_to_back(27).add_to_back(97).add_to_back(5)



list.print_forward_detailed()
list.insertion_sort()
list.print_forward()
# list.print_forward_detailed()
list.print_backward()