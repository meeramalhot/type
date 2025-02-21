import random
import time
import wonderwords

#https://pypi.org/project/wonderwords/
#r = RandomWord()
#r.random_words(3, include_parts_of_speech=["nouns"])

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
    
    start_time = time.time()
    start = len(" ".join(input().split()))
    end_time = time.time()

    elapsed_time_seconds = end_time - start_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    
    print("\nChecking...")
    
    user_words = input("Re-enter your sentence for verification: ").split()
    correct_words = sentence.split()
    
    score = sum(1 for u, c in zip(user_words, correct_words) if u == c)

    if(elapsed_time_minutes !=0):
      wpm = len(sentence) / elapsed_time_minutes
      print(f"\nYour estimated speed: {wpm} WPM!")
    else:
      wps = len(sentence) / elapsed_time_seconds
      print(f"\nYour estimated speed: {wps} WPS!")

    print("Accuracy:", f"{(score / len(correct_words)) * 100:.2f}%" if correct_words else "0%")

if __name__ == "__main__":
    
  typing_test()
