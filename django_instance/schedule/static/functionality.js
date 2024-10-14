 /*jslint devel: true */

"use strict";
function build(data) {
    console.log(data);
    var main_block = document.getElementById("main");

    var xmlh = new XMLHttpRequest();
    for (let index = 0; index < data.length; index++) {
        const project = data[index];

        // Element for the project
        const newProject = document.createElement("div");
        
        // Header of the project (blue zone in the top)
        const header = document.createElement("div");
            header.append(document.createTextNode(project.name));
        newProject.appendChild(header);

        // Form to create new tasks for the project
        const creatonForm = document.createElement("form");
            const formInput = document.createElement("input");
                formInput.type = "text";
                formInput.placeholder = "Start typing here to create a task";
            creatonForm.appendChild(formInput);
            const formButton = document.createElement("button");
                formButton.append(document.createTextNode("Add Task"));
            creatonForm.appendChild(formButton);
        newProject.appendChild(creatonForm)

        // List of tasks
        const taskList = document.createElement("ul");
        for (let index = 0; index < project.tasks.length; index++) {
            const task = project.tasks[index];

            // Checkbox to mark task
            const newTask = document.createElement("li");
            const taskCheckBox = document.createElement("input");
                taskCheckBox.type = "checkbox";
                taskCheckBox.id = task.id
            newTask.appendChild(taskCheckBox);

            // Lable for the checkbox
            const taskLabel = document.createElement("label");
                taskLabel.append(document.createTextNode(task.description))
                taskLabel.htmlFor = task.id;
            newTask.appendChild(taskLabel);

            taskList.append(newTask);
        }
        newProject.appendChild(taskList)

        main_block.appendChild(newProject);
    }
}

