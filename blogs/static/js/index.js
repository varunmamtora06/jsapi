function getBlogs(){
fetch('http://127.0.0.1:5000/api/blogs')
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const blogs = data.blogs.map(blog =>{
            console.log(blog.title ,"&&", blog.content);
            return `
            <div class="blog" id="${blog.id}">
                <div class="title" id="title">
                    <p>${blog.title}</p>
                </div>
                <div class="content" id="content">
                    <p>${blog.content}</p>
                </div>
                <button onclick="updateForm(${blog.id})">Edit</button>
                <button onclick="deleteForm(${blog.id})">Detele</button>
            </div>
        `
    }).join("");
    document.querySelector('#blogs').insertAdjacentHTML("afterbegin", blogs);
        
});
}
getBlogs();

function deleteForm(id){
    fetch('http://127.0.0.1:5000/api/deleteblog/'+id)
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
            location.reload();
}

function updateForm(id){
    fetch('http://127.0.0.1:5000/api/blog/'+id)
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const blog_form = document.getElementById('blogForm');
        const title = document.getElementById('title');
        const content = document.getElementById('content');
        const submit_bttn = document.getElementById('submit');

        title.value = data.blog.title;
        content.value = data.blog.content;

        submit_bttn.addEventListener('click',function(e){
            console.log("yess");
            e.preventDefault();
            const form_data = new FormData(blog_form);

            fetch('http://127.0.0.1:5000/api/updateblog/'+id, {
            method: 'POST', // or 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: form_data,
            mode: "no-cors",
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
            location.reload();
        })

    });
}



const blog_form = document.getElementById('blogForm');

blog_form.addEventListener('submit',function (e){
    e.preventDefault();
    
    const form_data = new FormData(this);

    console.log(form_data);
    for (var [key, value] of form_data.entries()) { 
        console.log(key, value);
    }

    fetch('http://127.0.0.1:5000/api/postblog', {
    method: 'POST', // or 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: form_data,
    mode: "no-cors",
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    location.reload();
});
