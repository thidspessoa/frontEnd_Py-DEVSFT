#Tuplas são basicamente variaveis mas que aceitam mais de um valor dentro dela, usando uma virgula. A tupla também é imutavel

#lista = list,3



def getTimestamp():
  return round(time.time()*1000)

if __name__ == "__main__":
  recording = {}
  start, stop = (0, 0)
  running = False
  while True:
    if keyboard.is_pressed("f10"):
      start = getTimestamp()
      print("Recording...")
      running = True
    if keyboard.is_pressed("f12"):
      stop = getTimestamp()
      print("Stopped recording!")
      break
    if running:
      current_time = getTimestamp() - start
      recording[current_time] = keyboard.read_key()
  # create audio file
  createSound("./test.wav", start, stop, recording)
  print("Done!")
  
#faz isso

class Solution:
    def twoSum(num: int, target: int) -> int:
        for i in range(len(num) -1):
            for j in range(i, len(num)-1):
                if num[i] + num[j] == target:
                    list = [i, j]
                    return list
def main():
    num = [3,2,4]
    target = 6
    r= twoSum(num, target)
    print(r)
        
if __name__ == '__main__':
    main()