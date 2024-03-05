


var chat_id;
var user_name;


function overlay_on(){
    console.log("Set overlay on!");

    if (document.getElementById("overlay-bg")){
        return;
    }

    
    var overlay_obj = document.createElement("div");
    overlay_obj.className = "overlay-bg";
    overlay_obj.id = "overlay-bg";


    document.body.appendChild(overlay_obj);
}


function overlay_off(){
    console.log("Set overlay off!");

    var overlay_obj = document.getElementById("overlay-bg");
    
    if (overlay_obj){
        overlay_obj.remove();
    }
}

function set_overlay_box_content(path){
    overlay_on();
   

    var enter_chat_data_obj = document.createElement("div");
    enter_chat_data_obj.className = "overlay-box-container";

    var box_var = document.createElement("div");
    box_var.className = "overlay-box";
    box_var.id = "overlay-box";

    
    $.get(path, function(data){
        box_var.innerHTML = data;
    })

    enter_chat_data_obj.appendChild(box_var);
    document.body.appendChild(enter_chat_data_obj);

}



function create_or_join(){
    set_overlay_box_content("/assets/html/forms/join_or_create.html");

    var box_var = document.getElementById("overlay-box");

    box_var.addEventListener("click", (event) => {
        if (event.target.id === "join-id-btn"){
            join_to_chat();
        }
    })

}


function join_to_chat(){
    set_overlay_box_content("/assets/html/forms/join_chat.html");
    
    var box_var = document.getElementById("overlay-box");

    box_var.addEventListener("click", (event) => {
        alert("join-btn");
        if (event.target.id === "join-btn"){
            join(1);
        }
    })

}


function join(chat_id){
    console.log("Join");
}

document.onload = create_or_join();





