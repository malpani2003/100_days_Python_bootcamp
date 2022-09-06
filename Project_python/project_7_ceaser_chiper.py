letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length_letter=len(letter)
# print(length_letter)
# print(letter.index("x"))
# print(letter.index("y"))
# print(letter.index("z"))
def encode():
    input_str=input("Enter the string to encode : ")
    jump=int(input("Enter the jump: "))
    length=len(input_str)
    print(length)
    output_str=""
    for i in range(0,(length)):
        for j in range(0,(length_letter)):
            if input_str[i]==letter[j]:
                if(j+jump<=25):
                    output_str+=letter[j+jump]
                else:
                    output_str+=letter[-length_letter+jump+j]

    print(f"Encode string will be {output_str}")
    print(len(output_str))

def decode():
    input_str=input("Enter the string to decode : ")
    jump=int(input("Enter the jump: "))
    length=len(input_str)
    print(length)
    output_str=""
    for i in range(0,(length)):
        for j in range(0,(length_letter)):
            if input_str[i]==letter[j]:
                if(j+jump<=25):
                    output_str+=letter[j-jump]
                else:
                    output_str+=letter[length_letter-jump-j]

    print(f"Decode string will be {output_str}")
    print(len(output_str))
ans=1
while(ans==1):
    option=int(input("Press 1 for Encode and 2 for decode :"))
    if(option==1):
        encode()
    elif(option==2):
        decode()
    ans=int(input("Do you want to contiue again(Press 1 for again) : "))



