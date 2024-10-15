export async function fetchProjectsTasks(project_id){
    let content = await fetch(`api/projects/${project_id}/tasks/`)
    return content.json()
}

window.fetchProjectsTasks = fetchProjectsTasks;