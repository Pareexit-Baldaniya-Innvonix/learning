// Task 1

// Outer class
class Library {
    constructor(name) {
        this.libraryName = name;
        // Access the class via the Static reference
        this.book = new Library.Book(this);
    }
}

// Inner class
Library.Book = class {
    constructor(outerLibrary) {
        this.outerLibrary = outerLibrary;
    }

    getLibraryName() {
        return this.outerLibrary.libraryName;
    }
};

const myLibrary = new Library("City Central Library");
console.log(myLibrary.book.getLibraryName());