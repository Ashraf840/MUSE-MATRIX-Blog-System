const modal = document.querySelector('.newsletter-email-modal');
// const openModalBtn = document.querySelector('.open-modal-btn');
// const openModalBtn = document.querySelector('#open-modal-btn');
const closeModalBtn = document.querySelector('.modal-close-btn');

// console.log('modal', modal);
// console.log('openModalBtn', openModalBtn);
// console.log('closeModalBtn', closeModalBtn);

// Function to open the modal
function openModal() {
    let recipient = document.querySelector('#recipient');
    recipient.value = '';
    // Check if "selectedEmailList" is not empty before opening the email-send-modal
    if (selectedEmailList.length) {
        // Open/Show email-send-modal
        modal.classList.remove('hidden');
        modal.classList.add('flex', 'items-center', 'justify-center');
        modal.setAttribute('aria-hidden', 'false');

        // Put comma after appending each email
        let email_str = '';
        selectedEmailList.forEach((s_email, index, array) => {
            if (index === array.length - 1) {
                // console.log('Last element:', s_email.email);
                email_str += s_email.email;
            } else {
                email_str += s_email.email + ', ';
            }
        });
        // console.log(email_str);
        // Append all the selected emails into the recipient-input-field
        recipient.value = email_str;
    } else {
        console.log("Please select at least one email address");
        // Show a sweet-alert message for not selecting any email
        Swal.fire({
            title: 'Error!',
            text: 'Select at least one email address!',
            icon: 'error',
            confirmButtonText: 'Cancel'
        })
    }
}

// Function to close the modal
function closeModal() {
    modal.classList.remove('flex', 'items-center', 'justify-center');
    modal.classList.add('hidden');
    modal.setAttribute('aria-hidden', 'true');
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