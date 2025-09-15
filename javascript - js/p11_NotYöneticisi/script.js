/* 
    Script: Öğrenci Not Yönetim Sistemi
    Açıklama: Öğrenci notlarını ve kayıtlarını yönetmek için etkileşimli sistem
    Yazar: [Future Developer] 
    Tarih: 03.09.2025
    Sürüm: 1.0

    Özellikler:
    - Öğretmen Paneli (şifre: teacher123)
    - Öğrenci Paneli (şifre: student123)
    - Not yönetimi, öğrenci kayıtları, istatistikler

    Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.
*/

// Student data by classes
let class9A = [
    { name: "Ali Yılmaz", studentId: "9A001", math: 85, turkish: 78, english: 92, science: 88 },
    { name: "Ayşe Demir", studentId: "9A002", math: 76, turkish: 89, english: 84, science: 79 },
    { name: "Mehmet Kaya", studentId: "9A003", math: 94, turkish: 87, english: 91, science: 96 },
    { name: "Fatma Özkan", studentId: "9A004", math: 68, turkish: 75, english: 72, science: 70 }
];

let class9B = [
    { name: "Ahmet Şahin", studentId: "9B001", math: 82, turkish: 80, english: 88, science: 85 },
    { name: "Zeynep Aslan", studentId: "9B002", math: 90, turkish: 94, english: 86, science: 92 },
    { name: "Can Polat", studentId: "9B003", math: 73, turkish: 69, english: 77, science: 74 }
];

let class10A = [
    { name: "Cem Aydın", studentId: "10A001", math: 89, turkish: 85, english: 90, science: 87 },
    { name: "Elif Yıldız", studentId: "10A002", math: 95, turkish: 92, english: 94, science: 98 },
    { name: "Burak Çelik", studentId: "10A003", math: 71, turkish: 74, english: 68, science: 73 }
];

let classes = [class9A, class9B, class10A];
let classNames = ["9-A", "9-B", "10-A"];
let subjects = ["math", "turkish", "english", "science"];
let subjectNames = ["Mathematics", "Turkish", "English", "Science"];

const addStudent = () => {
    alert("Add a new student to the system");
    let classIndex = parseInt(prompt("Select class:\n1 - 9-A\n2 - 9-B\n3 - 10-A")) - 1;
    
    if (classIndex < 0 || classIndex >= classes.length) {
        alert("Invalid class selection!");
        return;
    }

    let className = classNames[classIndex];
    let studentCount = classes[classIndex].length + 1;
    let studentId = className.replace("-", "") + "0" + (studentCount < 10 ? "0" + studentCount : studentCount);

    let newStudent = {
        name: prompt("Enter student name:"),
        studentId: studentId,
        math: parseInt(prompt("Enter Math grade (0-100):")) || 0,
        turkish: parseInt(prompt("Enter Turkish grade (0-100):")) || 0,
        english: parseInt(prompt("Enter English grade (0-100):")) || 0,
        science: parseInt(prompt("Enter Science grade (0-100):")) || 0
    };

    classes[classIndex].push(newStudent);
    alert(`Student "${newStudent.name}" (ID: ${newStudent.studentId}) has been added to class ${className} successfully!`);
    console.log("New student added:", newStudent);
};

const updateGrades = (searchTerm) => {
    let student = null;
    let classFound = null;

    for (let classGroup of classes) {
        for (let s of classGroup) {
            if (s.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                s.studentId.toLowerCase().includes(searchTerm.toLowerCase())) {
                student = s;
                classFound = classGroup;
                break;
            }
        }
        if (student) break;
    }

    if (student) {
        alert(`Updating grades for: ${student.name} (${student.studentId})`);
        let subject = parseInt(prompt("Select subject to update:\n1 - Mathematics\n2 - Turkish\n3 - English\n4 - Science")) - 1;
        
        if (subject >= 0 && subject < subjects.length) {
            let oldGrade = student[subjects[subject]];
            let newGrade = parseInt(prompt(`Current ${subjectNames[subject]} grade: ${oldGrade}\nEnter new grade (0-100):`));
            
            if (newGrade >= 0 && newGrade <= 100) {
                student[subjects[subject]] = newGrade;
                alert(`${subjectNames[subject]} grade updated from ${oldGrade} to ${newGrade} for ${student.name}`);
                console.log("Grade updated:", student);
            } else {
                alert("Invalid grade! Please enter a value between 0-100.");
            }
        } else {
            alert("Invalid subject selection!");
        }
    } else {
        alert("Student not found!");
    }
};

const calculateAverage = (student) => {
    let total = student.math + student.turkish + student.english + student.science;
    return (total / 4).toFixed(2);
};

