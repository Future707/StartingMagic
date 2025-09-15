/* 
    Script: Günlük Görev Planlayıcı ve Yapılacaklar Listesi
    Açıklama: Etkileşimli günlük planlama ve görev yönetim sistemi
    Yazar: [Future Developer] 
    Tarih: 02.09.2025
    Sürüm: 1.0

    Özellikler:
    - Öncelik ve kategori ile görev ekleme/çıkarma
    - Görevleri tamamlandı olarak işaretleme
    - Görevleri öncelik, kategori veya duruma göre görüntüleme
    - Günlük verimlilik istatistikleri

    Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.
*/

// Task categories and priorities
let tasks = [];
let categories = ["İş", "Kişisel", "Ev İşleri", "Alışveriş", "Spor", "Eğitim", "Sosyal"];
let priorities = ["Düşük", "Orta", "Yüksek", "Acil"];
let completedTasks = [];

const addTask = () => {
    alert("Yeni görev ekle");
    
    let taskName = prompt("Görev adını girin:");
    if (!taskName || taskName.trim() === "") {
        alert("Görev adı boş olamaz!");
        return;
    }

    // Category selection
    let categoryList = "Kategori seçin:\n";
    categories.forEach((cat, index) => {
        categoryList += `${index + 1} - ${cat}\n`;
    });
    
    let categoryIndex = parseInt(prompt(categoryList)) - 1;
    if (categoryIndex < 0 || categoryIndex >= categories.length) {
        alert("Geçersiz kategori! Varsayılan olarak 'Kişisel' seçildi.");
        categoryIndex = 1;
    }

    // Priority selection
    let priorityList = "Öncelik seçin:\n";
    priorities.forEach((priority, index) => {
        priorityList += `${index + 1} - ${priority}\n`;
    });
    
    let priorityIndex = parseInt(prompt(priorityList)) - 1;
    if (priorityIndex < 0 || priorityIndex >= priorities.length) {
        alert("Geçersiz öncelik! Varsayılan olarak 'Orta' seçildi.");
        priorityIndex = 1;
    }

    // Due date
    let dueDate = prompt("Son tarih (GG/AA/YYYY formatında - opsiyonel):");
    let notes = prompt("Not ekleyin (opsiyonel):");

    let newTask = {
        id: Date.now(),
        name: taskName,
        category: categories[categoryIndex],
        priority: priorities[priorityIndex],
        dueDate: dueDate || "Belirtilmemiş",
        notes: notes || "",
        completed: false,
        createdAt: new Date().toLocaleString("tr-TR")
    };

    tasks.push(newTask);
    alert(`✅ "${taskName}" görevi eklendi!\nKategori: ${newTask.category}\nÖncelik: ${newTask.priority}`);
    console.log("Yeni görev eklendi:", newTask);
};

const viewTasks = () => {
    if (tasks.length === 0) {
        alert("Henüz görev eklenmemiş.");
        return;
    }

    let viewOption = parseInt(prompt("Görüntüleme seçeneği:\n1 - Tüm Görevler\n2 - Tamamlanmamış Görevler\n3 - Tamamlanmış Görevler\n4 - Kategoriye Göre\n5 - Önceliğe Göre"));
    
    let tasksToShow = [];
    let title = "";

    switch(viewOption) {
        case 1:
            tasksToShow = tasks;
            title = "📋 TÜM GÖREVLER";
            break;
        case 2:
            tasksToShow = tasks.filter(task => !task.completed);
            title = "⏳ TAMAMLANMAMIŞ GÖREVLER";
            break;
        case 3:
            tasksToShow = tasks.filter(task => task.completed);
            title = "✅ TAMAMLANMIŞ GÖREVLER";
            break;
        case 4:
            let categoryList = "Kategori seçin:\n";
            categories.forEach((cat, index) => {
                categoryList += `${index + 1} - ${cat}\n`;
            });
            let catIndex = parseInt(prompt(categoryList)) - 1;
            if (catIndex >= 0 && catIndex < categories.length) {
                tasksToShow = tasks.filter(task => task.category === categories[catIndex]);
                title = `📂 ${categories[catIndex].toUpperCase()} GÖREVLERİ`;
            }
            break;
        case 5:
            let priorityList = "Öncelik seçin:\n";
            priorities.forEach((priority, index) => {
                priorityList += `${index + 1} - ${priority}\n`;
            });
            let priIndex = parseInt(prompt(priorityList)) - 1;
            if (priIndex >= 0 && priIndex < priorities.length) {
                tasksToShow = tasks.filter(task => task.priority === priorities[priIndex]);
                title = `🔥 ${priorities[priIndex].toUpperCase()} ÖNCELİKLİ GÖREVLER`;
            }
            break;
        default:
            alert("Geçersiz seçenek!");
            return;
    }

    if (tasksToShow.length === 0) {
        alert("Gösterilecek görev bulunamadı.");
        return;
    }

    let output = `${title}\n\n`;
    
    tasksToShow.forEach((task, index) => {
        let status = task.completed ? "✅" : "⏳";
        let priorityIcon = task.priority === "Acil" ? "🔴" : task.priority === "Yüksek" ? "🟡" : task.priority === "Orta" ? "🟢" : "⚪";
        
        output += `${index + 1}. ${status} ${task.name}\n`;
        output += `   ${priorityIcon} ${task.priority} | 📂 ${task.category}\n`;
        output += `   📅 Son Tarih: ${task.dueDate}\n`;
        if (task.notes) {
            output += `   📝 Not: ${task.notes}\n`;
        }
        output += `   🕒 Oluşturulma: ${task.createdAt}\n`;
        output += `${"=".repeat(40)}\n\n`;
    });
    
    alert(output);
};

