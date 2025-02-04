class Jar:
    def __init__(self, capacity = 12):
       self.capacity = capacity
       self.size = 0


    def __str__(self):
        return  f'{self.size * '🍪'}'

    def deposit(self, n):
        self.size = self.size + n
        if self.size > self.capacity:
            raise ValueError('Jar is too small')


    def withdraw(self, n):
        self.size = self.size - n
        if self.size < 0:
            raise ValueError('There are too few cookies inside the Jar')


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Capacity has to be non-negative')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n

def main():
  cookies = Jar(2)
  print(cookies)




if __name__ == '__main__':
    main()
