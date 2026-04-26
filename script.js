let contacts = [];

function addContact() {
    let name = document.getElementById("name").value;
    let phone = document.getElementById("phone").value;

    if (!name || !phone) {
        alert("Enter all fields!");
        return;
    }

    contacts.push({ name, phone });
    alert("✅ Contact added!");

    document.getElementById("name").value = "";
    document.getElementById("phone").value = "";
}

function viewContacts() {
    let output = document.getElementById("output");
    output.innerHTML = "";

    contacts.forEach(c => {
        output.innerHTML += `<div class="contact">${c.name} - ${c.phone}</div>`;
    });
}

function searchContact() {
    let name = document.getElementById("name").value.toLowerCase();
    let output = document.getElementById("output");
    output.innerHTML = "";

    let found = contacts.filter(c => c.name.toLowerCase() === name);

    if (found.length === 0) {
        output.innerHTML = "❌ Not found";
    } else {
        found.forEach(c => {
            output.innerHTML += `<div class="contact">${c.name} - ${c.phone}</div>`;
        });
    }
}

function deleteContact() {
    let name = document.getElementById("name").value.toLowerCase();

    contacts = contacts.filter(c => c.name.toLowerCase() !== name);

    alert("🗑️ Deleted if existed!");
    viewContacts();
}