const completeTask = () => {
    let incompleteTasks = tasks.filter(task => !task.completed);
    
    if (incompleteTasks.length === 0) {
        alert("Tamamlanacak görev bulunmuyor!");
        return;
    }

    let taskList = "Tamamlanacak görevi seçin:\n\n";
    incompleteTasks.forEach((task, index) => {
        taskList += `${index + 1} - ${task.name} (${task.category})\n`;
    });
    
    let taskIndex = parseInt(prompt(taskList)) - 1;
    
    if (taskIndex >= 0 && taskIndex < incompleteTasks.length) {
        let selectedTask = incompleteTasks[taskIndex];
        selectedTask.completed = true;
        selectedTask.completedAt = new Date().toLocaleString("tr-TR");
        
        completedTasks.push(selectedTask);
        
        alert(`🎉 Tebrikler! "${selectedTask.name}" görevi tamamlandı!\nTamamlanma Zamanı: ${selectedTask.completedAt}`);
        console.log("Görev tamamlandı:", selectedTask);
    } else {
        alert("Geçersiz seçim!");
    }
};

const deleteTask = () => {
    if (tasks.length === 0) {
        alert("Silinecek görev bulunmuyor!");
        return;
    }

    let taskList = "Silinecek görevi seçin:\n\n";
    tasks.forEach((task, index) => {
        let status = task.completed ? "✅" : "⏳";
        taskList += `${index + 1} - ${status} ${task.name} (${task.category})\n`;
    });
    
    let taskIndex = parseInt(prompt(taskList)) - 1;
    
    if (taskIndex >= 0 && taskIndex < tasks.length) {
        let deletedTask = tasks.splice(taskIndex, 1)[0];
        alert(`🗑️ "${deletedTask.name}" görevi silindi.`);
        console.log("Görev silindi:", deletedTask);
    } else {
        alert("Geçersiz seçim!");
    }
};

const searchTasks = () => {
    if (tasks.length === 0) {
        alert("Aranacak görev bulunmuyor!");
        return;
    }

    let searchTerm = prompt("Arama terimi girin (görev adı, kategori veya not):").toLowerCase();
    
    let foundTasks = tasks.filter(task => 
        task.name.toLowerCase().includes(searchTerm) ||
        task.category.toLowerCase().includes(searchTerm) ||
        task.notes.toLowerCase().includes(searchTerm)
    );

    if (foundTasks.length === 0) {
        alert(`"${searchTerm}" için sonuç bulunamadı.`);
        return;
    }

    let output = `🔍 ARAMA SONUÇLARI: "${searchTerm}"\n\n`;
    
    foundTasks.forEach((task, index) => {
        let status = task.completed ? "✅" : "⏳";
        let priorityIcon = task.priority === "Acil" ? "🔴" : task.priority === "Yüksek" ? "🟡" : task.priority === "Orta" ? "🟢" : "⚪";
        
        output += `${index + 1}. ${status} ${task.name}\n`;
        output += `   ${priorityIcon} ${task.priority} | 📂 ${task.category}\n`;
        output += `   📅 ${task.dueDate}\n\n`;
    });
    
    alert(output);
    console.log("Arama sonuçları:", foundTasks);
};

