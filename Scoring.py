
#get scores function 
def grade(score):
    if 90 <= score <= 100:
        letter_grade = 'A'
    elif 80 <= score <= 89:
        letter_grade = 'B'
    elif 70 <= score <= 79:
        letter_grade = 'C'
    elif 60 <= score <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade  
    
    
    
#get total of the grades function     
total=0;    
def gettotal(test):
    global total;
    total+=test;
    return total;
'''Project 5 - Program 1
by Solmaz Gharagozloo
11/23/18
'''   

    
student=[]
studenttest1=[]
studenttest2=[]
studenttest3=[]

student_number=int(input("please enter the number of students "))

#Hello Solmaz..have you watched the discussion we had on Saturday? I have explained how to do this program


#get student name function 
def getname():
 for i in range(student_number):
     stud = (input("Enter the name student number" + str(i+1)+ ": "))
     student.append(stud);
 return student
 
 
 #average function 
ave=0
average=[]
def getaverage():
    
    for i in range(len(student)):
        average.append((studenttest1[i]+studenttest2[i]+studenttest3[i])/3)
        
    
    return average



#Dear Professor- I used nested loop so I can make the student name variable. it should be revised , I want to place 3 scores of esch student into a seperate list , but I dont know how ?
#how can I have three list and append the scores of each student in each ? Try to use three different score lists
# are you here online?
totallist=[]
def getscore():
  for j in range(student_number):
   
    
      studenttest1.append(float(input("Enter the axam number[" + str(j+1)+ "] for "+student[j] +":" )))
      studenttest2.append(float(input("Enter the axam number[" + str(j+1)+ "] for "+student[j] +":" )))
      studenttest3.append(float(input("Enter the axam number[" + str(j+1)+ "] for "+student[j] +":" )))
      #gettotal(test);
  
  

  

def main():
 getname()   
 getscore()
 getaverage()
 for i in range(student_number):
    print("the Score for "+student[i]+ " is: "+str(format(average[i],",.2f"))+" and the grade is: "+ grade(average[i]))


main()
   
      
