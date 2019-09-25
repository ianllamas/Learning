#include <iostream>
#include <string.h>

using namespace std;

class Book{
private:
    //variable area
    string name;
    string author;
    string title;
    int price;
public:
    //function area
    Book (){
        name = "";
        author = "";
        title = "";
        price = 100;
    }

    Book(string nameOfBook, string nameOfAuthor, string titleOfBook, int priceOfBook){
        name = nameOfBook;
        author = nameOfAuthor;
        title = titleOfBook;
        price = priceOfBook;
    }
    void setPrice(int priceValue){
        if(priceValue > 0)
        price = priceValue;

        else
        {
            cout << "This is not a correct value for price";
        }
        
    }
    void setNameOfBook (string nameOfBook){
        name = nameOfBook;
    }
    void setAuthor (string authorName){
        author = authorName;
    }
    void setTitle (string titleOfBook){
        title = titleOfBook;
    }
};

class Cookbook: public Book{
public:
    Cookbook(){
        cout<<"Hey i am a Constructor of a Cookbook class";
        
    }
};

int main() {
   Book book("Learn C++", "Ian", "Learning C++ in detail", 300);
   //book.setPrice(400);
   //book.setNameOfBook("Learn C++");
   //book.setAuthor("Hamza");
   //book.setTitle("Learning C++ in detail");
   //book.setAuthor("Hamza");
   //cout <<book.author;
    Cookbook cookbook;
    cookbook.setPrice;


    return 0;    
}