const showStatistics = () => {
    if (tasks.length === 0) {
        alert("İstatistik göstermek için görev bulunmuyor!");
        return;
    }

    let totalTasks = tasks.length;
    let completedCount = tasks.filter(task => task.completed).length;
    let pendingCount = totalTasks - completedCount;
    let completionRate = ((completedCount / totalTasks) * 100).toFixed(1);

    // Category statistics
    let categoryStats = {};
    categories.forEach(cat => {
        categoryStats[cat] = tasks.filter(task => task.category === cat).length;
    });

    // Priority statistics
    let priorityStats = {};
    priorities.forEach(pri => {
        priorityStats[pri] = tasks.filter(task => task.priority === pri).length;
    });

    let output = "📊 GÖREV İSTATİSTİKLERİ\n\n";
    output += `📋 Toplam Görev: ${totalTasks}\n`;
    output += `✅ Tamamlanan: ${completedCount}\n`;
    output += `⏳ Bekleyen: ${pendingCount}\n`;
    output += `📈 Tamamlanma Oranı: %${completionRate}\n\n`;
    
    output += "📂 KATEGORİ DAĞILIMI:\n";
    for (let [category, count] of Object.entries(categoryStats)) {
        if (count > 0) {
            output += `• ${category}: ${count} görev\n`;
        }
    }
    
    output += "\n🔥 ÖNCELİK DAĞILIMI:\n";
    for (let [priority, count] of Object.entries(priorityStats)) {
        if (count > 0) {
            let icon = priority === "Acil" ? "🔴" : priority === "Yüksek" ? "🟡" : priority === "Orta" ? "🟢" : "⚪";
            output += `• ${icon} ${priority}: ${count} görev\n`;
        }
    }

    alert(output);
    console.log("Görev istatistikleri:", { totalTasks, completedCount, pendingCount, categoryStats, priorityStats });
};

const getTodaysTasks = () => {
    let today = new Date().toLocaleDateString("tr-TR");
    let todaysTasks = tasks.filter(task => {
        if (task.dueDate === "Belirtilmemiş") return false;
        try {
            let taskDate = new Date(task.dueDate.split("/").reverse().join("-")).toLocaleDateString("tr-TR");
            return taskDate === today;
        } catch {
            return false;
        }
    });

    if (todaysTasks.length === 0) {
        alert("🗓️ Bugün için planlanmış görev bulunmuyor!");
        return;
    }

    let output = `🗓️ BUGÜNÜN GÖREVLERİ (${today})\n\n`;
    
    todaysTasks.forEach((task, index) => {
        let status = task.completed ? "✅" : "⏳";
        let priorityIcon = task.priority === "Acil" ? "🔴" : task.priority === "Yüksek" ? "🟡" : task.priority === "Orta" ? "🟢" : "⚪";
        
        output += `${index + 1}. ${status} ${task.name}\n`;
        output += `   ${priorityIcon} ${task.priority} | 📂 ${task.category}\n\n`;
    });

    alert(output);
};

// Main application
alert("📝 Günlük Görev Planlayıcısına Hoş Geldiniz!");

let operation = parseInt(prompt("İşlem seçin:\n1 - Görev Ekle\n2 - Görevleri Görüntüle\n3 - Görev Tamamla\n4 - Görev Sil\n5 - Görev Ara\n6 - Bugünün Görevleri\n7 - İstatistikler\n8 - Çıkış"));

switch(operation) {
    case 1:
        addTask();
        break;
    case 2:
        viewTasks();
        break;
    case 3:
        completeTask();
        break;
    case 4:
        deleteTask();
        break;
    case 5:
        searchTasks();
        break;
    case 6:
        getTodaysTasks();
        break;
    case 7:
        showStatistics();
        break;
    case 8:
        alert("📝 Planlayıcıyı kullandığınız için teşekkürler! Productive bir gün geçirin!");
        break;
    default:
        alert("Geçersiz işlem seçimi!");
        break;
}