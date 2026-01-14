const additem = () => {
    // Step 1: Read the user input
    let userinput = document.querySelector("#inp").value
    // To see if it is being read
    console.log(userinput)
    // Step 2: Create a list item
    let listitem = document.createElement("li")
    listitem.textContent = userinput
    console.log(listitem)
    // Step 3: Target the list
    let list = document.querySelector("#todo")
    // Step 4: Add item to the list
    list.appendChild(listitem)

}

let addbtn = document.getElementById("addbtn")
addbtn.addEventListener("click", additem)
