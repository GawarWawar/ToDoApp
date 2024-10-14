 /*jslint devel: true */
import { create_task_structure } from "./createTask.js";


function build(data) {
    console.log(data);
    var main_block = document.getElementById("main");

    var xmlh = new XMLHttpRequest();
    for (let index = 0; index < data.length; index++) {
        const project = data[index];

        // Element for the project
        const newProject = document.createElement("div");
            newProject.className = "container";
        
        // Header of the project (blue zone in the top)
        const header = document.createElement("div");
            header.className = "row";
                const headerText = document.createElement("p") 
                headerText.className = "h2"
                headerText.append(document.createTextNode(project.name))
            header.append(headerText);
        newProject.appendChild(header);

        // Form to create new tasks for the project
        const formDiv = document.createElement("div")
        formDiv.className = "row"
            const creationForm = document.createElement("form");
                const formInput = document.createElement("input");
                    formInput.type = "text";
                    formInput.placeholder = "Start typing here to create a task";
                creationForm.appendChild(formInput);
                const formButton = document.createElement("button");
                    formButton.append(document.createTextNode("Add Task"));
                    creationForm.appendChild(formButton);
            formDiv.appendChild(creationForm)
        newProject.appendChild(formDiv)

        // List of tasks
        const taskList = document.createElement("ul");
        taskList.className = "list-group"
        for (let index = 0; index < project.tasks.length; index++) {
            const task = project.tasks[index];
            const newTask = create_task_structure(task);
            taskList.append(newTask);
        }
        newProject.appendChild(taskList)

        main_block.appendChild(newProject);
    }
}

// Expose mainFunction globally
window.build = build;
