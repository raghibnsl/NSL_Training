function deleteNote(noteID){
    fetch('/delete-note',{
        method:"POST",
        body:JSON.stringify({noteId:noteId}),
    }).then((res)=>{
        window.location.href="/";
    }); 
}
 