import random
import time

def make_random_sentence():
  nouns = ["puppy", "car", "rabbit", "girl", "monkey"]
  verbs = ["writes", "drinks", "jumps", "drives", "barfs"]
  adv = ["crazily", "dutifully.", "foolishly.", "merrily", "occasionally"]
  adj = ["adorable", "clueless", "dirty", "odd", "stupid"]

  #get all random permutations
  random_entry = lambda x: x[random.randrange(len(x))]
  
  return " ".join([random_entry(nouns), random_entry(verbs), random_entry(adv), random_entry(adj)])

def typing_test():
    sentence = make_random_sentence()
    print(f"{sentence}\n")

    input("Press Enter when ready...")
    
    start = len(" ".join(input().split()))  # Capture length of user input as a time proxy
    
    print("\nChecking...")
    
    user_words = input("Re-enter your sentence for verification: ").split()
    correct_words = sentence.split()
    
    score = sum(1 for u, c in zip(user_words, correct_words) if u == c)
    wpm = score * 2
    
    print(f"\nYour estimated speed: {wpm} WPM!")
    print("Accuracy:", f"{(score / len(correct_words)) * 100:.2f}%" if correct_words else "0%")

if __name__ == "__main__":
    
  typing_test()
