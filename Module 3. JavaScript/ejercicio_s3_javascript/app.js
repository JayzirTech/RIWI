let list = document.getElementById('task-list')
let form = document.getElementById('task-form')
let searchInput = document.getElementById('search-task-tittle')
let storage = localStorage

function welcome_message() {
    if (sessionStorage.getItem('name')) {
        alert(`Hello, ${sessionStorage.getItem('name')}. Welcome to your task manager`)
        return
    } 
    const name = prompt("Welcome. Please enter your name:") 
    sessionStorage.setItem('name', name)
    welcome_message()
}

function add_note(title, description) { 
    localStorage.setItem(title,JSON.stringify(description))
    storage = localStorage
    load_localStorage(storage)
}

function load_localStorage(storage, search = "") {
    // Obtiene la ultima busqueda realizada
    const lastSearch = sessionStorage.getItem('lastSearch')

    if (lastSearch) {
        const searchInput = document.getElementById('search-task-tittle')
        if (searchInput) searchInput.value = lastSearch
        if (!search) search = lastSearch
    }

    // Obtiene el ultimo filtro colocado
    const lastFilterSelected = sessionStorage.getItem('lastFilterSelected')

    // Si hay un filtro guardado entra al condicional
    if (lastFilterSelected) {

        // Busca el radio que tenga el valor del filtro guardado y lo guarda en savedRadio
        const savedRadio = document.querySelector(`input[name="task-filter"][value="${lastFilterSelected}"]`)

        // Si encuentra el radio, lo selecciona
        if (savedRadio) savedRadio.checked = true
    }

    // Obtiene el valor del filtro actual 
    const filter = document.querySelector('input[name="task-filter"]:checked').value
    list.innerHTML = ""
    let html = ""

    for (const key in storage) {
        // hasOwnProperty es un metodo que devuelve true si el objeto tiene la propiedad especificada, en este caso key, y false si no la tiene. Esto es para evitar iterar sobre propiedades heredadas del prototipo de localStorage.
        if (!Object.hasOwn(storage, key)) continue;

        let content = JSON.parse(storage[key]);
        let description = content[0]
        let status = content[1]
        let id = key.replace(/ /g,"_")

        // Si el filtro no concuerda con el status de la tarea la salta
        if (filter === 'pending' && status)     continue
        if (filter === 'completed' && !status)      continue

        // Busqueda
        console.log(key);
        console.log(search);
        
        

        if (search && !key.toLowerCase().includes(search.toLowerCase()))continue

        // Aca se usa un operador ternario para asignar la clase completed al li si el status es true, y si no, no asignarle ninguna clase
        html += `
            <li id="${id}" data-key="${key}" status="${status}" class="${status ? 'completed' : ''}">
                <h2>${key}</h2>
                <p>${description}</p>
                <label class="completed-checkbox">
                    <input type="checkbox" class="completed-input" id="completed-${id}" value="completed" ${status ? 'checked' : ''}>
                    <span class="completed-label">Completed</span>
                </label>
                <button class="delete-task" type="button">Delete</button>
            </li>`
    }

    list.innerHTML = html
    
    list.querySelectorAll('.completed-input').forEach((checkbox) => {
        const element = checkbox.closest('li')
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                element.classList.add('completed')
            } else {
                element.classList.remove('completed')
            }
            // dataset es un objeto que contiene todos los atributos data- del elemento, en este caso data-key
            // dataset se podria traducir como data-
            const taskKey = element.dataset.key
            // Agarra el nombre de la tarea, lo busca en el localStorage y lo guarda en la variable contenido
            const content = JSON.parse(localStorage.getItem(taskKey))
            // Modifica el segundo elemento del array contenido, que es el status de la tarea, con el valor del checkbox
            content[1] = this.checked
            // Guarda el contenido modificado en el localStorage, convirtiendolo a string con Json.stringify
            localStorage.setItem(taskKey, JSON.stringify(content))
        })
    })

    list.querySelectorAll('.delete-task').forEach((button) => {
        button.addEventListener('click', function() {
            const element = this.closest('li')
            const taskKey = element.dataset.key
            localStorage.removeItem(taskKey)
            // elimina el elemento del DOM
            element.remove()
        })
    })
}
        
form.addEventListener('submit', (event) => {
    event.preventDefault()
    const title = document.getElementById('task-tittle').value
    const description = document.getElementById('task-input').value
    let nota = [`${description}`, false]
    add_note(title, nota)
    form.reset();
});

searchInput.addEventListener('input', () => {
    const title = searchInput.value
    sessionStorage.setItem('lastSearch', title)
    load_localStorage(storage, title)
})

// Filtro de tareas ----------------------------------
document.querySelectorAll('input[name="task-filter"]').forEach((radio) => {
    radio.addEventListener('change', () => {
        sessionStorage.setItem('lastFilterSelected', radio.value)
        load_localStorage(storage)
    })
})

load_localStorage(storage)
// welcome_message()