/* 
    Script: Kütüphane Yönetim Sistemi
    Açıklama: Kitap yönetimi ve kullanıcı işlemleri için etkileşimli kütüphane sistemi
    Yazar: [Future Developer] 
    Tarih: 05.09.2025
    Sürüm: 1.0

    Özellikler:
    - Kütüphaneci Paneli (şifre: admin123)
    - Kullanıcı Paneli (şifre: user123)
    - Kitap ekleme, silme, arama
    - Kitap ödünç alma ve iade sistemi

    Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.
*/

// Book categories
let fiction = [
    { title: "1984", author: "George Orwell", year: 1949, available: true, genre: "Dystopian" },
    { title: "Pride and Prejudice", author: "Jane Austen", year: 1813, available: true, genre: "Romance" },
    { title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925, available: false, genre: "Classic" },
    { title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960, available: true, genre: "Drama" }
];

let nonFiction = [
    { title: "Sapiens", author: "Yuval Noah Harari", year: 2011, available: true, genre: "History" },
    { title: "Educated", author: "Tara Westover", year: 2018, available: true, genre: "Memoir" },
    { title: "The Power of Habit", author: "Charles Duhigg", year: 2012, available: false, genre: "Psychology" }
];

let science = [
    { title: "A Brief History of Time", author: "Stephen Hawking", year: 1988, available: true, genre: "Physics" },
    { title: "The Selfish Gene", author: "Richard Dawkins", year: 1976, available: true, genre: "Biology" },
    { title: "Cosmos", author: "Carl Sagan", year: 1980, available: false, genre: "Astronomy" }
];

let categories = [fiction, nonFiction, science];
let categoryNames = ["Fiction", "Non-Fiction", "Science"];
let bookProperties = ["title", "author", "year", "available", "genre"];

// Borrowed books tracking
let borrowedBooks = [];

const addBook = () => {
    alert("Add a new book to the library");
    let categoryIndex = parseInt(prompt("Select category:\n1-Fiction\n2-Non-Fiction\n3-Science")) - 1;
    
    if (categoryIndex < 0 || categoryIndex >= categories.length) {
        alert("Invalid category selection!");
        return;
    }

    let newBook = {
        title: prompt("Enter book title:"),
        author: prompt("Enter author name:"),
        year: parseInt(prompt("Enter publication year:")),
        available: true,
        genre: prompt("Enter genre:")
    };

    categories[categoryIndex].push(newBook);
    alert(`Book "${newBook.title}" has been added to ${categoryNames[categoryIndex]} category successfully!`);
    console.log("New book added:", newBook);
};

const removeBook = (searchTerm) => {
    let removedBook = null;
    let categoryFound = null;

    for (let category of categories) {
        for (let book of category) {
            if (book.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                book.author.toLowerCase().includes(searchTerm.toLowerCase())) {
                removedBook = book;
                categoryFound = category;
                category.splice(category.indexOf(book), 1);
                break;
            }
        }
        if (removedBook) break;
    }

    if (removedBook) {
        alert(`Book "${removedBook.title}" by ${removedBook.author} has been removed successfully!`);
        console.log("Removed book:", removedBook);
    } else {
        alert("Book not found!");
    }
};

const searchBooks = (searchTerm) => {
    let foundBooks = [];
    
    for (let i = 0; i < categories.length; i++) {
        for (let book of categories[i]) {
            for (let property of Object.values(book)) {
                if (property.toString().toLowerCase().includes(searchTerm.toLowerCase())) {
                    foundBooks.push({...book, category: categoryNames[i]});
                    break;
                }
            }
        }
    }
    
    return foundBooks;
};

const displayBooksByCategory = () => {
    let categoryIndex = parseInt(prompt("Select category to view:\n1-Fiction\n2-Non-Fiction\n3-Science")) - 1;
    
    if (categoryIndex < 0 || categoryIndex >= categories.length) {
        alert("Invalid category selection!");
        return;
    }

    let selectedCategory = categories[categoryIndex];
    let output = `${categoryNames[categoryIndex]} Books:\n\n`;
    
    if (selectedCategory.length === 0) {
        output += "No books available in this category.";
    } else {
        selectedCategory.forEach((book, index) => {
            let status = book.available ? "Available" : "Borrowed";
            output += `${index + 1}. "${book.title}" by ${book.author}\n   Year: ${book.year} | Genre: ${book.genre} | Status: ${status}\n\n`;
        });
    }
    
    alert(output);
};

