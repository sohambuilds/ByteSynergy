const sendRequestBtn = document.getElementById('sendRequestBtn');
const responseElement = document.getElementById('response');

sendRequestBtn.addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:5000/processRequest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: 'Hello there',
                userId: '12312312312'
            })
        });

        const responseData = await response.json();
        responseElement.textContent = responseData.message;
    } catch (error) {
        console.error(error);
    }
});
