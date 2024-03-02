my_list=["car1","car2","car3","car4","car1"]
deleted_values=[]

while "car1" in my_list:
  my_list.remove("car1")
  deleted_values.append("car1")

print("deleted values:",deleted_values)
print("remaining list:",my_list)
  
