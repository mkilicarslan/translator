// Materialze init
M.AutoInit();

// Toasts - Flash messsages
const flashMessages = document.querySelectorAll(".flash-messages__item");
console.log(flashMessages);
for (let i of flashMessages) {
	text = i.innerText;
	category = i.className.split(" ")[1];

	console.log(i, category);
	M.toast({
		html: text,
		classes: category === "error" ? "red" : "green",
		displayLength: 6000,
	});
}

// Remove flash messages section
const flashMessagesSection = document.getElementById("flash-messages");
flashMessagesSection.remove();
