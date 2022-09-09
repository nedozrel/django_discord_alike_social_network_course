const messagesContainer = document.querySelector('.messages');
const messagesList = messagesContainer.querySelector('.messages__list')
let messages = messagesList.querySelectorAll('.messages__item');

for (let message of messages) {
    let cross = message.querySelector('.messages__cross');
    cross.addEventListener('click', deleteMessage);

    function deleteMessage() {
        message.remove();
        messages = messagesList.querySelectorAll('.messages__item');
        if (!messages.length) {
            messagesContainer.remove();
        }
    }
}