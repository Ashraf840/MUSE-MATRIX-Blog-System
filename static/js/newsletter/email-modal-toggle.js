const modal = document.querySelector('.newsletter-email-modal');
// const openModalBtn = document.querySelector('.open-modal-btn');
// const openModalBtn = document.querySelector('#open-modal-btn');
const closeModalBtn = document.querySelector('.modal-close-btn');

let selectedEmailList = [];

// console.log('modal', modal);
// console.log('openModalBtn', openModalBtn);
// console.log('closeModalBtn', closeModalBtn);

// Function to open the modal
function openModal(id) {
    console.log('btn id', id);
    modal.classList.remove('hidden');
    modal.classList.add('flex', 'items-center', 'justify-center');
    modal.setAttribute('aria-hidden', 'false');
}

// Function to close the modal
function closeModal() {
    modal.classList.remove('flex', 'items-center', 'justify-center');
    modal.classList.add('hidden');
    modal.setAttribute('aria-hidden', 'true');
}

function appendEmailChecklist(event, email) {
    console.log('event', event);
    selectedEmailList.push(email);
    console.log('selectedEmailList', selectedEmailList);
}

// Event listener to open the modal when the button is clicked
// openModalBtn.addEventListener('click', openModal);
// openModalBtn.addEventListener('click', () => {
//     console.log('aisdhiasudy');
// });

// Event listener to close the modal when the close button is clicked
closeModalBtn.addEventListener('click', closeModal);
// closeModalBtn.addEventListener('click', () => {
//     console.log('aisdhiasudy');
// });