import { router } from "../router/router"

export function sideBarController() {
    const algo = document.getElementsByTagName('nav')

    localStorage.removeItem('user')
    router()
    return
}