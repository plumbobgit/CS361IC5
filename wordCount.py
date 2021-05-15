def wordCounts(a):
    return str(len(a.split()))


a = input("Enter a sentence: ")
print("The number of words in the sentence are: ", wordCounts(a))
