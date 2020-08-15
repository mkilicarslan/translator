// Materialze init
M.AutoInit();

// Toasts - Flash messsages
const flashMessages = document.querySelectorAll(".flash-messages__item");
for (let i of flashMessages) {
	text = i.innerText;
	M.toast({
		html: text,
		classes: "green",
		displayLength: 6000,
	});
}
// Remove flash messages section
const flashMessagesSection = document.getElementById("flash-messages");
flashMessagesSection.remove();
