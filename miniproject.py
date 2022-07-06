class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def displaybook(self):
        print("We have following books in our library")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book in self.booklist and book not in self.lendDict:
            self.lendDict.update({book: user})
            print("yes you can lend this book")
        elif book in self.lendDict:
            print(f"sorry , this book is already being used by {self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to the booklist")

    def returnbook(self,book):
        self.booklist.remove(book)
        print("Book has been return form the booklist")


if __name__ == '__main__':
    Ani=Library(['python','C++','C programming','java'],"Abhiroj")

    while(True):
        print(f"Welcome to the {Ani.name} Library. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lended Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice=int(input())

        if user_choice==1:
            Ani.displaybook()
        elif user_choice==2:
            user=input("Enter the name of the user")
            book = input("Enter the name of the book you want to lend")
            Ani.lendbook(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add")
            Ani.addbook(book)
        elif user_choice==4:
            book=input("Enter the name of the book you want to retu1rn")
            Ani.returnbook()
        else:
            print("Not a valid option")

        print("Enter q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="q" and user_choice2!="c"):
            user_choice2 = input()
            if user_choice2=="q":
                exit()

            elif user_choice=="c":
                continue







