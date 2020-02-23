document.addEventListener('DOMContentLoaded',()=>{
    alert('Hello')
    var socket=io.connect('http://127.0.0.1:5000')

    socket.on('connect',()=>{
        document.querySelectorAll('button').forEach(button =>{
            button.onclick=()=>{
                alert('Clicked')
                var selection=button.dataset.vote 
                socket.emit('submit vote',{'selection':selection})
            }
        })
    })
    socket.on('announce vote',data=>{
        alert('ASED')
        var li=document.createElement('li')
        li.innerHTML=`Vote Recorded: ${data.selection}`
        document.querySelector('#votes').append(li)
    })
})