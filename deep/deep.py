answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
lowercase_answer = answer.lower()
clean_answer = ' '.join(lowercase_answer.split())
print(clean_answer)
if "42" in clean_answer:
    print("Yes")
elif "fourty-two" in clean_answer:
    print("Yes")
elif "fourty two" in clean_answer:
    print("Yes")
else:
    print("No")
    