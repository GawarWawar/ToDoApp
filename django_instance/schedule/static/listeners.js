document.addEventListener("submit", (event) => {
  // on form submission, prevent default
  event.preventDefault();
  const { target } = event;

  let xhttp = new XMLHttpRequest();

  xhttp.withCredentials = "true";
  xhttp.open(
    target.getAttribute("method"),
    target.getAttribute("action"),
    true
  );
  xhttp.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");

  const formData = new FormData(target);
  xhttp.send(formData);
});
