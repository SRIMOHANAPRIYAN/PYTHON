class ClassAssignment():
    
    def subfields():
        print("Subfields in AI are: ")
        mess="Subfields in AI are: "
        print("Machine Learning")
        mess="Machine Learning"
        print("Neural Network")
        mess="Neural Network"
        print("Vision")
        mess="Vision"
        print("Robotics")
        mess="Robotics"
        print("Speech Processing")
        mess="Speech Processing"
        print("Natural Language Processing")
        mess="Natural Language Processing"
        return mess

    def oddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(f"{num} is even number")
            mess=f"{num} is even number"
        else:
            print(f"{num} is odd number")
            mess=f"{num} is odd number"
            return mess

    def MarriageEligibility():
        gender = input("Your gender: ")
        age = int(input("Your age: "))
        if gender == "male":
            if age >= 21:
                print("Eligible")
                message="Eligible"
            else:
                print("Not eligible")
                message="Not eligible"
        elif gender == "female":
            if age >= 18:
                print("Eligible")
                message="Eligible"
            else:
                print("Not eligible")
                message="Not eligible"
        else:
            print("Invalid gender")
            message="Invalid gender"
            return message 

    def FindPercentage():
        num1=int(input("Subject1: "))
        num2=int(input("Subject2: "))
        num3=int(input("Subject3: "))
        num4=int(input("Subject4: "))
        num5=int(input("Subject5: "))
        total=num1+num2+num3+num4+num5
        percentage=total/500*100
        print("Total: ",total)
        message="Total: ",total
        print("Percentage: ",percentage)
        message="Percentage: ",percentage
        return message

    def triangle():
        Height=int(input("Height:"))
        Weight=int(input("Weight:"))
        print("Area formula :(Height*Weight)/2")
        message="Area formula :(Height*Weight)/2"
        mull=(Height*Weight)/2
        print("Area of triangle:",mull)
        message="Area of triangle:",mull
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breath=int(input("Breath:"))
        print("perimeter formula: Height1+Height2+Breath")
        message="perimeter formula: Height1+Height2+Breath"
        total=Height1+Height2+Breath
        print("perimeter of triangle:",total)
        message="perimeter of triangle:",total
        return message

    