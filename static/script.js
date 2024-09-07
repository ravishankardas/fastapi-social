async function callApi() {
    const response = await fetch('/api_endpoint', {
        method: 'GET',
    });
    const result = await response.json();
    console.log(result);
    alert(result.message);
}

function loadResume() {
    fetch('/api/resume')
    .then(response => {
        if (response.ok) {
            // Redirect to the resume page if the API call is successful
            window.location.href = "/api/resume";
        } else {
            console.error("Failed to load resume.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function backHome(){
    
}