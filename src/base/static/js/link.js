

function redirectPage(event) {
    // access information to request the link 
    const linkID = event.target.dataset.linkid;
    const pk = event.target.dataset.pk;
    // request the link and redirect user
    fetch(`/link_resolve/?linkid=${linkID}&pk=${pk}`)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
        }
        return response.json()})
    .then(data => {
        window.location.href = data.resolved_url;
    })    .catch(error => {
        console.error("ERROR:", error);
    });;

}

document.addEventListener("openLink", redirectPage);
