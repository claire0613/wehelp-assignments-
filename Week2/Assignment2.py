def calculate(min,max):
    sum=0
    n=min
    for i in range(min,max+1):
        sum+=n
        n+=1
    print(sum)
calculate(1,3)
calculate(4,8)

def avg(data):
    sum=0
    for i in range(data["count"]):
        sum+=data["employees"][i]["salary"]
    avg_salary=sum/data["count"]
    print(avg_salary)

avg({
    "count":3,
    "employees":[{"name":"John","salary":30000},
    {"name":"Bob","salary":60000},
    {"name":"Jenny","salary":50000}
    ]
})
def maxProduct(nums):
    max_multi=0
    for i in range(len(nums)):
        n1=nums[i]
        nums_c=nums.copy()
        nums_c.pop(i)
        for j in range(len(nums_c)):
            n2=nums_c[j]
            multi_number=n1*n2
   
            if(multi_number>max_multi):
                max_multi=multi_number 
            elif(len(nums)==2):
                max_multi=multi_number
    print(max_multi)   
  

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])

def twoSum(nums,target):

    table={}
    for i in range(len(nums)):    
        table[nums[i]]=i
    for i in range(len(nums)):
        if target-nums[i] in table:
            if table[target-nums[i]] != i:
                return [i, table[target-nums[i]]]
    return []

result=twoSum([2, 11, 7, 15], 9)
print(result)

                    


def maxZeros(nums):
    length=0
    longest_length= 0
    for i in range(len(nums)):
        n=nums[i]  
        if n==0:
            length+=1
            if (length>longest_length):
                longest_length=length
        else:
            length=0
    print(longest_length)
            

maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])
