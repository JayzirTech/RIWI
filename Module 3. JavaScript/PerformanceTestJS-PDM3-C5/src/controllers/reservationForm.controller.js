import { router } from "../router/router"

export function reservationFormController() {
    window.history.pushState({}, '', '/home')
    router()
    return
}