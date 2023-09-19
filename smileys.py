def convert(str): 
    smileys = str.replace(":)", "🙂") 
    smileys_frowneys = smileys.replace(":(", "🙁")
    return smileys_frowneys

def main():
    smileyfrowney = input("Please write a sentence including a smiley :) and/or a frowney :(")
    results = convert(smileyfrowney)
    print(results)

main()