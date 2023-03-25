num=int(input("Enter a number:"))
sum=0
temp = num
while temp > 0:
    digit=temp % 10
    sum+=digit**3
    temp//=10
if num ==sum:
  print(num,"Is A Armstrong Number")
else:
  print(num,"Is A  Not Armstrong Number")
