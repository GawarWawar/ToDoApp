function task_submit_listen(){
    const formElem = document.querySelector("form");
    formElem.addEventListener("submit", (event) => {
        // on form submission, prevent default
        event.preventDefault();
        
        var xhttp = new XMLHttpRequest();

        // construct a FormData object, which fires the formdata event
        const formData = new FormData(formElem);

        xhttp.withCredentials = "true"
        xhttp.open(formElem.getAttribute('method'), formElem.getAttribute('action'), true);
        xhttp.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        
        xhttp.send(formData);
      });
}

window.task_submit_listen = task_submit_listen;