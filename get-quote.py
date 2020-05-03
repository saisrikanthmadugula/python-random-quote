import random

def elementary():
  print("Keep it logically awesome.\n")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=len(quotes)-1
  rnd = random.randint(0,last)
  print(quotes[rnd])
  rnd = random.randint(0,last)
  print(quotes[rnd])

  #creating a file object temp to write new lines to quotes.txt file.
  temp=open("quotes.txt","a")
  newquotes=["I am the best","We will win"]
  for line in newquotes:
    #write line to temp file
    temp.write(line)
    temp.write("\n")
  temp.close()
  
  #printing the last two lines in the quotes.txt file
  newtemp=open("quotes.txt")
  quotes=newtemp.readlines()
  last=len(quotes)-1
  print(quotes[last-1])
  print(quotes[last])
  newtemp.close()

if __name__== "__main__":
  elementary()
