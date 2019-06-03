#todolist project
todolist = []
a = input("voulez vous ajouter un item? \n Separez les diff taches par des virgules")
a=a.split(',')
todolist.extend(a)
print (todolist)

b = input("voulez vous ajouter autre chose ?")
while b!= 'yes' or 'no':
  if b == "yes":
    a = input("new task")
    a=a.split(',')
    todolist.extend(a)
    
  elif b == "no":
    break
  b = input("voulez vous ajouter autre chose ?")
c = input("voulez vous supprimer qqchose ?")
while c!= 'yes' or 'no':
  if c == "yes":
    delete=input("que voulez vous supprimer?")
    todolist.remove(delete)
    break
  elif b=="no":
    break
print(todolist)
