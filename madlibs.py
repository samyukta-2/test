def madlibs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    
    story = f"One day, a {adjective} {noun} decided to {verb} {adverb}. It was a sight to behold!"
    
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    madlibs()

