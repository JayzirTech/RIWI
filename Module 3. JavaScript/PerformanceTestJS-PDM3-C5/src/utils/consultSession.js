export function getSessionUser(){
    const user = localStorage.getItem('user')    
    return user ? JSON.parse(user) : null
}

export function getUserRole(){
    const user = getSessionUser();
    return user ? user.role : null
}