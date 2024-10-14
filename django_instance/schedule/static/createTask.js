/*jslint devel: true */

export function create_task_structure(task) {
    // Checkbox to mark task
    const newTask = document.createElement("tr");
        const checkboxColumn = document.createElement("td");
            const taskCheckBox = document.createElement("input");
                taskCheckBox.type = "checkbox";
                taskCheckBox.id = "Project."+task.project_instance.id+".Task."+task.id+".";
            checkboxColumn.appendChild(taskCheckBox);
        newTask.appendChild(checkboxColumn);

    // Task description
        // + lable for the checkbox
        const descriptionColumn = document.createElement("td");
            const taskLabel = document.createElement("label");
                taskLabel.append(document.createTextNode(task.description))
                taskLabel.htmlFor = "Project."+task.project_instance.id+".Task."+task.id+".";
            descriptionColumn.appendChild(taskLabel);
        newTask.appendChild(descriptionColumn);

    return newTask;
}