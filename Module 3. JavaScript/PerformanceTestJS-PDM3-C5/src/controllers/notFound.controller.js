import { router } from "../router/router"

export function notFoundController() {
    window.history.pushState({}, '', '/home')
    router()
    return
}