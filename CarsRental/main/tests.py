
import random
import string
# Create your tests here.
def password_generate():
   sentence = string.ascii_letters + string.digits + string.punctuation
   Complete_sentence = ''.join(random.choice(sentence) for _ in range(10))
   editsentence=f"<center><h1 style= color:blue>{Complete_sentence}</h1></center>"
   print(editsentence)
password_generate()