const borrowBook = (searchTerm) => {
    let bookToBorrow = null;
    let categoryFound = null;

    for (let category of categories) {
        for (let book of category) {
            if ((book.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                book.author.toLowerCase().includes(searchTerm.toLowerCase())) && book.available) {
                bookToBorrow = book;
                categoryFound = category;
                break;
            }
        }
        if (bookToBorrow) break;
    }

    if (bookToBorrow) {
        bookToBorrow.available = false;
        borrowedBooks.push(bookToBorrow);
        let userName = prompt("Enter your name:");
        alert(`Book "${bookToBorrow.title}" has been borrowed by ${userName} successfully!`);
        console.log("Book borrowed:", bookToBorrow);
    } else {
        alert("Book not found or already borrowed!");
    }
};

const returnBook = (searchTerm) => {
    let bookToReturn = null;

    for (let book of borrowedBooks) {
        if (book.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
            book.author.toLowerCase().includes(searchTerm.toLowerCase())) {
            bookToReturn = book;
            break;
        }
    }

    if (bookToReturn) {
        bookToReturn.available = true;
        borrowedBooks.splice(borrowedBooks.indexOf(bookToReturn), 1);
        alert(`Book "${bookToReturn.title}" has been returned successfully!`);
        console.log("Book returned:", bookToReturn);
    } else {
        alert("Book not found in borrowed books!");
    }
};

// Main application
alert("📚 Welcome to the Library Management System!");

let userType = parseInt(prompt("Select user type:\n0 - Librarian\n1 - Library User"));

if (userType === 0) {
    // Librarian operations
    let password = prompt("Enter librarian password:");
    if (password !== "admin123") {
        alert("Incorrect password! Access denied.");
    } else {
        let operation = parseInt(prompt("LIBRARIAN Operations:\n1 - Add Book\n2 - Remove Book\n3 - Search Books\n4 - View All Books by Category\n5 - Exit"));
        
        switch(operation) {
            case 1:
                addBook();
                break;
            case 2:
                let bookToRemove = prompt("Enter book title or author to remove:");
                removeBook(bookToRemove);
                break;
            case 3:
                let searchTerm = prompt("Enter search term:");
                let results = searchBooks(searchTerm);
                if (results.length > 0) {
                    let output = "Search Results:\n\n";
                    results.forEach((book, index) => {
                        let status = book.available ? "Available" : "Borrowed";
                        output += `${index + 1}. "${book.title}" by ${book.author}\n   Category: ${book.category} | Year: ${book.year} | Status: ${status}\n\n`;
                    });
                    alert(output);
                    console.log("Search results:", results);
                } else {
                    alert("No books found matching your search.");
                }
                break;
            case 4:
                displayBooksByCategory();
                break;
            case 5:
                alert("Logging out...");
                break;
            default:
                alert("Invalid operation!");
                break;
        }
    }
} else if (userType === 1) {
    // User operations
    let operation = parseInt(prompt("USER Operations:\n1 - Search Books\n2 - View Books by Category\n3 - Borrow Book\n4 - Return Book\n5 - Exit"));
    
    switch(operation) {
        case 1:
            let searchTerm = prompt("Enter book title, author, or genre:");
            let results = searchBooks(searchTerm);
            if (results.length > 0) {
                let output = "Available Books:\n\n";
                results.forEach((book, index) => {
                    if (book.available) {
                        output += `${index + 1}. "${book.title}" by ${book.author}\n   Category: ${book.category} | Year: ${book.year} | Genre: ${book.genre}\n\n`;
                    }
                });
                alert(output);
                console.log("Search results:", results);
            } else {
                alert("No books found matching your search.");
            }
            break;
        case 2:
            displayBooksByCategory();
            break;
        case 3:
            let bookToBorrow = prompt("Enter book title or author to borrow:");
            borrowBook(bookToBorrow);
            break;
        case 4:
            let bookToReturn = prompt("Enter book title or author to return:");
            returnBook(bookToReturn);
            break;
        case 5:
            alert("Thank you for using the Library Management System!");
            break;
        default:
            alert("Invalid operation!");
            break;
    }
} else {
    alert("Invalid user type selection!");
}