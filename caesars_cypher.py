import caesars_art
def encode(alphabet, idx, shifter, output):
    output.append(alphabet[(idx+ shifter)%len(alphabet)])
def decode(alphabet2, idx2, shifter2, output2):
    output2.append(alphabet2[(idx2 - shifter2)%len(alphabet2)])
print(caesars_art.logo)
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
continue_program = True
while continue_program:
    direction = input("Would you like to encrypt or decrypt? ").lower()
    message_entry = input("Enter a message: ").lower()
    shift_val = int(input("Enter a shift value: "))
    message_out = []
    out_string = ""
    if direction == "decrypt":
        shift_val *= -1
    for l in message_entry:
        counter = 0
        if l not in letter_list:
            message_out.append(l)
        for alp in letter_list:
            if l == alp:
                # if direction == "encrypt":
                #     encode(letter_list, counter, shift_val, message_out)
                # if direction == "decrypt":
                    # decode(letter_list, counter, shift_val, message_out)
                message_out.append(letter_list[(counter + shift_val)%len(letter_list)])
            counter += 1
    # for i in message_out:
    #     out_string +=
    out_string = "".join(message_out)
    print(f"Your {direction[:3]}oded message is: {out_string}")
    if input("Do you want to continue ciphering? ").lower() == "yes":
        continue_program = True
    else:
        continue_program = False
        print("Goodbye")