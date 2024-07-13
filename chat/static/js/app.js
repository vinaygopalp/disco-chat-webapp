

document.addEventListener("DOMContentLoaded", () => {
    const appContainer = document.getElementById('app-container');
    const loadingScreen = document.getElementById('loading-screen');
    
    // Simulate loading
    setTimeout(() => {
        loadingScreen.style.display = 'none';
        appContainer.style.visibility = 'visible';
    }, 3000);

    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;

    darkModeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
    });

    // Modal functionality
    const profileButton = document.getElementById('profile-button');
    const loginModal = document.getElementById('login-modal');
    const signupModal = document.getElementById('signup-modal');
    const profileModal = document.getElementById('profile-modal');
    const addMemberModal = document.getElementById('add-member-modal');
    const modalOverlay = document.getElementById('modal-overlay');

    profileButton.addEventListener('click', () => {
        profileModal.style.display = 'block';
        modalOverlay.style.display = 'block';
    });

    modalOverlay.addEventListener('click', () => {
        loginModal.style.display = 'none';
        signupModal.style.display = 'none';
        profileModal.style.display = 'none';
        addMemberModal.style.display = 'none';
        modalOverlay.style.display = 'none';
    });

    const showSignup = document.getElementById('show-signup');
    const showLogin = document.getElementById('show-login');

    showSignup.addEventListener('click', () => {
        loginModal.style.display = 'none';
        signupModal.style.display = 'block';
    });

    showLogin.addEventListener('click', () => {
        signupModal.style.display = 'none';
        loginModal.style.display = 'block';
    });

 
    // Add member
    const addMemberButton = document.getElementById('add-member');

    addMemberButton.addEventListener('click', () => {
        addMemberModal.style.display = 'block';
        modalOverlay.style.display = 'block';
    });

    const addMemberSubmit = document.getElementById('add-member-submit');

    addMemberSubmit.addEventListener('click', () => {
        const memberName = document.getElementById('member-name').value.trim();
        if (memberName) {
            alert(`Member ${memberName} added!`);
            addMemberModal.style.display = 'none';
            modalOverlay.style.display = 'none';
        }
    });

  
    const deleteChatRoomButton = document.getElementById('delete-chat-room');

    deleteChatRoomButton.addEventListener('click', () => {
        const chatRoomName = document.getElementById('chat-room-name').textContent;
        if (confirm(`Are you sure you want to delete the chat room: ${chatRoomName}?`)) {
            const chatRooms = document.querySelectorAll('#chat-room-list li');
            chatRooms.forEach(room => {
                if (room.textContent === chatRoomName) {
                    room.remove();
                }
            });
            document.getElementById('chat-room-name').textContent = 'Select a chat room';
            chatMessages.innerHTML = '';
        }
    });

    //gsap.fromTo("#loading-screen", { opacity: 1 }, { opacity: 0, duration: 3, ease: "power2.out" });

 
});



//websockets and encryption
 