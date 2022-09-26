
function deleteNote(noteId){                                    // Button function used for deleting notes
    fetch('/delete-note',{
        method:"POST",
        body:JSON.stringify({ noteId:noteId }),
    }).then((res)=>{
        window.location.href="/";
    }); 
}
 