const getLetterGrade = (average) => {
    if (average >= 90) return "AA";
    if (average >= 80) return "BA";
    if (average >= 70) return "BB";
    if (average >= 60) return "CB";
    if (average >= 50) return "CC";
    return "FF";
};

const viewStudentRecord = (searchTerm) => {
    let student = null;
    let className = null;

    for (let i = 0; i < classes.length; i++) {
        for (let s of classes[i]) {
            if (s.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                s.studentId.toLowerCase().includes(searchTerm.toLowerCase())) {
                student = s;
                className = classNames[i];
                break;
            }
        }
        if (student) break;
    }

    if (student) {
        let average = calculateAverage(student);
        let letterGrade = getLetterGrade(average);
        
        let output = `STUDENT RECORD\n\nName: ${student.name}\nStudent ID: ${student.studentId}\nClass: ${className}\n\n`;
        output += `GRADES:\nMathematics: ${student.math}\nTurkish: ${student.turkish}\nEnglish: ${student.english}\nScience: ${student.science}\n\n`;
        output += `Average: ${average}\nLetter Grade: ${letterGrade}`;
        
        alert(output);
        console.log("Student record:", student);
    } else {
        alert("Student not found!");
    }
};

const viewClassStatistics = () => {
    let classIndex = parseInt(prompt("Select class for statistics:\n1 - 9-A\n2 - 9-B\n3 - 10-A")) - 1;
    
    if (classIndex < 0 || classIndex >= classes.length) {
        alert("Invalid class selection!");
        return;
    }

    let selectedClass = classes[classIndex];
    let className = classNames[classIndex];
    
    if (selectedClass.length === 0) {
        alert(`No students found in class ${className}`);
        return;
    }

    let output = `CLASS ${className} STATISTICS\n\n`;
    output += `Total Students: ${selectedClass.length}\n\n`;

    // Subject averages
    for (let i = 0; i < subjects.length; i++) {
        let total = 0;
        for (let student of selectedClass) {
            total += student[subjects[i]];
        }
        let average = (total / selectedClass.length).toFixed(2);
        output += `${subjectNames[i]} Average: ${average}\n`;
    }

    // Top student
    let topStudent = selectedClass[0];
    let topAverage = calculateAverage(topStudent);
    
    for (let student of selectedClass) {
        let average = calculateAverage(student);
        if (average > topAverage) {
            topStudent = student;
            topAverage = average;
        }
    }
    
    output += `\nTop Student: ${topStudent.name} (Average: ${topAverage})`;
    
    alert(output);
    console.log("Class statistics for", className, selectedClass);
};

const viewAllStudents = () => {
    let classIndex = parseInt(prompt("Select class:\n1 - 9-A\n2 - 9-B\n3 - 10-A")) - 1;
    
    if (classIndex < 0 || classIndex >= classes.length) {
        alert("Invalid class selection!");
        return;
    }

    let selectedClass = classes[classIndex];
    let className = classNames[classIndex];
    let output = `CLASS ${className} STUDENTS\n\n`;
    
    if (selectedClass.length === 0) {
        output += "No students found in this class.";
    } else {
        selectedClass.forEach((student, index) => {
            let average = calculateAverage(student);
            let letterGrade = getLetterGrade(average);
            output += `${index + 1}. ${student.name} (${student.studentId})\n   Average: ${average} | Grade: ${letterGrade}\n\n`;
        });
    }
    
    alert(output);
};

// Main application
alert("📚 Welcome to the Student Grade Management System!");

let userType = parseInt(prompt("Select user type:\n0 - Teacher\n1 - Student"));

if (userType === 0) {
    // Teacher operations
    let password = prompt("Enter teacher password:");
    if (password !== "teacher123") {
        alert("Incorrect password! Access denied.");
    } else {
        let operation = parseInt(prompt("TEACHER Operations:\n1 - Add Student\n2 - Update Grades\n3 - View Student Record\n4 - View All Students\n5 - Class Statistics\n6 - Exit"));
        
        switch(operation) {
            case 1:
                addStudent();
                break;
            case 2:
                let studentToUpdate = prompt("Enter student name or ID:");
                updateGrades(studentToUpdate);
                break;
            case 3:
                let studentToView = prompt("Enter student name or ID:");
                viewStudentRecord(studentToView);
                break;
            case 4:
                viewAllStudents();
                break;
            case 5:
                viewClassStatistics();
                break;
            case 6:
                alert("Logging out...");
                break;
            default:
                alert("Invalid operation!");
                break;
        }
    }
} else if (userType === 1) {
    // Student operations
    let studentToView = prompt("Enter your name or student ID:");
    viewStudentRecord(studentToView);
} else {
    alert("Invalid user type selection!");
}