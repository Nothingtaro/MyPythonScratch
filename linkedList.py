class node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
    
class linked_list:
  def __init__(self):
    self.head = node()
    
  def append(self,data):
    new_node = node(data)
    cur_node = self.head
    while cur_node.next != None:
      cur_node = cur_node.next
    cur_node.next = new_node
    
  def length(self):
    cur_node = self.head
    total = 0
    while cur_node.next != None:
      total += 1
      cur_node = cur_node.next
    return total
  
  def display(self):
    elems = []
    cur_node = self.head
    while cur_node.next != None:
      cur_node = cur_node.next
      elems.append(cur_node.data)
    print(elems)

  def get(self, index):
    if index >= self.length():
      raise ValueError("ERROR: 'Get Index out of range!")
    cur_idx = 0
    cur_node = self.head
    while True:
      cur_node = cur_node.next
      if cur_idx == index:
        return cur_node.data
      cur_idx += 1
      
  def erase(self, index):
    if index >= self.length():
      raise ValueError("ERROR: 'Get Index out of range!")
    cur_idx = 0
    cur_node = self.head
    while True:
      last_node = cur_node
      cur_node = cur_node.next
      if cur_idx == index:
        last_node.next = cur_node.next
        return None
      cur_idx += 1

myList = linked_list()

myList.display()

myList.append(1)    
myList.append(2)    
myList.append(3)    
myList.display()

myList.erase(1)
myList.display()