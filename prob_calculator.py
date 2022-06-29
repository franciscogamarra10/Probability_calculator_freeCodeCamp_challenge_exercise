import copy
import random
# Consider using the modules imported above.

class Hat:
  ## **args para definir un objeto iterable de 2 indices
  def __init__(self,**lista):
    self.contents=[]
    for key,value in lista.items() :
      for j in range(value):
        self.contents.append(key)
      

  def contenido(self):
     
     v22=copy.copy(self.contents)

     return v22

    
  def draw(self,n):
    self.n=n

    if self.n >len(self.contents):
      return self.contents
    else:
      v2=random.sample(self.contents,self.n)
      # v22=copy.copy(self.contents)
      for i in range(len(v2)):
    
          self.contents.remove(v2[i])
      
      return v2

      


  def nt(self):
    
  

    return len(self.contents)




    

      

  
  
  

# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # print(hat.contents)
  contenido=hat.contenido()
  
  bb=contenido
  
  
  contenido2=[] ###  lista conteniendo la cantidad de bolas del experimento

  for key,value in expected_balls.items() :

      for j in range(value):
        contenido2.append(key)

  # print(hat.contents)
  # print(contenido2)
  casos=0
  for i in range(num_experiments):
    ## muestra random a extraer
    # print(contenido.contents)
    
    # conte=contenido_l
    # print(hat.contents)
    # print(contenido)
    # print(num_balls_drawn)
    if num_balls_drawn<= len(contenido):
        
        subcon=random.sample(bb,num_balls_drawn)
        # bb.remove(subcon)
    else:
        subcon=contenido
      
    # print(subcon)
    # print('---')
    # print(contenido2)
    # ss=0  
    # print(len(subcon))
    # print(len(contenido2))
    # for l1, l2 in zip(contenido2, subcon):
    #   print(l1,l2)
    #   if l1==l2:
    #     ss=ss+1
        
    # print(ss)    
    contenido22=set(contenido2)
    ll=[]
    for i in contenido22:

     if subcon.count(i)>= contenido2.count(i):
        ll.append(i)

    ll=set(ll) 
    # ll2=set(range(0,len(contenido2)))
    # print('---')
    # print(ll)
    # print('---')
    # print(ll2)
           
   
      
    # print(f'{l1} -> {l2}')  
    # print(subcon)
    # print(contenido2)
    # contenido3=[x for x in subcon if x in contenido2]## que 

    # ss=[]
    # for j in range(len(contenido2)):
    #    if contenido2[j] in subcon:
         
         # print(subcon)
    # print(ss)  
    # bolas coinciden de lo que se espera en el sample
    # print(subcon)
    # print(contenido2)
    # print(contenido3)
    if ll ==contenido22 :
    # if len(ll) == len(contenido2):  
      casos+=1
      # print('--')
      # print(casos)
      # bb=hat
      
    # else:
    #   bb=hat
      

    

  return casos/num_experiments


random.seed(95)
# hat = Hat(blue=4, red=2, green=6)

# probability =experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

# hat = Hat(red=5,blue=2)

hat =Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=3000)
        # actual = probability
        # expected = 0.272

# hat=Hat(yellow=5,red=1,green=3,blue=9,test=1)

# probability =experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

print(probability)
        # actual = probability
        # expected = 1.0



# print(hat.draw(2))
        # expected = ['blue', 'red']
        # self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
# print(len(hat.contents))
        # expected = 5