inputNums = []
counter = 0
flag = True

while True:
    try:
        inputNum = input("Input a number: ")
        if inputNum == 'Done':
            break
    except:
        print("Input a number or the word Done")
    else: 
        inputNums.append(int(inputNum))
        counter += 1

inputNums.sort()
sum = 0
for num in inputNums:
    sum += num
average = sum/len(inputNums)

print(inputNums)
print(inputNums[0])
print(inputNums[len(inputNums)-1])
print(average)
