#Here's some code witch will help you in checking if triangle exist

class Triangle:

    def sides_input(self):

        sides = [None, None, None]

        for x in range(0, 3):
            sides[x] = int(input("Please, enter your side: "))

        return sides

    def triangle_checking(self, sides):

        a = sides[0]
        b = sides[1]
        c = sides[2]

        if a + b > c and a + c > b and b + c > a:
            print("\nYoru triangle exist")
        else:
            print("\nYour triangle don't exist")


    def is_triangle_valid(self):
        self.triangle_checking(self.sides_input())