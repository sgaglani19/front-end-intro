function addTask(){
    let taskInput = document.getElementById("tasks")
   let taskValue = taskInput.value;

   if(taskValue.trim() !== ""){
        var newTask = document.createElement("li");

        newTask.textContent = taskValue;

        var taskList = document.getElementById("taskList");

        taskList.appendChild(newTask);

        taskInput.value = "";
   }
   else{
    alert("Please enter a task before submitting.");
   }
}