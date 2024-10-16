function makeXMLRequest(event) {
    const { target } = event;

    let xhttp = new XMLHttpRequest();

    xhttp.open(
        target.getAttribute("method"),
        target.getAttribute("action"),
        true
    );

    const formData = new FormData(target);
    xhttp.send(formData);
    return xhttp
}

window.makeXMLRequest = makeXMLRequest;