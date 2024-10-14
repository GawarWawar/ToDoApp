export async function fetchProjectsTasks(project_id){
    let content = await fetch(`api/projects/${project_id}/tasks/`)
    return content.json()
}

export function createTask(event){
    const { target } = event;
  
    let xhttp = new XMLHttpRequest();
  
    xhttp.open(
      target.getAttribute("method"),
      target.getAttribute("action"),
      true
    );
    xhttp.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
  
    const formData = new FormData(target);
    xhttp.send(formData);

    return xhttp

  };
  
window.createTask = createTask;
window.fetchProjectsTasks = fetchProjectsTasks;